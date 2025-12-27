# 🤖 Jarvis AI Voice Assistant

Advanced voice-controlled AI assistant with multiple voice commands, automation capabilities, and AI integration.

## ✨ Features

- 🎤 **Voice Recognition** - Multiple voice commands support
- 🔊 **Text-to-Speech** - Natural voice responses
- 🤖 **AI Integration** - OpenAI GPT integration
- 🌐 **Web Automation** - Open websites, search Google
- 📧 **Email & Messages** - Send emails and WhatsApp messages
- 🎵 **Media Control** - Play music, videos on YouTube
- 🌤️ **Weather Updates** - Real-time weather information
- 📰 **News Updates** - Latest news headlines
- 🔍 **Wikipedia Search** - Quick information lookup
- 💻 **System Control** - Open applications, take screenshots
- ⏰ **Reminders & Alarms** - Set reminders and alarms
- 🧮 **Calculations** - Perform mathematical calculations
- 🌍 **Translation** - Translate text between languages

## 📋 Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Internet connection
- OpenAI API key (optional, for AI features)

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/rahul700raj/jarvis-ai-voice-assistant.git
cd jarvis-ai-voice-assistant
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Keys

Create a `config.py` file:

```python
# OpenAI API Key (optional)
OPENAI_API_KEY = "your-openai-api-key"

# Weather API Key (optional - get from openweathermap.org)
WEATHER_API_KEY = "your-weather-api-key"

# News API Key (optional - get from newsapi.org)
NEWS_API_KEY = "your-news-api-key"
```

### Step 4: Run Jarvis

```bash
python jarvis.py
```

## 🎯 Voice Commands

### Basic Commands
- "Hello Jarvis" / "Hey Jarvis" - Activate assistant
- "What's your name?" - Introduction
- "What can you do?" - List capabilities
- "Exit" / "Quit" / "Goodbye" - Close assistant

### Web & Search
- "Open Google" - Opens Google
- "Open YouTube" - Opens YouTube
- "Search for [query]" - Google search
- "Play [song name] on YouTube" - Play music/video

### Information
- "What's the weather?" - Current weather
- "Tell me the news" - Latest headlines
- "Wikipedia [topic]" - Search Wikipedia
- "What time is it?" - Current time
- "What's the date?" - Current date

### AI Chat
- "Ask AI [question]" - Chat with AI
- "Tell me a joke" - Get a joke
- "Tell me a fact" - Random fact

### System Control
- "Open [application name]" - Open apps
- "Take a screenshot" - Capture screen
- "Increase volume" - Volume up
- "Decrease volume" - Volume down
- "Mute" / "Unmute" - Audio control

### Productivity
- "Set reminder [message]" - Set reminder
- "Calculate [expression]" - Math calculations
- "Translate [text] to [language]" - Translation
- "Send email" - Email composition

## 🛠️ Customization

### Add Custom Commands

Edit `jarvis.py` and add your commands in the `process_command()` function:

```python
def process_command(command):
    if "your custom command" in command:
        speak("Your custom response")
        # Your custom action
```

### Change Voice Settings

Modify voice properties in `jarvis.py`:

```python
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
```

### Select Different Voice

```python
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice
# engine.setProperty('voice', voices[1].id)  # Female voice
```

## 📁 Project Structure

```
jarvis-ai-voice-assistant/
├── jarvis.py              # Main application
├── config.py              # Configuration file
├── requirements.txt       # Dependencies
├── modules/
│   ├── speech.py         # Speech recognition & TTS
│   ├── ai_chat.py        # AI integration
│   ├── web_automation.py # Web tasks
│   ├── system_control.py # System operations
│   └── utilities.py      # Helper functions
├── data/
│   └── commands.json     # Command mappings
└── README.md             # Documentation
```

## 🔧 Troubleshooting

### Microphone Not Working
```bash
# Test microphone
python -m speech_recognition
```

### PyAudio Installation Issues (Windows)
```bash
pip install pipwin
pipwin install pyaudio
```

### PyAudio Installation Issues (Linux)
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

### PyAudio Installation Issues (Mac)
```bash
brew install portaudio
pip install pyaudio
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI for GPT integration
- Google for Speech Recognition
- pyttsx3 for Text-to-Speech

## 📞 Support

For issues and questions, please open an issue on GitHub.

---

**Made with ❤️ by Rahul Mishra**
