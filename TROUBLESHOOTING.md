# TROUBLESHOOTING GUIDE

## Issue: "Error Analyzing Resume"

### Common Causes & Solutions

---

## 1. PDF File Format Issue

**Problem:** The resume file is not in PDF format or is corrupted.

**Solutions:**
- ✅ Ensure the file is a valid PDF (ends in `.pdf`)
- ✅ Try a different PDF file
- ✅ If the file was converted from Word, re-save it as PDF
- ✅ Check file size - make sure it's not empty or extremely large (>10MB)

**How to test:**
```bash
# Try uploading a sample PDF
# The app should accept any valid PDF file
```

---

## 2. Backend Not Connected to ML Service

**Problem:** The backend (port 5000) cannot reach the ML service (port 8000).

**Check:**
1. Verify ML Service is running:
   ```powershell
   Get-NetTCPConnection -LocalPort 8000 -State Listen
   ```
   Should show: `Listening on 0.0.0.0:8000`

2. If not running, restart it:
   ```powershell
   cd "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\ml-service"
   python main.py
   ```

---

## 3. Skills Database Not Found

**Problem:** The ATS analyzer cannot find the skills database.

**Check:**
- File `skills_database.json` must exist in:
  - `c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\`

**Solution:**
```bash
# Verify the file exists:
ls -la ../skills_database.json

# If missing, copy from backup or recreate
```

---

## 4. Port Already in Use

**Problem:** Services fail to start because ports are already in use.

**Solution:**
```powershell
# Kill all processes on port 8000 (ML Service)
taskkill /F /IM python.exe

# Kill all processes on port 5000 (Backend)
taskkill /F /IM node.exe

# Wait 3 seconds
Start-Sleep -Seconds 3

# Restart services
```

---

## 5. File Upload Permissions

**Problem:** The server cannot read/write uploaded files.

**Check:**
1. Upload directory must exist and be writable:
   ```bash
   c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\server\uploads\
   ```

2. Create if missing:
   ```powershell
   New-Item -ItemType Directory -Path "server\uploads" -Force
   ```

---

## 6. CORS Error

**Problem:** Browser shows CORS error when sending file to backend.

**This is automatically configured, but if you see it:**
1. Check that backend has CORS enabled:
   ```javascript
   // In server/server.js - line 19-22
   app.use(cors({
     origin: 'http://localhost:3000',
     credentials: true
   }));
   ```

2. Verify backend is on port 5000

---

## 7. Network/Firewall Issue

**Problem:** Browser cannot connect to localhost:5000 or localhost:8000

**Solutions:**
1. Add Windows Firewall exceptions:
   ```powershell
   # For Node.js
   netsh advfirewall firewall add rule name="Node.js Port 5000" dir=in action=allow protocol=tcp localport=5000

   # For Python
   netsh advfirewall firewall add rule name="Python Port 8000" dir=in action=allow protocol=tcp localport=8000

   # For Frontend
   netsh advfirewall firewall add rule name="Frontend Port 3000" dir=in action=allow protocol=tcp localport=3000
   ```

---

## Complete Service Restart (Nuclear Option)

If everything fails, do a complete restart:

```powershell
# 1. Kill all services
taskkill /F /IM node.exe 2>$null
taskkill /F /IM python.exe 2>$null
Start-Sleep -Seconds 3

# 2. Start Backend
cd "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\server"
node server.js &

# 3. Start ML Service
cd "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\ml-service"
python main.py &

# 4. Start Frontend
cd "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\client\build"
python -m http.server 3000 &

# 5. Wait 10 seconds
Start-Sleep -Seconds 10

# 6. Verify all services
Write-Host "Backend:" (Get-NetTCPConnection -LocalPort 5000 -State Listen -EA SilentlyContinue)
Write-Host "ML Service:" (Get-NetTCPConnection -LocalPort 8000 -State Listen -EA SilentlyContinue)
Write-Host "Frontend:" (Get-NetTCPConnection -LocalPort 3000 -State Listen -EA SilentlyContinue)

