# DIRECTORY_STRUCTURE.md - Complete File Listing

## 📁 Full Directory Tree

```
ai-career-assistant/                                (Root Directory)
│
├── 📄 README.md                                    (Project overview & architecture)
├── 📄 INSTALLATION_GUIDE.md                        (Step-by-step installation)
├── 📄 API_DOCUMENTATION.md                         (API endpoints reference)
├── 📄 FEATURES.md                                  (Feature specifications)
├── 📄 QUICK_START.md                               (5-minute quick start)
├── 📄 PROJECT_COMPLETION_SUMMARY.md                (This project summary)
├── 📄 DIRECTORY_STRUCTURE.md                       (File listing - this file)
├── 📄 .gitignore                                   (Git ignore rules)
├── 📄 start-all.bat                                (Windows startup script)
├── 📄 start-all.sh                                 (macOS/Linux startup script)
├── 📄 skills_database.json                         (Shared skills database)
│
├── 📁 client/                                      (React Frontend)
│   ├── 📄 package.json                             (Dependencies & scripts)
│   ├── 📁 public/
│   │   └── 📄 index.html                           (HTML entry point)
│   └── 📁 src/
│       ├── 📄 index.js                             (React entry point)
│       ├── 📄 index.css                            (Global styles)
│       ├── 📄 App.js                               (Main app component)
│       ├── 📄 App.css                              (App styles)
│       │
│       ├── 📁 pages/
│       │   ├── 📄 ATSChecker.js                    (ATS analysis page)
│       │   ├── 📄 ATSChecker.css                   (ATS page styles)
│       │   ├── 📄 SkillGapAnalyzer.js              (Skill gap page)
│       │   ├── 📄 SkillGapAnalyzer.css             (Skill gap styles)
│       │   ├── 📄 RoadmapGenerator.js              (Roadmap page)
│       │   └── 📄 RoadmapGenerator.css             (Roadmap styles)
│       │
│       └── 📁 components/
│           ├── 📄 Navbar.js                        (Navigation component)
│           ├── 📄 Navbar.css                       (Navbar styles)
│           ├── 📄 FileUpload.js                    (File upload component)
│           ├── 📄 FileUpload.css                   (File upload styles)
│           ├── 📄 CircularScore.js                 (Score circle component)
│           ├── 📄 CircularScore.css                (Score circle styles)
│           ├── 📄 SkillChips.js                    (Skill chips component)
│           └── 📄 SkillChips.css                   (Skill chips styles)
│
├── 📁 server/                                      (Express Backend)
│   ├── 📄 package.json                             (Dependencies & scripts)
│   ├── 📄 server.js                                (Main server file)
│   ├── 📄 .env                                     (Environment variables)
│   ├── 📄 .env.example                             (Environment template)
│   │
│   ├── 📁 routes/
│   │   ├── 📄 ats.routes.js                        (ATS endpoint routes)
│   │   ├── 📄 skillGap.routes.js                   (Skill gap routes)
│   │   └── 📄 roadmap.routes.js                    (Roadmap routes)
│   │
│   ├── 📁 controllers/
│   │   ├── 📄 ats.controller.js                    (ATS logic & API calls)
│   │   ├── 📄 skillGap.controller.js               (Skill gap logic)
│   │   └── 📄 roadmap.controller.js                (Roadmap logic)
│   │
│   ├── 📁 middleware/
│   │   └── 📄 upload.js                            (Multer file upload config)
│   │
│   ├── 📁 models/
│   │   └── 📄 UserHistory.js                       (MongoDB schema)
│   │
│   └── 📁 uploads/                                 (Uploaded PDF files)
│       └── 📄 .gitkeep                             (Git tracking placeholder)
│
└── 📁 ml-service/                                  (Python FastAPI Service)
    ├── 📄 main.py                                  (FastAPI server & routes)
    ├── 📄 requirements.txt                         (Python dependencies)
    ├── 📄 ats_checker.py                           (ATS analysis module)
    ├── 📄 skill_gap.py                             (Skill gap module)
    └── 📄 roadmap_generator.py                     (Roadmap generation module)
```

---

## 📊 File Count Summary

