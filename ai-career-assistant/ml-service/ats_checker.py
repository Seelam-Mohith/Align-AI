import os
import io
import json
import pdfplumber
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from typing import Dict, List, Tuple

# Force Transformers to skip TensorFlow and use PyTorch-only code paths.
os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
os.environ.setdefault("USE_TF", "0")

from datasets import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)
import kagglehub


class ATSChecker:
    """Compatibility ATS analyzer used by the FastAPI `/ats` endpoint."""

    def __init__(self):
        self.skills_db = self._load_skills_database()
        self.all_skills = self._flatten_skills()

    def _load_skills_database(self) -> Dict:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        skill_paths = [
            os.path.join(project_root, "skills_database.json"),
            os.path.join(current_dir, "../skills_database.json"),
            "skills_database.json",
        ]
        for path in skill_paths:
            abs_path = os.path.abspath(path)
            if os.path.exists(abs_path):
                with open(abs_path, "r", encoding="utf-8") as file:
                    return json.load(file)
        return {}

    def _flatten_skills(self) -> Dict[str, int]:
        skills = {}
        for _, items in self.skills_db.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        name = item.get("name", "").strip().lower()
                        weight = int(item.get("weight", 1))
                        if name:
                            skills[name] = max(1, weight)
        return skills

    def _extract_pdf_text(self, pdf_bytes: bytes) -> str:
        text = ""
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()

    def _extract_skills_from_text(self, text: str) -> Tuple[List[str], List[str]]:
        text_lower = text.lower()
        matched = []
        matched_set = set()

        for skill in self.all_skills.keys():
            if re.search(r"\\b" + re.escape(skill) + r"\\b", text_lower):
                if skill not in matched_set:
                    matched_set.add(skill)
                    matched.append(skill.title())

        missing = []
        for skill, _weight in sorted(self.all_skills.items(), key=lambda item: item[1], reverse=True):
            if skill not in matched_set:
                missing.append(skill.title())
            if len(missing) >= 10:
                break

        return matched, missing

    def _keyword_score(self, resume_text: str, keywords: List[str]) -> float:
        if not keywords:
            return 0.0
        resume_tokens = set(re.findall(r"[a-zA-Z][a-zA-Z0-9+.#-]{1,}", resume_text.lower()))
        if not resume_tokens:
            return 0.0
        keyword_tokens = set()
        for keyword in keywords:
            keyword_tokens.update(re.findall(r"[a-zA-Z][a-zA-Z0-9+.#-]{1,}", keyword.lower()))
        if not keyword_tokens:
            return 0.0
        return min(100.0, round((len(resume_tokens & keyword_tokens) / len(keyword_tokens)) * 100, 2))

    def analyze(self, pdf_bytes: bytes) -> Dict:
        resume_text = self._extract_pdf_text(pdf_bytes)
        if not resume_text:
            raise Exception("Could not extract text from PDF")

        matched_skills, missing_skills = self._extract_skills_from_text(resume_text)
        keyword_score = self._keyword_score(resume_text, list(self.all_skills.keys())[:50])

        total_skills = max(1, len(self.all_skills))
        skill_component = min(40.0, (len(matched_skills) / total_skills) * 40.0)
        total_score = int(min(100.0, skill_component + (0.4 * keyword_score) + 20.0))

        if total_score >= 80:
            strength = "Excellent"
        elif total_score >= 65:
            strength = "Strong"
        elif total_score >= 50:
            strength = "Moderate"
        else:
            strength = "Weak"

        return {
            "score": total_score,
            "matched": matched_skills[:20],
            "missing": missing_skills[:10],
            "strength": strength,
            "bert_score": 0.0,
            "tfidf_score": keyword_score,
            "message": (
                f"Your resume has {len(matched_skills)} matched skills. "
                "Focus on adding the missing skills to improve your ATS score."
            ),
        }


