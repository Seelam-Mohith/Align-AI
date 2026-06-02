# QUICK_START.md - 5-Minute Quick Start Guide

## ⚡ Get Running in 5 Minutes

### Prerequisites Check
```bash
node --version    # Should be v16+
npm --version     # Should be v8+
python --version  # Should be v3.8+
mongod --version  # Should be v4.4+
```

### Option 1: Automated Start (Windows)
```bash
cd ai-career-assistant
start-all.bat
```

### Option 2: Automated Start (macOS/Linux)
```bash
cd ai-career-assistant
chmod +x start-all.sh
./start-all.sh
```

### Option 3: Manual Start (All Platforms)

**Terminal 1: Backend**
```bash
cd server
npm install
npm run dev
# Wait for: ✅ MongoDB connected successfully
```

**Terminal 2: ML Service**
```bash
cd ml-service
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
# Wait for: INFO: Uvicorn running on http://0.0.0.0:8000
```

**Terminal 3: Frontend**
```bash
cd client
npm install
npm start
# Waits for: Compiled successfully!
```

---

## ✅ Verify Everything Works

1. **Backend Health**
   ```bash
   curl http://localhost:5000/api/health
   # Response: {"status":"Server is running"}
   ```

2. **ML Service Health**
   ```bash
   curl http://localhost:8000/health
   # Response: {"status":"ML service is running"}
   ```

3. **Frontend Running**
   - Browser opens to: http://localhost:3000
   - Navbar shows all 3 tools

---

## 🧪 Quick Feature Test

### Test 1: ATS Checker
1. Go to http://localhost:3000/ats-checker
2. Create a sample PDF or use existing resume
3. Click upload zone or drag-drop PDF
4. Click "Analyze Resume"
5. See score and recommendations

### Test 2: Skill Gap Analyzer
1. Go to http://localhost:3000/skill-gap
2. Paste sample resume text:
   ```
   I have 5 years experience with Python, JavaScript, React, Node.js, 
   MongoDB, Express, Git, Docker, and AWS. Strong in full-stack development
   and cloud architecture.
   ```
3. Paste sample job description:
   ```
   Seeking Senior Backend Developer with expertise in Python, FastAPI, 
   PostgreSQL, Docker, Kubernetes, AWS, and microservices architecture.
   Must have REST API design experience.
   ```
4. Click "Analyze Gap"
5. See overlaps and recommendations

### Test 3: Roadmap Generator
1. Go to http://localhost:3000/roadmap
2. Click quick button "Web Developer" or type custom goal
3. Click "Generate Roadmap"
4. Click sections to expand
5. See learning path with durations

---

## 🛠️ Common Commands

### Install All Dependencies
```bash
cd server && npm install && cd ../ml-service && pip install -r requirements.txt && cd ../client && npm install
```

### Clean Start
```bash
# Kill all node processes
pkill -f node

# Remove node_modules
rm -rf server/node_modules client/node_modules

# Reinstall
npm install --prefix server
npm install --prefix client
```

### Check Service Status
```bash
curl http://localhost:5000/api/health
curl http://localhost:8000/health
```

### View Logs
- **Frontend**: Browser console (F12)
- **Backend**: Terminal running npm run dev
- **ML Service**: Terminal running python main.py

---

## 📁 Key Files to Know

```
ai-career-assistant/
├── README.md                 ← Full documentation
├── INSTALLATION_GUIDE.md     ← Detailed setup
├── API_DOCUMENTATION.md      ← API endpoints
├── FEATURES.md               ← Feature list
├── QUICK_START.md           ← This file
│
├── client/src/pages/         ← React pages
├── server/controllers/       ← API controllers
└── ml-service/              ← Python ML code
```

---

## 🚨 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Port 5000 in use" | Kill process: `lsof -i :5000 \| kill` |
| "Cannot find module" | Run `npm install` in that folder |
| "ModuleNotFoundError" | Activate venv: `source venv/bin/activate` |
| "MongoDB connection error" | Start MongoDB: `mongod` |
| "CORS error" | Check backend is running on :5000 |
| "Blank page" | Check browser console (F12) for errors |

---

## 📚 Next Steps

1. **Explore Code**: Read through main.py, server.js, App.js
2. **Test Workflows**: Try all 3 features
3. **Check MongoDB**: View saved data with `mongosh`
4. **Review API**: Check API_DOCUMENTATION.md
5. **Customize**: Edit skills_database.json, roadmaps

---

## 💾 MongoDB Quick Commands

```bash
# Start MongoDB
mongod

# Connect (new terminal)
mongosh

# View all databases
show dbs

# Use app database
use ai-career-assistant

# View collections
show collections

# View all history
db.userhistories.find()

# View ATS analyses only
db.userhistories.find({analysisType: "ats"})

# Count entries
db.userhistories.countDocuments()

# Delete all history (CAREFUL!)
db.userhistories.deleteMany({})
```

---

## 🎯 Architecture at a Glance

```
User Browser (http://localhost:3000)
    ↓
React App (Components, Pages)
    ↓
Express Backend (http://localhost:5000)
    ↓
Python FastAPI (http://localhost:8000)
    ↓
MongoDB (Port 27017)
```

---

## 📞 Need Help?

1. Check INSTALLATION_GUIDE.md for detailed steps
2. Check API_DOCUMENTATION.md for endpoint details
3. Check FEATURES.md for feature specifications
4. Review README.md for comprehensive info
5. Check browser console (F12) for error messages
6. Check terminal logs for backend/ML service errors

---

## 🚀 Deploy to Production

### Deploy Backend (Heroku)
```bash
heroku login
heroku create your-app
git push heroku main
```

### Deploy Frontend (Vercel)
```bash
npm install -g vercel
vercel
```

### Deploy ML Service (Render/Heroku)
```bash
heroku create your-ml-app
git push heroku main
```

---

**Ready to go! Happy coding! 🎉**

For complete setup details, see INSTALLATION_GUIDE.md
For API details, see API_DOCUMENTATION.md
For feature details, see FEATURES.md
