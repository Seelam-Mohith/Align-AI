# skill_gap.py - Skill Gap Analysis
import re
import json
from typing import List, Dict, Tuple
import os

class SkillGapAnalyzer:
    """
    Analyzes the gap between resume skills and job description requirements
    """
    
    def __init__(self):
        """Initialize with skills database"""
        self.skills_db = self._load_skills_database()
        self.all_skills = self._flatten_skills()
    
    def _load_skills_database(self) -> Dict:
        """Load skills database from JSON"""
        try:
            # Compute absolute path to skills_database.json (2 levels up from ml-service)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_dir)  # Go from ml-service/ to ai-career-assistant/
            skill_paths = [
                os.path.join(project_root, 'skills_database.json'),
                os.path.join(current_dir, '../skills_database.json'),
                'skills_database.json',
            ]
            
            for path in skill_paths:
                abs_path = os.path.abspath(path)
                if os.path.exists(abs_path):
                    print(f"Loading skills database from: {abs_path}")
                    with open(abs_path, 'r') as f:
                        return json.load(f)
            
            print(f"Warning: skills_database.json not found in any of: {skill_paths}")
            return {}
        except Exception as e:
            print(f"Error loading skills database: {e}")
            return {}
    
    def _flatten_skills(self) -> List[str]:
        """Get list of all skills"""
        skills = []
        for category, items in self.skills_db.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        skill_name = item.get('name', '')
                        if skill_name:
                            skills.append(skill_name.lower())
        return skills
    
    def _extract_skills(self, text: str) -> List[str]:
        """
        Extract skills from text using keyword matching
        """
        text_lower = text.lower()
        found_skills = []
        found_set = set()
        
        for skill in self.all_skills:
            # Check for exact word boundaries
            if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
                skill_title = skill.title()
                if skill_title not in found_set:
                    found_skills.append(skill_title)
                    found_set.add(skill_title)
        
        return found_skills
    
    def _generate_recommendations(
        self,
        missing_skills: List[str],
        resume_skills: List[str]
    ) -> List[str]:
        """Generate personalized recommendations"""
        recommendations = []
        
        # Prioritize missing technical skills
        if missing_skills:
            top_missing = missing_skills[:3]
            recommendations.append(
                f"Focus on learning: {', '.join(top_missing)}. These are in high demand."
            )
        
        # Suggest skill combinations
        if 'Python' in resume_skills and 'Machine Learning' in missing_skills:
            recommendations.append(
                "You have Python skills - leverage this to learn Machine Learning frameworks like TensorFlow and PyTorch."
            )
        
        if 'React' in resume_skills and 'Node.js' in resume_skills:
            recommendations.append(
                "Great! You have full-stack skills. Consider learning TypeScript to enhance your JavaScript expertise."
            )
        
        if 'AWS' in missing_skills or 'Cloud' in missing_skills:
            recommendations.append(
                "Cloud skills are highly valuable. Consider AWS or GCP certifications."
            )
        
        # General recommendations
        if not recommendations:
            recommendations.append(
                "Take online courses and build projects using the missing skills."
            )
            recommendations.append(
                "Contribute to open-source projects to gain practical experience."
            )
            recommendations.append(
                "Focus on soft skills like communication and teamwork alongside technical skills."
            )
        
        return recommendations[:5]  # Return top 5 recommendations
    
    def analyze(self, resume_text: str, job_description: str) -> Dict:
        """
        Main analysis method
        Returns: {present, required, missing, recommendations}
        """
        try:
            # Extract skills from both texts
            resume_skills = self._extract_skills(resume_text)
            required_skills = self._extract_skills(job_description)
            
            # Find unique skills
            resume_set = set(s.lower() for s in resume_skills)
            required_set = set(s.lower() for s in required_skills)
            
            # Calculate gaps
            present_skills = list(resume_set & required_set)
            missing_skills = list(required_set - resume_set)
            
            # Capitalize for display
            present_skills = [s.title() for s in present_skills]
            missing_skills = [s.title() for s in missing_skills]
            
            # Generate recommendations
            recommendations = self._generate_recommendations(missing_skills, resume_skills)
            
            return {
                "present": sorted(present_skills),
                "required": sorted(required_skills)[:20],  # Top 20
                "missing": sorted(missing_skills),
                "recommendations": recommendations,
                "overlap_percentage": round(
                    (len(present_skills) / max(len(required_skills), 1)) * 100, 2
                ),
                "message": f"You have {len(present_skills)} out of {len(required_skills)} required skills."
            }
        
        except Exception as e:
            raise Exception(f"Skill Gap Analysis Error: {str(e)}")
