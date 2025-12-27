# 🎤 Voice Commands Reference

## Complete List of Voice Commands

### 🔹 Basic Interaction

| Command | Action |
|---------|--------|
| "Hello Jarvis" / "Hey Jarvis" / "Hi Jarvis" | Activate and greet |
| "What's your name?" | Introduction |
| "Who are you?" | About Jarvis |
| "What can you do?" | List capabilities |
| "Exit" / "Quit" / "Goodbye" / "Bye" | Close assistant |

### 🔹 Time & Date

| Command | Action |
|---------|--------|
| "What time is it?" | Current time |
| "Tell me the time" | Current time |
| "What's the date?" | Current date |
| "Tell me the date" | Current date |

### 🔹 Web Browsing

| Command | Action |
|---------|--------|
| "Open Google" | Opens Google.com |
| "Open YouTube" | Opens YouTube.com |
| "Open GitHub" | Opens GitHub.com |
| "Open Facebook" | Opens Facebook.com |
| "Open Twitter" | Opens Twitter.com |

### 🔹 Search

| Command | Action |
|---------|--------|
| "Search for [query]" | Google search |
| "Search [query]" | Google search |
| "Google [query]" | Google search |

**Examples:**
- "Search for Python tutorials"
- "Search best restaurants near me"
- "Google latest technology news"

### 🔹 YouTube

| Command | Action |
|---------|--------|
| "Play [song/video] on YouTube" | Play video |
| "Play [artist name] on YouTube" | Play artist's videos |

**Examples:**
- "Play Imagine Dragons on YouTube"
- "Play Python tutorial on YouTube"
- "Play relaxing music on YouTube"

### 🔹 Wikipedia

| Command | Action |
|---------|--------|
| "Wikipedia [topic]" | Search Wikipedia |
| "Tell me about [topic] from Wikipedia" | Wikipedia search |

**Examples:**
- "Wikipedia Artificial Intelligence"
- "Wikipedia Elon Musk"
- "Tell me about Python from Wikipedia"

### 🔹 Weather

| Command | Action |
|---------|--------|
| "What's the weather?" | Weather info (asks for city) |
| "Tell me the weather" | Weather info |
| "Weather forecast" | Weather info |

**Note:** Requires Weather API key in config.py

### 🔹 News

| Command | Action |
|---------|--------|
| "Tell me the news" | Top 5 headlines |
| "What's the news?" | Latest news |
| "News headlines" | Top headlines |

**Note:** Requires News API key in config.py

### 🔹 AI Chat

| Command | Action |
|---------|--------|
| "Ask AI [question]" | Chat with AI |
| "Chat with AI [question]" | AI conversation |

**Examples:**
- "Ask AI what is machine learning"
- "Chat with AI about space exploration"
- "Ask AI to write a poem"

**Note:** Requires OpenAI API key in config.py

### 🔹 Entertainment

| Command | Action |
|---------|--------|
| "Tell me a joke" | Random joke |
| "Make me laugh" | Random joke |

### 🔹 System Control

| Command | Action |
|---------|--------|
| "Open Notepad" | Opens Notepad |
| "Open Calculator" | Opens Calculator |
| "Open Paint" | Opens Paint |
| "Open Chrome" | Opens Chrome browser |
| "Open Firefox" | Opens Firefox browser |
| "Open Edge" | Opens Edge browser |

### 🔹 Screenshots

| Command | Action |
|---------|--------|
| "Take a screenshot" | Capture screen |
| "Screenshot" | Capture screen |

**Note:** Saves as 'screenshot.png' in current directory

## 🎯 Tips for Best Results

1. **Speak Clearly** - Pronounce words clearly
2. **Reduce Background Noise** - Use in quiet environment
3. **Wait for "Listening"** - Speak after seeing the listening indicator
4. **Natural Speech** - Speak naturally, not too fast or slow
5. **Complete Sentences** - Use complete commands

## 🔧 Customizing Commands

You can add your own commands by editing `jarvis.py`:

```python
def process_command(command):
    # Add your custom command here
    if 'your custom phrase' in command:
        speak("Your response")
        # Your action code
```

## 📝 Command Examples by Category

### Productivity
```
"What time is it?"
"What's the date?"
"Take a screenshot"
"Open Calculator"
```

### Information
```
"Wikipedia Python programming"
"What's the weather?"
"Tell me the news"
"Search for best laptops 2024"
```

### Entertainment
```
"Play Coldplay on YouTube"
"Tell me a joke"
"Open YouTube"
```

### AI Assistance
```
"Ask AI to explain quantum computing"
"Chat with AI about climate change"
"Ask AI to write a story"
```

---

**Need more commands? Open an issue on GitHub with your suggestions! 🚀**
