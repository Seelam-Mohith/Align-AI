# AI Career Assistant - Complete Setup Guide

## 📋 Project Overview

AI Career Assistant is a full-stack MERN + Python microservice application that provides three AI-powered career development tools:

1. **Resume ATS Score Checker** - Analyze resume for ATS compatibility
2. **Skill Gap Analyzer** - Compare resume vs job description
3. **AI Roadmap Generator** - Generate personalized career roadmaps

## 🏗️ Architecture

```
┌─────────────────┐
│   React App     │ (Port 3000)
│   (Frontend)    │
└────────┬────────┘
         │
┌────────▼────────────────┐
│  Express/Node.js        │ (Port 5000)
│  (Backend API)          │
└────────┬────────────────┘
         │
┌────────▼────────────────┐
│  FastAPI Service        │ (Port 8000)
│  (ML/Python Service)    │
└─────────────────────────┘
         │
    MongoDB (Port 27017)
```

## 📁 Folder Structure

```
ai-career-assistant/
├── client/                      # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── ATSChecker.js
│   │   │   ├── SkillGapAnalyzer.js
│   │   │   └── RoadmapGenerator.js
│   │   ├── components/
│   │   │   ├── Navbar.js
│   │   │   ├── FileUpload.js
│   │   │   ├── SkillChips.js
│   │   │   └── CircularScore.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── server/                      # Express Backend
│   ├── models/
│   │   └── UserHistory.js
│   ├── controllers/
│   │   ├── ats.controller.js
│   │   ├── skillGap.controller.js
│   │   └── roadmap.controller.js
│   ├── routes/
│   │   ├── ats.routes.js
│   │   ├── skillGap.routes.js
│   │   └── roadmap.routes.js
│   ├── middleware/
│   │   └── upload.js
│   ├── uploads/
│   ├── server.js
│   ├── .env
│   └── package.json
│
├── ml-service/                  # Python FastAPI Microservice
│   ├── main.py
│   ├── ats_checker.py
│   ├── skill_gap.py
│   ├── roadmap_generator.py
│   └── requirements.txt
│
└── skills_database.json         # Shared skills database
```

## 🚀 Quick Start

### Prerequisites

- Node.js (v16+)
- Python (v3.8+)
- MongoDB (v4.4+)
- npm or yarn

### 1. Setup Backend (Node.js)

```bash
cd server
npm install

# Create .env file (already provided)
# Start the server
npm start
# or for development with auto-reload
npm run dev
```

Server runs on: `http://localhost:5000`

### 2. Setup ML Service (Python)

```bash
cd ml-service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model (optional but recommended)
python -m spacy download en_core_web_sm

# Start the FastAPI server
python main.py
```

Server runs on: `http://localhost:8000`

### 3. Setup Frontend (React)

```bash
cd client
npm install

# Start the development server
npm start
```

App runs on: `http://localhost:3000`

### 4. Setup MongoDB

```bash
# Using MongoDB Atlas (Cloud):
# 1. Create account at mongodb.com
# 2. Create cluster
# 3. Update MONGODB_URI in server/.env

# Or using local MongoDB:
# 1. Install MongoDB locally
# 2. Run: mongod
```

## 🔧 Configuration

### Environment Variables

**server/.env**
```
MONGODB_URI=mongodb://localhost:27017/ai-career-assistant
PYTHON_SERVICE_URL=http://localhost:8000
PORT=5000
NODE_ENV=development
```

## 📚 API Endpoints

### ATS Checker
```
POST /api/ats/upload
- Form Data: file (PDF)
- Response: {score, matched, missing, strength}
```

### Skill Gap Analyzer
```
POST /api/skill-gap/analyze
- Body: {resume_text, job_description}
- Response: {present, required, missing, recommendations}
```

### Roadmap Generator
```
POST /api/roadmap/generate
- Body: {goal}
- Response: {beginner, intermediate, advanced, message}
```

## 🎨 Features

### 1. Resume ATS Score Checker
- 📄 Upload PDF resume
- 🔍 Extract text from PDF
- 📊 Calculate ATS score (0-100)
- ✅ Show matched skills
- ⚠️ Show missing skills
- 📈 Visual circular progress bar
- 💾 Save analysis to MongoDB

**Scoring Algorithm:**
- 40% skill matching
- 40% TF-IDF similarity
- 20% formatting bonus

