# 📥 Detailed Installation Guide

## Step-by-Step Installation Process

### Step 1: Install Python

1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Verify installation:
   ```bash
   python --version
   ```

### Step 2: Clone Repository

```bash
# Using HTTPS
git clone https://github.com/rahul700raj/jarvis-ai-voice-assistant.git

# OR using SSH
git clone git@github.com:rahul700raj/jarvis-ai-voice-assistant.git

# Navigate to directory
cd jarvis-ai-voice-assistant
```

### Step 3: Install Dependencies

#### Windows

```bash
# Install PyAudio (required for microphone)
pip install pipwin
pipwin install pyaudio

# Install other dependencies
pip install -r requirements.txt
```

#### Linux (Ubuntu/Debian)

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3-pyaudio portaudio19-dev espeak

# Install Python packages
pip install -r requirements.txt
```

#### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install portaudio
pip install -r requirements.txt
```

### Step 4: Configure API Keys (Optional)

1. **OpenAI API Key** (for AI chat):
   - Go to [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create account and generate API key
   - Add to `config.py`

2. **Weather API Key**:
   - Go to [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up and get free API key
   - Add to `config.py`

3. **News API Key**:
   - Go to [NewsAPI](https://newsapi.org/)
   - Register and get API key
   - Add to `config.py`

### Step 5: Test Microphone

```bash
# Test if microphone is working
python -m speech_recognition
```

Follow the prompts to test your microphone.

### Step 6: Run Jarvis

```bash
python jarvis.py
```

## 🔧 Troubleshooting

### Issue: PyAudio Installation Failed

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

### Issue: Microphone Not Detected

1. Check microphone permissions in system settings
2. Test with:
   ```bash
   python -m speech_recognition
   ```
3. Try different microphone in code:
   ```python
   # List available microphones
   import speech_recognition as sr
   print(sr.Microphone.list_microphone_names())
   ```

### Issue: Speech Recognition Not Working

1. Check internet connection (Google Speech API requires internet)
2. Verify microphone is working
3. Try adjusting `recognizer.pause_threshold` in code

### Issue: Text-to-Speech Not Working

**Linux:**
```bash
sudo apt-get install espeak
```

**Windows:** Should work by default

**macOS:** Should work by default

### Issue: Import Errors

```bash
# Reinstall all dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

## 🎯 Quick Start Commands

After installation, try these commands:

1. "Hello Jarvis"
2. "What time is it?"
3. "Open Google"
4. "Play music on YouTube"
5. "Tell me a joke"
6. "What's the weather?"

## 📱 Running on Startup (Optional)

### Windows

1. Press `Win + R`
2. Type `shell:startup`
3. Create shortcut to `jarvis.py`

### Linux

Add to `~/.bashrc`:
```bash
alias jarvis='cd /path/to/jarvis-ai-voice-assistant && python jarvis.py'
```

### macOS

Create Launch Agent or add to login items.

## 🆘 Need Help?

- Check [README.md](README.md) for features
- Open an issue on GitHub
- Check existing issues for solutions

---

**Installation complete! Say "Hello Jarvis" to start! 🚀**
