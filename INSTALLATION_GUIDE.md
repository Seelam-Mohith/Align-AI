# INSTALLATION_GUIDE.md - Detailed Installation Instructions

## 🖥️ System Requirements

- **OS**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: Minimum 2GB free space
- **Node.js**: v16.0.0 or higher
- **Python**: v3.8 or higher
- **MongoDB**: v4.4 or higher (local or Atlas)

## Step-by-Step Installation

### Step 1: Clone or Download Project

```bash
# Navigate to your projects folder
cd /path/to/projects

# Copy the ai-career-assistant folder here
# Make sure you have all folders: client/, server/, ml-service/
```

### Step 2: Install & Run Node.js Backend

```bash
# Navigate to server directory
cd ai-career-assistant/server

# Install dependencies
npm install

# Check if installation was successful
npm list

# Start the server in development mode
npm run dev

# Expected output:
# ✅ MongoDB connected successfully
# 🚀 Server running on http://localhost:5000
```

**Verify Backend:**
```bash
# In another terminal, test the health endpoint
curl http://localhost:5000/api/health
# Expected: {"status":"Server is running"}
```

### Step 3: Install & Run Python ML Service

```bash
# Navigate to ml-service directory
cd ../ml-service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list

# Download spaCy model (optional but recommended for advanced NLP)
python -m spacy download en_core_web_sm

# Start FastAPI server
python main.py

# Expected output:
# INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Verify ML Service:**
```bash
# In another terminal
curl http://localhost:8000/health
# Expected: {"status":"ML service is running"}
```

### Step 4: Install & Run React Frontend

```bash
# Navigate to client directory
cd ../client

# Install dependencies
npm install

# Start development server
npm start

# Expected output:
# Compiled successfully!
# You can now view ai-career-assistant-client in the browser.
# Local:            http://localhost:3000
```

The browser should automatically open to `http://localhost:3000`

### Step 5: Verify All Services

Create a checklist:

```
✓ Backend running on http://localhost:5000
✓ ML Service running on http://localhost:8000
✓ Frontend running on http://localhost:3000
✓ MongoDB connected
✓ Can access http://localhost:3000/ats-checker
```

## 🗄️ MongoDB Setup

### Option A: MongoDB Atlas (Cloud - Recommended)