### 2. Skill Gap Analyzer
- 📝 Paste resume text
- 📋 Paste job description
- 🔄 Compare skills
- 💡 Get personalized recommendations
- 📊 Show overlap percentage
- 📈 Visual comparison table

### 3. AI Roadmap Generator
- 🎯 Select career goal
- 📍 Get 3-level roadmap (Beginner, Intermediate, Advanced)
- ⏱️ Duration estimates
- 🎓 Skill requirements
- 📚 Learning path
- 🏢 Support for 6+ career paths

## 🛠️ Technology Stack

### Frontend
- **React 18** - UI library
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Recharts** - Data visualization
- **CSS3** - Styling

### Backend
- **Express.js** - Web framework
- **Mongoose** - MongoDB ODM
- **Multer** - File upload handling
- **Axios** - HTTP client
- **CORS** - Cross-origin requests

### ML Service
- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **pdfplumber** - PDF text extraction
- **scikit-learn** - Machine learning
- **NumPy** - Numerical computing
- **spaCy** - NLP (optional)

### Database
- **MongoDB** - NoSQL database

## 📦 Skills Database Structure

```json
{
  "languages": [...],
  "frameworks": [...],
  "tools": [...],
  "cloud": [...],
  "databases": [...],
  "soft_skills": [...],
  "specializations": [...]
}
```

Each skill has:
- `name`: Skill name
- `category`: Skill category
- `weight`: Importance weight (1-10)

## 🎓 Supported Career Paths

1. **Web Developer** - 52-78 weeks
2. **AI Engineer** - 52-78 weeks
3. **Data Scientist** - 52-78 weeks
4. **Cybersecurity Analyst** - 52-78 weeks
5. **DevOps Engineer** - 52-78 weeks
6. **Mobile Developer** - 52-78 weeks

Each path includes:
- Beginner level (Foundation)
- Intermediate level (Core skills)
- Advanced level (Specialization)

## 🧪 Testing the Application

### Test ATS Checker
1. Go to ATS Checker page
2. Upload a PDF resume
3. Click "Analyze Resume"
4. View score and recommendations

### Test Skill Gap Analyzer
1. Go to Skill Gap page
2. Paste resume text
3. Paste job description
4. Click "Analyze Gap"
5. View overlaps and recommendations

### Test Roadmap Generator
1. Go to Roadmap page
2. Select a career goal (or type custom)
3. Click "Generate Roadmap"
4. Expand sections to view learning path

## 🔒 Security Considerations

1. **File Uploads**: Validate file types and sizes
2. **CORS**: Whitelist specific domains
3. **Input Validation**: Validate all inputs with Pydantic
4. **Error Handling**: Don't expose sensitive stack traces
5. **Environment Variables**: Keep secrets in .env files

## 🚨 Troubleshooting

### Port Already in Use
```bash
# Find and kill process using port
# Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :3000
kill -9 <PID>
```

### MongoDB Connection Error
```
1. Ensure MongoDB is running
2. Check MONGODB_URI in .env
3. Verify network access in MongoDB Atlas
```

### Python Dependencies Error
```bash
# Reinstall requirements
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### CORS Errors
```
1. Check CORS middleware in server.js
2. Ensure frontend URL is whitelisted
3. Check browser console for specific errors
```

## 📈 Performance Optimization

1. **Frontend**:
   - Code splitting with React.lazy()
   - Memoization with useMemo
   - Virtual scrolling for large lists

2. **Backend**:
   - Database indexing
   - Caching with Redis (optional)
   - Request rate limiting

3. **ML Service**:
   - Model caching
   - Async processing
   - Batch operations

## 🔄 Deployment

### Deploy to Heroku

#### Backend
```bash
cd server
heroku create your-app-name
heroku addons:create mongolab:sandbox
git push heroku main
```

#### ML Service
```bash
cd ml-service
heroku create your-ml-app-name
git push heroku main
```

#### Frontend
```bash
cd client
npm run build
# Deploy to Vercel, Netlify, or GitHub Pages
```

## 📚 Additional Resources

- [React Documentation](https://react.dev)
- [Express.js Guide](https://expressjs.com)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [MongoDB Manual](https://docs.mongodb.com/manual)
- [Mongoose Docs](https://mongoosejs.com)

## 📝 License

MIT License - Feel free to use this project for learning and development.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## 📧 Support

For issues or questions:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Include error logs and steps to reproduce

---

**Happy coding! 🚀**
