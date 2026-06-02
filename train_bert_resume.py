import os
import pdfplumber
import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Force Transformers to skip TensorFlow and use PyTorch-only code paths.
os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
os.environ.setdefault("USE_TF", "0")

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import kagglehub

# ── 1. Resolve dataset location ───────────────────────────────────────────────
def resolve_resumes_dir():
    # Priority order:
    # 1) RESUMES_DIR env var (absolute path to the folder containing class folders)
    # 2) ./Resumes under current working directory
    # 3) KaggleHub download fallback
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

    # Fall back: search one level deeper in case KaggleHub adds a version folder.
    for entry in os.listdir(path):
        candidate = os.path.join(path, entry, "Resumes")
        if os.path.isdir(candidate):
            return candidate

    raise FileNotFoundError(
        "Could not find a 'Resumes' folder. "
        "Set RESUMES_DIR to your local folder or verify Kaggle dataset contents."
    )


# ── 2. PDF text extraction ────────────────────────────────────────────────────
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


# ── 3. Traverse dataset directory ─────────────────────────────────────────────
resumes_dir = resolve_resumes_dir()
print(f"Resumes directory: {resumes_dir}")

records = []
for current_root, _, filenames in os.walk(resumes_dir):
    pdf_filenames = [name for name in filenames if name.lower().endswith(".pdf")]
    if not pdf_filenames:
        continue

    relative_root = os.path.relpath(current_root, resumes_dir)
    if relative_root in (".", ""):
        # Skip PDFs directly under the root; they have no class label folder.
        continue

    category = relative_root.split(os.sep, 1)[0]
    for filename in pdf_filenames:
        pdf_path = os.path.join(current_root, filename)
        try:
            text = extract_text_from_pdf(pdf_path)
            if text:
                records.append({"text": text, "label": category})
        except Exception as e:
            print(f"  Warning: could not read {pdf_path}: {e}")

print(f"Total samples extracted: {len(records)}")

if not records:
    raise ValueError(
        "No resume text extracted. Ensure your folder has PDFs under class subfolders."
    )


# ── 4. Build DataFrame ────────────────────────────────────────────────────────
df = pd.DataFrame(records, columns=["text", "label"])
print(df["label"].value_counts())


# ── 5. Encode labels ──────────────────────────────────────────────────────────
le = LabelEncoder()
df["label"] = le.fit_transform(df["label"])
num_labels = len(le.classes_)
print(f"Number of unique labels: {num_labels}")
print(f"Classes: {list(le.classes_)}")


# ── 6. Train/test split ───────────────────────────────────────────────────────
train_df, test_df = train_test_split(
    df, test_size=0.2, random_state=42, stratify=df["label"]
)
train_df = train_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)
print(f"Train size: {len(train_df)}, Test size: {len(test_df)}")


# ── 7. Load tokenizer ─────────────────────────────────────────────────────────
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


# ── 8. Tokenisation helper ────────────────────────────────────────────────────
def tokenize(batch):
    return tokenizer(
        batch["text"],
        max_length=512,
        padding="max_length",
        truncation=True,
    )


# ── 9. Convert to HuggingFace Dataset ────────────────────────────────────────
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

train_dataset = train_dataset.map(tokenize, batched=True)
test_dataset = test_dataset.map(tokenize, batched=True)

train_dataset = train_dataset.rename_column("label", "labels")
test_dataset = test_dataset.rename_column("label", "labels")

train_dataset.set_format(
    type="torch", columns=["input_ids", "attention_mask", "token_type_ids", "labels"]
)
test_dataset.set_format(
    type="torch", columns=["input_ids", "attention_mask", "token_type_ids", "labels"]
)


# ── 10. Load BERT model ───────────────────────────────────────────────────────
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=num_labels,
)


# ── 11. Training configuration ────────────────────────────────────────────────
training_args = TrainingArguments(
    output_dir="./bert_results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    load_best_model_at_end=True,
)


# ── 12 & 13. Initialise and train ─────────────────────────────────────────────
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

print("Starting training…")
trainer.train()


# ── 14. Evaluate ──────────────────────────────────────────────────────────────
print("Evaluating…")
metrics = trainer.evaluate()
print(metrics)


# ── 15. Save model and tokenizer ──────────────────────────────────────────────
save_dir = "./bert_resume_model"
trainer.save_model(save_dir)
tokenizer.save_pretrained(save_dir)
print(f"Model and tokenizer saved to {save_dir}/")