| Directory | Files | Type |
|-----------|-------|------|
| Root | 12 | Documentation & Config |
| client/public | 1 | HTML |
| client/src | 1 | JavaScript |
| client/src/pages | 6 | React + CSS |
| client/src/components | 8 | React + CSS |
| server | 1 | JavaScript |
| server/routes | 3 | JavaScript |
| server/controllers | 3 | JavaScript |
| server/middleware | 1 | JavaScript |
| server/models | 1 | JavaScript |
| server/config | 2 | Environment |
| ml-service | 5 | Python |
| **Total** | **44** | **Files** |

---

## 🔑 Key Files Explained

### Frontend (React)
- **App.js** - Main router setup, handles all routes
- **ATSChecker.js** - Handles PDF upload and ATS analysis
- **SkillGapAnalyzer.js** - Text input for gap analysis
- **RoadmapGenerator.js** - Career path generation
- **Navbar.js** - Navigation between pages
- **CircularScore.js** - Animated progress visualization
- **SkillChips.js** - Reusable skill badge component
- **FileUpload.js** - Drag-drop PDF upload component

### Backend (Node.js)
- **server.js** - Express server setup, middleware, routes
- **ats.controller.js** - Handles file upload and calls Python service
- **skillGap.controller.js** - Processes skill gap requests
- **roadmap.controller.js** - Processes roadmap requests
- **UserHistory.js** - MongoDB schema for storing analyses
- **upload.js** - Multer middleware for file handling

### ML Service (Python)
- **main.py** - FastAPI application with 3 endpoints
- **ats_checker.py** - PDF parsing and ATS scoring algorithm
- **skill_gap.py** - Skill extraction and gap analysis
- **roadmap_generator.py** - Predefined career roadmaps (6 paths)

### Configuration
- **.env** - Environment variables (MongoDB, Python service URL, port)
- **.gitignore** - Files to exclude from git
- **skills_database.json** - Master database of 150+ skills
- **package.json** (client) - React dependencies
- **package.json** (server) - Node.js dependencies
- **requirements.txt** - Python dependencies

---

## 📝 Documentation Files

| File | Purpose | Size |
|------|---------|------|
| README.md | Main overview and getting started | ~500 lines |
| INSTALLATION_GUIDE.md | Detailed step-by-step installation | ~600 lines |
| API_DOCUMENTATION.md | Complete API reference | ~400 lines |
| FEATURES.md | Feature specifications | ~700 lines |
| QUICK_START.md | 5-minute quick reference | ~250 lines |
| PROJECT_COMPLETION_SUMMARY.md | Project completion report | ~700 lines |
| DIRECTORY_STRUCTURE.md | This file | ~200 lines |

---

## 🗂️ Logical Organization

### By Functionality
```
ATS Checker:
- client/src/pages/ATSChecker.js
- client/src/components/FileUpload.js
- client/src/components/CircularScore.js
- server/routes/ats.routes.js
- server/controllers/ats.controller.js
- ml-service/ats_checker.py

Skill Gap Analyzer:
- client/src/pages/SkillGapAnalyzer.js
- client/src/components/SkillChips.js
- server/routes/skillGap.routes.js
- server/controllers/skillGap.controller.js
- ml-service/skill_gap.py

Roadmap Generator:
- client/src/pages/RoadmapGenerator.js
- server/routes/roadmap.routes.js
- server/controllers/roadmap.controller.js
- ml-service/roadmap_generator.py
```

### By Layer
```
Presentation (Frontend):
- client/src/pages/* (3 pages)
- client/src/components/* (4 components)
- client/public/index.html

Business Logic (Backend):
- server/controllers/* (3 controllers)
- server/routes/* (3 routes)
- ml-service/*.py (3 modules)

Data Layer:
- server/models/UserHistory.js
- server/middleware/upload.js
- skills_database.json

Configuration:
- Various .env, package.json, requirements.txt
```

---

## 📦 Deployment Structure

For deployment, maintain this structure:

```
Production/
├── Frontend Builds
│   └── build/ (from npm run build)
│
├── Backend Service
│   ├── Node.js app
│   ├── .env (production)
│   └── uploads/ (temp storage)
│
├── ML Service
│   ├── Python app
│   └── venv/ (virtual environment)
│
└── Database
    └── MongoDB (managed or self-hosted)
```

