# main.py - FastAPI main server
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
import json
import os

# Import modules
from ats_checker import ATSChecker
from skill_gap import SkillGapAnalyzer
from roadmap_generator import RoadmapGenerator

# Initialize FastAPI app
app = FastAPI(title="AI Career Assistant ML Service", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
ats_checker = ATSChecker()
skill_gap_analyzer = SkillGapAnalyzer()
roadmap_generator = RoadmapGenerator()

# Pydantic models for request/response
class SkillGapRequest(BaseModel):
    resume_text: str
    job_description: str

class RoadmapRequest(BaseModel):
    goal: str

# Routes
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ML service is running"}

@app.post("/ats")
async def analyze_ats(file: UploadFile = File(...)):
    """
    Analyze resume for ATS score
    - Extract PDF text
    - Match with skills database
    - Calculate ATS score
    """
    try:
        print(f"DEBUG: File received: {file.filename}, content_type: {file.content_type}")
        
        # Allow both PDF and common misnamed types
        if file.content_type not in ["application/pdf", "application/octet-stream"]:
            # Try to check file extension instead
            if not file.filename.lower().endswith('.pdf'):
                raise HTTPException(status_code=400, detail=f"File must be PDF. Got: {file.content_type}")
        
        # Read file content
        contents = await file.read()
        print(f"DEBUG: File size: {len(contents)} bytes")
        
        # Analyze with ATS checker
        result = ats_checker.analyze(contents)
        print(f"DEBUG: Analysis result: {result}")
        
        return result
    except Exception as e:
        print(f"ERROR in analyze_ats: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/skill-gap")
async def analyze_skill_gap(request: SkillGapRequest):
    """
    Analyze skill gap between resume and job description
    - Extract skills from resume
    - Extract skills from job description
    - Find gaps and overlaps
    """
    try:
        result = skill_gap_analyzer.analyze(
            request.resume_text,
            request.job_description
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/roadmap")
async def generate_roadmap(request: RoadmapRequest):
    """
    Generate career roadmap for given goal
    """
    try:
        result = roadmap_generator.generate(request.goal)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
