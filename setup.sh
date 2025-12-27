#!/bin/bash

# Jarvis AI Voice Assistant - Quick Setup Script
# This script automates the installation process

echo "🤖 Jarvis AI Voice Assistant - Quick Setup"
echo "=========================================="
echo ""

# Check Python installation
echo "📋 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Check pip installation
echo "📋 Checking pip installation..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Installing pip..."
    python3 -m ensurepip --upgrade
fi
echo "✅ pip is installed"
echo ""

# Detect OS
echo "📋 Detecting operating system..."
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    CYGWIN*)    MACHINE=Windows;;
    MINGW*)     MACHINE=Windows;;
    *)          MACHINE="UNKNOWN:${OS}"
esac
echo "✅ Detected: $MACHINE"
echo ""

# Install system dependencies based on OS
echo "📦 Installing system dependencies..."
if [ "$MACHINE" = "Linux" ]; then
    echo "Installing Linux dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3-pyaudio portaudio19-dev espeak
elif [ "$MACHINE" = "Mac" ]; then
    echo "Installing macOS dependencies..."
    if ! command -v brew &> /dev/null; then
        echo "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install portaudio
fi
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created"
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [ "$MACHINE" = "Windows" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip
echo ""

# Install Python dependencies
echo "📦 Installing Python dependencies..."
if [ "$MACHINE" = "Windows" ]; then
    pip install pipwin
    pipwin install pyaudio
fi
pip install -r requirements.txt
echo "✅ All dependencies installed"
echo ""

# Create config file if it doesn't exist
if [ ! -f "config.py" ]; then
    echo "📝 Creating config.py file..."
    cp config.py config.py.backup 2>/dev/null || true
    echo "✅ Config file ready"
fi
echo ""

# Test microphone
echo "🎤 Testing microphone..."
echo "Please say something when prompted..."
python3 -m speech_recognition
echo ""

# Final instructions
echo "=========================================="
echo "✅ Installation Complete!"
echo "=========================================="
echo ""
echo "📝 Next Steps:"
echo "1. Edit config.py and add your API keys (optional)"
echo "2. Run: python jarvis.py"
echo "3. Say 'Hello Jarvis' to start!"
echo ""
echo "📚 Documentation:"
echo "- README.md - Full documentation"
echo "- INSTALLATION.md - Detailed installation guide"
echo "- COMMANDS.md - All voice commands"
echo ""
echo "🚀 To start Jarvis now, run:"
echo "   python jarvis.py"
echo ""
