# API_DOCUMENTATION.md - Detailed API Reference

## Base URLs

- **Backend**: `http://localhost:5000`
- **ML Service**: `http://localhost:8000`
- **Frontend**: `http://localhost:3000`

---

## 🔵 ATS Checker Endpoints

### Upload and Analyze Resume

**Endpoint**: `POST /api/ats/upload`

**Description**: Upload a PDF resume and get ATS score analysis

**Request**:
```http
POST /api/ats/upload HTTP/1.1
Host: localhost:5000
Content-Type: multipart/form-data

file: <PDF file>
```

**Response (200 OK)**:
```json
{
  "score": 86,
  "matched": [
    "Python",
    "JavaScript",
    "React",
    "Node.js",
    "MongoDB",
    "Express",
    "Git",
    "Docker",
    "AWS"
  ],
  "missing": [
    "Kubernetes",
    "Rust",
    "Go",
    "Scala",
    "Cassandra",
    "GraphQL",
    "Microservices",
    "Machine Learning",
    "TensorFlow",
    "Kafka"
  ],
  "strength": "Strong",
  "tfidf_score": 45.32,
  "message": "Your resume has 9 matched skills. Focus on adding the missing skills to improve your ATS score."
}
```

**Response (400 Bad Request)**:
```json
{
  "error": "No file provided"
}
```

**Response (500 Internal Server Error)**:
```json
{
  "error": "Error analyzing resume"
}
```

**cURL Example**:
```bash
curl -X POST http://localhost:5000/api/ats/upload \
  -F "file=@resume.pdf"
```

**JavaScript Example**:
```javascript
const formData = new FormData();
formData.append('file', pdfFile);

const response = await fetch('http://localhost:5000/api/ats/upload', {
  method: 'POST',
  body: formData
});

const data = await response.json();
console.log(data);
```

---

## 🔵 Skill Gap Analyzer Endpoints

### Analyze Skill Gap

**Endpoint**: `POST /api/skill-gap/analyze`

**Description**: Compare resume skills with job description requirements

**Request**:
```http
POST /api/skill-gap/analyze HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "resume_text": "I have experience with Python, React, Node.js, MongoDB...",
  "job_description": "Required: Python, Django, PostgreSQL, Docker, AWS..."
}
```

**Response (200 OK)**:
```json
{
  "present": [
    "Docker",
    "Python"
  ],
  "required": [
    "AWS",
    "Django",
    "Docker",
    "PostgreSQL",
    "Python",
    "Kubernetes",
    "Microservices",
    "RESTful APIs"
  ],
  "missing": [
    "AWS",
    "Django",
    "Kubernetes",
    "Microservices",
    "PostgreSQL",
    "RESTful APIs"
  ],
  "recommendations": [
    "Focus on learning: AWS, Django, Kubernetes. These are in high demand.",
    "You have Python skills - leverage this to learn Django framework.",
    "Cloud skills are highly valuable. Consider AWS or GCP certifications.",
    "Take online courses and build projects using the missing skills.",
    "Contribute to open-source projects to gain practical experience."
  ],
  "overlap_percentage": 25.0,
  "message": "You have 2 out of 8 required skills."
}
```

**Response (400 Bad Request)**:
```json
{
  "error": "Resume text and job description are required"
}
```

**cURL Example**:
```bash
curl -X POST http://localhost:5000/api/skill-gap/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "I have Python, React, Node.js",
    "job_description": "Required: Python, Django, PostgreSQL"
  }'
```

**JavaScript Example**:
```javascript
const response = await fetch('http://localhost:5000/api/skill-gap/analyze', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    resume_text: resumeText,
    job_description: jobDescription
  })
});

const data = await response.json();
console.log(data);
```

---

## 🔵 Roadmap Generator Endpoints

### Generate Career Roadmap

**Endpoint**: `POST /api/roadmap/generate`

**Description**: Generate a personalized career roadmap for a given goal

**Request**:
```http
POST /api/roadmap/generate HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "goal": "Web Developer"
}
```

**Response (200 OK)**:
```json
{
  "beginner": [
    {
      "title": "HTML & CSS Fundamentals",
      "description": "Learn the basics of HTML structure and CSS styling",
      "skills": ["HTML", "CSS", "Responsive Design"],
      "duration": "4 weeks"
    },
    {
      "title": "JavaScript Basics",
      "description": "Master JavaScript fundamentals...",
      "skills": ["JavaScript", "DOM", "Events"],
      "duration": "6 weeks"
    }
  ],
  "intermediate": [
    {
      "title": "React Fundamentals",
      "description": "Learn React components, hooks, and state management",
      "skills": ["React", "JSX", "Hooks", "State Management"],
      "duration": "8 weeks"
    }
  ],
  "advanced": [
    {
      "title": "Full Stack Architecture",
      "description": "Design and build complete full-stack applications",
      "skills": ["System Design", "Scalability", "Architecture"],
      "duration": "10 weeks"
    }
  ],
  "goal": "Web Developer",
  "message": "Personalized roadmap for Web Developer",
  "total_duration": "52-78 weeks (1-1.5 years for full track)"
}
```

