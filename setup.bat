@echo off
REM Jarvis AI Voice Assistant - Quick Setup Script for Windows
REM This script automates the installation process

echo ========================================
echo 🤖 Jarvis AI Voice Assistant - Quick Setup
echo ========================================
echo.

REM Check Python installation
echo 📋 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% found
echo.

REM Check pip installation
echo 📋 Checking pip installation...
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not installed
    echo Installing pip...
    python -m ensurepip --upgrade
)
echo ✅ pip is installed
echo.

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install pipwin for PyAudio
echo 📦 Installing pipwin...
pip install pipwin
echo.

REM Install PyAudio using pipwin
echo 📦 Installing PyAudio...
pipwin install pyaudio
echo.

REM Install other dependencies
echo 📦 Installing other dependencies...
pip install -r requirements.txt
echo ✅ All dependencies installed
echo.

REM Create config file backup
if exist config.py (
    echo 📝 Config file exists
) else (
    echo 📝 Config file ready for editing
)
echo.

REM Test microphone
echo 🎤 Testing microphone...
echo Please say something when prompted...
python -m speech_recognition
echo.

REM Final instructions
echo ========================================
echo ✅ Installation Complete!
echo ========================================
echo.
echo 📝 Next Steps:
echo 1. Edit config.py and add your API keys (optional)
echo 2. Run: python jarvis.py
echo 3. Say 'Hello Jarvis' to start!
echo.
echo 📚 Documentation:
echo - README.md - Full documentation
echo - INSTALLATION.md - Detailed installation guide
echo - COMMANDS.md - All voice commands
echo.
echo 🚀 To start Jarvis now, run:
echo    python jarvis.py
echo.
pause