---

## 🔄 File Dependencies

### Frontend Dependencies
```
index.js
  └── App.js
      ├── ATSChecker.js
      │   ├── FileUpload.js
      │   ├── CircularScore.js
      │   └── SkillChips.js
      ├── SkillGapAnalyzer.js
      │   └── SkillChips.js
      └── RoadmapGenerator.js
```

### Backend Dependencies
```
server.js
  ├── routes/ats.routes.js
  │   └── controllers/ats.controller.js
  │       └── models/UserHistory.js
  ├── routes/skillGap.routes.js
  │   └── controllers/skillGap.controller.js
  │       └── models/UserHistory.js
  └── routes/roadmap.routes.js
      └── controllers/roadmap.controller.js
          └── models/UserHistory.js

middleware/upload.js
  (used by ats.controller.js)
```

### Python Service Dependencies
```
main.py
  ├── ats_checker.py
  │   ├── pdfplumber (for PDF parsing)
  │   └── scikit-learn (for TF-IDF)
  ├── skill_gap.py
  │   └── re module (regex)
  └── roadmap_generator.py
      └── json module
```

---

## 📊 File Size Reference (Approximate)

| File | Size | Type |
|------|------|------|
| app/pages/*.js | 300-400 lines | React |
| app/components/*.js | 100-200 lines | React |
| server/controllers/*.js | 80-120 lines | Node |
| ml-service/*.py | 300-500 lines | Python |
| skills_database.json | 100+ skills | JSON |
| documentation | 2,000+ lines | Markdown |

---

## 🎯 Usage Pattern

Typical file access pattern during development:

1. **First Time Setup**
   - Read: QUICK_START.md
   - Read: INSTALLATION_GUIDE.md
   - Modify: .env files

2. **Frontend Development**
   - Edit: client/src/pages/*.js
   - Edit: client/src/components/*.js
   - Reference: API_DOCUMENTATION.md

3. **Backend Development**
   - Edit: server/controllers/*.js
   - Edit: server/routes/*.js
   - Reference: API_DOCUMENTATION.md

4. **ML Service Development**
   - Edit: ml-service/*.py
   - Update: skills_database.json
   - Reference: FEATURES.md

5. **Deployment**
   - Read: README.md deployment section
   - Update: Production .env files
   - Run: Build scripts

---

## 🔐 File Permissions

### Executable Scripts
```bash
chmod +x start-all.sh      # macOS/Linux
# start-all.bat (Windows - auto executable)
```

### Sensitive Files
```
.env                       # Never commit
uploads/                   # Temporary files
node_modules/              # Generated
venv/                      # Generated
```

---

## 📚 How to Navigate

1. **Getting Started**: QUICK_START.md
2. **Setup Problems**: INSTALLATION_GUIDE.md
3. **API Issues**: API_DOCUMENTATION.md
4. **Feature Details**: FEATURES.md
5. **Code Overview**: README.md
6. **This File**: DIRECTORY_STRUCTURE.md

---

## ✅ File Checklist

Before deploying, verify all files exist:

### Frontend
- [ ] client/package.json
- [ ] client/public/index.html
- [ ] client/src/App.js
- [ ] client/src/pages/ (3 files)
- [ ] client/src/components/ (4 files)

### Backend
- [ ] server/package.json
- [ ] server/server.js
- [ ] server/routes/ (3 files)
- [ ] server/controllers/ (3 files)
- [ ] server/models/UserHistory.js
- [ ] server/.env

### ML Service
- [ ] ml-service/main.py
- [ ] ml-service/requirements.txt
- [ ] ml-service/ats_checker.py
- [ ] ml-service/skill_gap.py
- [ ] ml-service/roadmap_generator.py

### Documentation
- [ ] README.md
- [ ] INSTALLATION_GUIDE.md
- [ ] API_DOCUMENTATION.md
- [ ] FEATURES.md
- [ ] QUICK_START.md
- [ ] PROJECT_COMPLETION_SUMMARY.md

### Configuration
- [ ] skills_database.json
- [ ] .gitignore
- [ ] start-all.bat
- [ ] start-all.sh

---

This file serves as a complete reference for the project structure and file organization!
