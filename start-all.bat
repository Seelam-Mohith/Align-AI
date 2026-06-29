@REM start-all.bat - Windows batch script to start all services
@echo off
echo.
echo ========================================
echo  AI Career Assistant - Starting Services
echo ========================================
echo.

REM Get the directory of this script
set SCRIPT_DIR=%~dp0

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

for /f "delims=" %%i in ('node --version') do set NODE_VERSION=%%i
echo [OK] Node.js found: %NODE_VERSION%
echo [OK] Python found

echo.
echo Starting Backend (Express.js on port 5000)...
start cmd /k "cd /d "%SCRIPT_DIR%server" && if not exist node_modules npm install --silent && npm run dev"
timeout /t 3 /nobreak

echo Starting ML Service (FastAPI on port 8000)...
if exist "%SCRIPT_DIR%ml-service\.venv\Scripts\activate" (
    start cmd /k "cd /d "%SCRIPT_DIR%ml-service" && call .venv\Scripts\activate && python main.py"
) else (
    start cmd /k "cd /d "%SCRIPT_DIR%ml-service" && python main.py"
)
timeout /t 3 /nobreak

echo Starting Frontend (React on port 3000)...
start cmd /k "cd /d "%SCRIPT_DIR%client" && if not exist node_modules npm install --silent && npm start"

echo.
echo ========================================
echo  Services Starting...
echo ========================================
echo.
echo Frontend:   http://localhost:3000
echo Backend:    http://localhost:5000
echo ML Service: http://localhost:8000
echo.
echo All services should be ready in 30-60 seconds
echo Press Ctrl+C in any window to stop that service
echo.
pause
