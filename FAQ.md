# ❓ Frequently Asked Questions (FAQ)

## General Questions

### Q: What is Jarvis AI Voice Assistant?
**A:** Jarvis is an advanced voice-controlled AI assistant that can perform various tasks like web searches, playing music, providing weather updates, news, and much more through voice commands.

### Q: Do I need an internet connection?
**A:** Yes, internet is required for:
- Speech recognition (Google Speech API)
- Web searches and browsing
- YouTube playback
- Weather and news updates
- AI chat features

### Q: Is it free to use?
**A:** Yes, the core features are completely free. Some optional features require API keys:
- OpenAI API (paid) - for AI chat
- Weather API (free tier available)
- News API (free tier available)

### Q: Which operating systems are supported?
**A:** Jarvis works on:
- ✅ Windows 10/11
- ✅ macOS (10.14+)
- ✅ Linux (Ubuntu, Debian, Fedora)

### Q: What Python version do I need?
**A:** Python 3.8 or higher is required.

## Installation Questions

### Q: How do I install PyAudio on Windows?
**A:** Use pipwin:
```bash
pip install pipwin
pipwin install pyaudio
```

### Q: Installation fails on Linux, what should I do?
**A:** Install system dependencies first:
```bash
sudo apt-get update
sudo apt-get install python3-pyaudio portaudio19-dev espeak
pip install -r requirements.txt
```

### Q: Can I use Jarvis without API keys?
**A:** Yes! Most features work without API keys. You only need API keys for:
- AI chat (OpenAI)
- Weather updates (OpenWeatherMap)
- News headlines (NewsAPI)

### Q: Where do I get API keys?
**A:** 
- **OpenAI:** https://platform.openai.com/api-keys
- **Weather:** https://openweathermap.org/api
- **News:** https://newsapi.org/

## Usage Questions

### Q: How do I activate Jarvis?
**A:** Simply say "Hello Jarvis" or "Hey Jarvis" after running the program.

### Q: Jarvis doesn't understand my commands, why?
**A:** Try these solutions:
1. Speak clearly and at normal pace
2. Reduce background noise
3. Check microphone is working
4. Ensure internet connection is stable
5. Try rephrasing the command

### Q: Can I change Jarvis's voice?
**A:** Yes! Edit `jarvis.py`:
```python
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to female voice
```

### Q: How do I change speech speed?
**A:** Edit `jarvis.py`:
```python
engine.setProperty('rate', 150)  # Increase or decrease value
```

### Q: Can I add custom commands?
**A:** Yes! Edit the `process_command()` function in `jarvis.py`:
```python
elif 'your command' in command:
    speak("Your response")
    # Your code here
```

## Troubleshooting Questions

### Q: Microphone not detected, what should I do?
**A:** 
1. Check system microphone permissions
2. Test with: `python -m speech_recognition`
3. List available microphones:
```python
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
```

### Q: Speech recognition always returns "none"?
**A:** 
1. Check internet connection
2. Verify microphone is working
3. Speak louder and clearer
4. Reduce background noise
5. Try adjusting `recognizer.pause_threshold` in code

### Q: Text-to-speech not working?
**A:** 
- **Linux:** Install espeak: `sudo apt-get install espeak`
- **Windows/Mac:** Should work by default, try reinstalling pyttsx3

### Q: "Module not found" error?
**A:** Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Q: PyAudio installation fails?
**A:** See platform-specific solutions in INSTALLATION.md

## Feature Questions

### Q: Can Jarvis send emails?
**A:** The basic framework is there, but you need to implement SMTP configuration for your email provider.

### Q: Can Jarvis control smart home devices?
**A:** Not by default, but you can extend it by adding smart home API integrations.

### Q: Can I use Jarvis offline?
**A:** Limited functionality. Speech recognition requires internet, but you can modify the code to use offline alternatives like:
- CMU Sphinx for offline speech recognition
- Offline TTS engines

### Q: How do I make Jarvis start on system boot?
**A:** 
- **Windows:** Add shortcut to Startup folder
- **Linux:** Add to `~/.bashrc` or create systemd service
- **Mac:** Add to Login Items

### Q: Can multiple people use Jarvis?
**A:** Yes, but it doesn't have user authentication. Anyone can give commands.

### Q: Does Jarvis learn from my commands?
**A:** No, it doesn't have machine learning capabilities by default. You'd need to implement that separately.

## Performance Questions

### Q: Jarvis is slow to respond?
**A:** 
1. Check internet speed
2. Reduce `recognizer.pause_threshold`
3. Use faster speech recognition service
4. Optimize code for your use case

### Q: High CPU usage?
**A:** 
1. Close unnecessary applications
2. Reduce speech recognition sensitivity
3. Optimize continuous listening loop

### Q: Can I run Jarvis on Raspberry Pi?
**A:** Yes! But performance may vary. Use Raspberry Pi 4 or newer for best results.

## Customization Questions

### Q: How do I add more websites to open?
**A:** Add to `process_command()`:
```python
elif 'open facebook' in command:
    webbrowser.open("https://www.facebook.com")
```

### Q: Can I change the wake word from "Jarvis"?
**A:** Yes! Modify the command detection in `process_command()` function.

### Q: How do I add more applications to open?
**A:** Add to the `apps` dictionary in `open_application()` function.

### Q: Can I integrate with other AI models?
**A:** Yes! You can replace OpenAI with other models like:
- Google Gemini
- Anthropic Claude
- Local models (Ollama, LM Studio)

## Security Questions

### Q: Is my data safe?
**A:** 
- Voice data is sent to Google for speech recognition
- API keys should be kept private (never commit to GitHub)
- No data is stored locally by default

### Q: Should I share my API keys?
**A:** **NO!** Never share or commit API keys to public repositories.

### Q: How do I protect my API keys?
**A:** 
1. Use `.env` files
2. Add `config.py` to `.gitignore`
3. Use environment variables
4. Rotate keys regularly

## Advanced Questions

### Q: Can I deploy Jarvis as a web service?
**A:** Yes, but you'd need to:
1. Implement web interface
2. Handle multiple concurrent users
3. Use WebRTC for audio streaming
4. Deploy on cloud platform

### Q: Can I integrate with Discord/Telegram?
**A:** Yes! You can create bot integrations using their respective APIs.

### Q: How do I contribute to the project?
**A:** 
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Q: Can I use this commercially?
**A:** Yes, it's MIT licensed. But check API provider terms for commercial use.

## Getting Help

### Q: Where can I get help?
**A:** 
1. Check this FAQ
2. Read INSTALLATION.md
3. Check COMMANDS.md
4. Open an issue on GitHub
5. Check existing GitHub issues

### Q: How do I report a bug?
**A:** Open an issue on GitHub with:
1. Description of the problem
2. Steps to reproduce
3. Error messages
4. Your OS and Python version

### Q: Can I request new features?
**A:** Yes! Open a feature request issue on GitHub.

---

**Still have questions? Open an issue on GitHub! 🚀**