def resolve_resumes_dir() -> str:
    """Resolve the source directory for resume PDFs."""
    env_resumes_dir = os.getenv("RESUMES_DIR")
    if env_resumes_dir and os.path.isdir(env_resumes_dir):
        print(f"Using RESUMES_DIR from environment: {env_resumes_dir}")
        return env_resumes_dir

    local_resumes_dir = os.path.join(os.getcwd(), "Resumes")
    if os.path.isdir(local_resumes_dir):
        print(f"Using local resumes directory: {local_resumes_dir}")
        return local_resumes_dir

    print("Local resumes folder not found. Downloading dataset via KaggleHub...")
    path = kagglehub.dataset_download("hadikp/resume-data-pdf")
    print(f"Dataset path: {path}")

    resumes_dir = os.path.join(path, "Resumes")
    if os.path.isdir(resumes_dir):
        return resumes_dir

    # Fall back in case KaggleHub wraps data in an extra folder.
    for entry in os.listdir(path):
        candidate = os.path.join(path, entry, "Resumes")
        if os.path.isdir(candidate):
            return candidate

    raise FileNotFoundError(
        "Could not find a 'Resumes' folder. "
        "Set RESUMES_DIR to your local folder or verify Kaggle dataset contents."
    )


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file path."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def tokenize(batch, tokenizer):
    """Tokenize a batch of resume text."""
    return tokenizer(
        batch["text"],
        max_length=512,
        padding="max_length",
        truncation=True,
    )


def main() -> None:
    resumes_dir = resolve_resumes_dir()
    print(f"Resumes directory: {resumes_dir}")

    records = []
    for current_root, _, filenames in os.walk(resumes_dir):
        pdf_filenames = [name for name in filenames if name.lower().endswith(".pdf")]
        if not pdf_filenames:
            continue

        relative_root = os.path.relpath(current_root, resumes_dir)
        if relative_root in (".", ""):
            continue

        category = relative_root.split(os.sep, 1)[0]
        for filename in pdf_filenames:
            pdf_path = os.path.join(current_root, filename)
            try:
                text = extract_text_from_pdf(pdf_path)
                if text:
                    records.append({"text": text, "label": category})
            except Exception as err:
                print(f"Warning: could not read {pdf_path}: {err}")

    print(f"Total samples extracted: {len(records)}")
    if not records:
        raise ValueError(
            "No resume text extracted. Ensure your folder has PDFs under class subfolders."
        )

    df = pd.DataFrame(records, columns=["text", "label"])
    print(df["label"].value_counts())

    label_encoder = LabelEncoder()
    df["label"] = label_encoder.fit_transform(df["label"])
    num_labels = len(label_encoder.classes_)
    print(f"Number of unique labels: {num_labels}")
    print(f"Classes: {list(label_encoder.classes_)}")

    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df["label"],
    )
    train_df = train_df.reset_index(drop=True)
    test_df = test_df.reset_index(drop=True)
    print(f"Train size: {len(train_df)}, Test size: {len(test_df)}")

    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    train_dataset = Dataset.from_pandas(train_df)
    test_dataset = Dataset.from_pandas(test_df)

    train_dataset = train_dataset.map(lambda batch: tokenize(batch, tokenizer), batched=True)
    test_dataset = test_dataset.map(lambda batch: tokenize(batch, tokenizer), batched=True)

    train_dataset = train_dataset.rename_column("label", "labels")
    test_dataset = test_dataset.rename_column("label", "labels")

    columns = ["input_ids", "attention_mask", "labels"]
    if "token_type_ids" in train_dataset.column_names and "token_type_ids" in test_dataset.column_names:
        columns.insert(2, "token_type_ids")

    train_dataset.set_format(type="torch", columns=columns)
    test_dataset.set_format(type="torch", columns=columns)

    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=num_labels,
    )

    training_args = TrainingArguments(
        output_dir="./bert_results",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_dir="./logs",
        load_best_model_at_end=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
    )

    print("Starting training...")
    trainer.train()

    print("Evaluating...")
    metrics = trainer.evaluate()
    print(metrics)

    save_dir = "./bert_resume_model"
    trainer.save_model(save_dir)
    tokenizer.save_pretrained(save_dir)
    print(f"Model and tokenizer saved to {save_dir}/")


if __name__ == "__main__":
    main()