**Response (400 Bad Request)**:
```json
{
  "error": "Career goal is required"
}
```

**Supported Goals**:
- Web Developer
- AI Engineer
- Data Scientist
- Cybersecurity Analyst
- DevOps Engineer
- Mobile Developer

**cURL Example**:
```bash
curl -X POST http://localhost:5000/api/roadmap/generate \
  -H "Content-Type: application/json" \
  -d '{"goal": "Web Developer"}'
```

**JavaScript Example**:
```javascript
const response = await fetch('http://localhost:5000/api/roadmap/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    goal: 'Web Developer'
  })
});

const data = await response.json();
console.log(data);
```

---

## 🔴 Python ML Service API

### ATS Analysis (Direct ML Service)

**Endpoint**: `POST /ats`

**URL**: `http://localhost:8000/ats`

**Request**:
```http
POST /ats HTTP/1.1
Host: localhost:8000
Content-Type: multipart/form-data

file: <PDF binary>
```

**Response**:
```json
{
  "score": 86,
  "matched": [...],
  "missing": [...],
  "strength": "Strong"
}
```

---

### Skill Gap Analysis (Direct ML Service)

**Endpoint**: `POST /skill-gap`

**URL**: `http://localhost:8000/skill-gap`

**Request**:
```json
{
  "resume_text": "...",
  "job_description": "..."
}
```

**Response**:
```json
{
  "present": [...],
  "required": [...],
  "missing": [...],
  "recommendations": [...]
}
```

---

### Roadmap Generation (Direct ML Service)

**Endpoint**: `POST /roadmap`

**URL**: `http://localhost:8000/roadmap`

**Request**:
```json
{
  "goal": "Web Developer"
}
```

**Response**:
```json
{
  "beginner": [...],
  "intermediate": [...],
  "advanced": [...]
}
```

---

## 📊 Error Codes & Meanings

| Code | Meaning | Solution |
|------|---------|----------|
| 200 | Success | No action needed |
| 400 | Bad Request | Check request parameters |
| 404 | Not Found | Check endpoint URL |
| 500 | Server Error | Check server logs |
| 503 | Service Unavailable | Ensure all services are running |

---

## 🔐 Authentication

Currently, the API has **no authentication**. For production:

1. Implement JWT tokens
2. Use API keys
3. Add rate limiting
4. Implement user authentication

---

## 📝 Request/Response Examples

### Complete Flow Example

```javascript
// 1. Upload Resume and Get ATS Score
async function uploadResume(pdfFile) {
  const formData = new FormData();
  formData.append('file', pdfFile);
  
  const response = await fetch('http://localhost:5000/api/ats/upload', {
    method: 'POST',
    body: formData
  });
  
  return await response.json();
}

// 2. Analyze Skill Gap
async function analyzeSkillGap(resumeText, jobDescription) {
  const response = await fetch('http://localhost:5000/api/skill-gap/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      resume_text: resumeText,
      job_description: jobDescription
    })
  });
  
  return await response.json();
}

// 3. Generate Roadmap
async function generateRoadmap(goal) {
  const response = await fetch('http://localhost:5000/api/roadmap/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ goal })
  });
  
  return await response.json();
}

// Usage
const atsResult = await uploadResume(file);
const gapResult = await analyzeSkillGap(resume, jobDesc);
const roadmapResult = await generateRoadmap('Web Developer');
```

---

## 🚀 API Response Times

Typical response times:

| Endpoint | Time |
|----------|------|
| ATS Upload | 2-5 seconds |
| Skill Gap | 1-2 seconds |
| Roadmap | <1 second |

---

## 📚 Database Collections

### UserHistory Collection

```json
{
  "_id": ObjectId,
  "userId": "guest",
  "analysisType": "ats|skill-gap|roadmap",
  "data": { /* analysis result */ },
  "metadata": {
    "resumeName": "resume.pdf",
    "jobTitle": "Senior Developer",
    "careerGoal": "Web Developer"
  },
  "createdAt": ISODate,
  "updatedAt": ISODate
}
```

---

This API documentation provides everything needed to integrate with and use the AI Career Assistant backend services.