1. Visit [mongodb.com](https://mongodb.com)
2. Sign up for free account
3. Create a new project
4. Build a cluster
5. Create a database user
6. Get connection string
7. Update `server/.env`:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai-career-assistant
   ```

### Option B: Local MongoDB

#### Windows:
```bash
# Download installer from mongodb.com
# Run installer and follow prompts
# Verify installation
mongod --version

# Start MongoDB service
mongod

# In another terminal, connect to database
mongosh
```

#### macOS (Homebrew):
```bash
# Install MongoDB
brew tap mongodb/brew
brew install mongodb-community

# Start MongoDB
brew services start mongodb-community

# Connect to database
mongosh
```

#### Linux (Ubuntu):
```bash
# Install MongoDB
sudo apt-get update
sudo apt-get install mongodb

# Start MongoDB
sudo systemctl start mongodb

# Verify
mongosh
```

## 🔧 Environment Configuration

### Create/Verify .env Files

**server/.env**
```
MONGODB_URI=mongodb://localhost:27017/ai-career-assistant
PYTHON_SERVICE_URL=http://localhost:8000
PORT=5000
NODE_ENV=development
```

**client/.env** (optional for frontend)
```
REACT_APP_API_URL=http://localhost:5000/api
```

## 📦 Dependency Version Reference

### Node.js Dependencies
```json
{
  "express": "^4.18.2",
  "mongoose": "^7.0.0",
  "multer": "^1.4.5",
  "axios": "^1.3.0",
  "cors": "^2.8.5",
  "dotenv": "^16.0.3"
}
```

### Python Dependencies
```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
pdfplumber==0.10.3
scikit-learn==1.3.2
numpy==1.24.3
spacy==3.7.2
python-multipart==0.0.6
```

### React Dependencies
```json
{
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "react-router-dom": "^6.8.0",
  "axios": "^1.3.0",
  "recharts": "^2.5.0",
  "tailwindcss": "^3.2.0"
}
```

## ⚠️ Common Installation Issues & Solutions

### Issue: `npm ERR! code EACCES`
**Solution:**
```bash
# Fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

### Issue: `ModuleNotFoundError: No module named 'pdfplumber'`
**Solution:**
```bash
# Ensure virtual environment is activated
python -m pip install --upgrade pip
pip install pdfplumber
```

### Issue: `Port 3000/5000/8000 already in use`
**Solution:**
```bash
# Windows - Find and kill process
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# macOS/Linux - Find and kill process
lsof -i :3000
kill -9 <PID>

# Or use different ports
# Edit .env and package.json to use different ports
```

### Issue: `MongoDB connection refused`
**Solution:**
```bash
# Check if MongoDB is running
# Windows: Check Services
# macOS: brew services list
# Linux: sudo systemctl status mongodb

# Start MongoDB
mongod  # or brew services start mongodb-community
```

### Issue: `CORS error in browser`
**Solution:**
1. Check CORS middleware in `server/server.js`
2. Verify frontend URL is whitelisted
3. Check browser console for specific error
4. Clear browser cache

### Issue: `Out of memory when processing large PDFs`
**Solution:**
```python
# In ats_checker.py, limit file size:
# Current limit: 10MB in multer
# Increase RAM or process files in chunks
```

## 🧪 Test Installation

### Test 1: Backend API
```bash
curl -X GET http://localhost:5000/api/health
# Expected: {"status":"Server is running"}
```

### Test 2: ML Service
```bash
curl -X GET http://localhost:8000/health
# Expected: {"status":"ML service is running"}
```

### Test 3: MongoDB
```bash
# In MongoDB client
show dbs
use ai-career-assistant
show collections
```

### Test 4: Full Flow (Manual)

1. Open http://localhost:3000
2. Go to ATS Checker page
3. Create a sample PDF resume or use existing PDF
4. Upload and click "Analyze Resume"
5. Observe score and recommendations

## 🔄 Restart Services

### Quick Restart Script

**Windows (restart.bat)**
```batch
@echo off
start cmd /k "cd server && npm run dev"
start cmd /k "cd ml-service && python main.py"
start cmd /k "cd client && npm start"
```

**macOS/Linux (restart.sh)**
```bash
#!/bin/bash
cd server && npm run dev &
cd ml-service && python main.py &
cd client && npm start &
```

Make executable: `chmod +x restart.sh`

## 📊 Verify Installation Checklist

```
Frontend (React)
  ✓ npm install completed
  ✓ node_modules exists
  ✓ npm start runs without errors
  ✓ App opens on http://localhost:3000

Backend (Node.js)
  ✓ npm install completed
  ✓ node_modules exists
  ✓ npm start runs without errors
  ✓ Server listens on http://localhost:5000
  ✓ Can hit /api/health endpoint

ML Service (Python)
  ✓ Virtual environment created
  ✓ pip install -r requirements.txt completed
  ✓ python main.py runs without errors
  ✓ Service listens on http://localhost:8000
  ✓ Can hit /health endpoint

Database (MongoDB)
  ✓ MongoDB running
  ✓ Connection string configured in .env
  ✓ Can connect using mongosh
  ✓ Can create/query database

Integration
  ✓ Frontend can communicate with backend
  ✓ Backend can communicate with ML service
  ✓ Can upload file and get ATS score
  ✓ Can analyze skill gap
  ✓ Can generate roadmap
  ✓ Data saved to MongoDB
```

## 🎯 Next Steps

After successful installation:

1. **Explore the UI**: Navigate through all three tools
2. **Test with sample data**: Use the features
3. **Check MongoDB**: Verify data is being saved
4. **Review code**: Understand the architecture
5. **Customize**: Modify skills database and roadmaps
6. **Deploy**: Follow deployment guide for production

## 📞 Getting Help

If you encounter issues:

1. Check the README.md for general information
2. Review error messages carefully
3. Check service logs:
   - Frontend: Browser console (F12)
   - Backend: Terminal where npm start is running
   - ML Service: Terminal where python main.py is running
4. Verify all services are running
5. Check network connectivity

---

**Installation complete! Ready to use AI Career Assistant! 🚀**