# 7. Open browser
Start http://localhost:3000
```

---

## Debugging: Check ML Service Logs

When you analyze a resume, check the ML service terminal for debug output:

```
DEBUG: File received: resume.pdf, content_type: application/pdf
DEBUG: File size: 15234 bytes
DEBUG: Analysis result: {...}
```

If you see ERROR lines, note them down.

---

## Debugging: Check Backend Logs

The backend should show requests being processed:

```
POST /api/ats/upload
File received from frontend
Calling ML service at http://localhost:8000/ats
Response from ML service received
Saving to MongoDB
Response sent to frontend
```

---

## Test Endpoints Directly

Use PowerShell to test endpoints:

```powershell
# Test backend health
curl http://localhost:5000/api/health
# Expected: {"status":"Server is running"}

# Test ML service health
curl http://localhost:8000/health
# Expected: {"status":"ML service is running"}

# Test ATS endpoint with a test PDF (requires file)
$filePath = "C:\path\to\resume.pdf"
$uri = "http://localhost:8000/ats"
$form = @{
    file = Get-Item -Path $filePath
}
Invoke-RestMethod -Uri $uri -Method Post -Form $form
```

---

## Common Error Messages & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ERR_CONNECTION_REFUSED` | Service not running | Restart service |
| `404 Not Found` | Wrong endpoint path | Check API URL in code |
| `CORS error` | Backend CORS settings | Check server.js line 19 |
| `File must be PDF` | Wrong file format | Upload a valid PDF |
| `Error analyzing resume` | ML service crashed | Restart ML service |
| `MongoDB connection error` | DB not running | Start MongoDB service |
| `Port already in use` | Service already running | Kill old process first |

---

## Quick Diagnostic Check

Run this PowerShell script to diagnose issues:

```powershell
Write-Host "=== DIAGNOSTIC CHECK ===" -ForegroundColor Green
Write-Host ""

# Check ports
Write-Host "Port Status:" -ForegroundColor Cyan
$ports = @(5000, 8000, 3000)
foreach ($port in $ports) {
    $check = Get-NetTCPConnection -LocalPort $port -State Listen -EA SilentlyContinue
    if ($check) {
        Write-Host "✅ Port $port: LISTENING" -ForegroundColor Green
    } else {
        Write-Host "❌ Port $port: NOT LISTENING" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "File Locations:" -ForegroundColor Cyan

# Check critical files
$files = @(
    "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\skills_database.json",
    "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\server\server.js",
    "c:\Users\seela\OneDrive\Documents\All_Coding\AI_Career\ai-career-assistant\ml-service\main.py"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "✅ $file" -ForegroundColor Green
    } else {
        Write-Host "❌ MISSING: $file" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Recommendation:" -ForegroundColor Yellow
Write-Host "1. Verify all ports are LISTENING"
Write-Host "2. Verify all files exist"
Write-Host "3. Try uploading a different PDF file"
Write-Host "4. Check browser console for JavaScript errors (F12)"
```

---

## Getting Help

If issues persist:

1. **Check browser console** (F12) for JavaScript errors
2. **Check terminal logs** for error messages
3. **Restart all services** using the Nuclear Option above
4. **Try a different PDF file** to rule out file issues
5. **Review API_DOCUMENTATION.md** for endpoint details
6. **Check server/.env** for correct configuration

---

## Success Indicators

✅ When everything works, you should see:

1. **Browser:** App loads at http://localhost:3000
2. **Backend terminal:** "✅ MongoDB connected successfully"
3. **ML Service terminal:** "Application startup complete"
4. **Frontend terminal:** "Serving HTTP on :: port 3000"
5. **ATS Analyzer:** Shows score 0-100 after uploading PDF

---

**Still having issues?** Try the complete restart above and upload a fresh PDF file.
