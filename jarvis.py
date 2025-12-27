#!/usr/bin/env python3
"""
Jarvis AI Voice Assistant
Advanced voice-controlled assistant with multiple capabilities
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import wikipedia
import pywhatkit
import requests
import json
from pathlib import Path

# Try to import optional dependencies
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import config
except ImportError:
    config = None

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Select voice (0 = male, 1 = female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Convert text to speech"""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice command"""
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("🔄 Recognizing...")
            
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
            return command.lower()
            
        except sr.WaitTimeoutError:
            return "timeout"
        except sr.UnknownValueError:
            return "none"
        except sr.RequestError:
            speak("Sorry, speech service is unavailable")
            return "none"
        except Exception as e:
            print(f"Error: {e}")
            return "none"

def get_weather(city="Delhi"):
    """Get weather information"""
    try:
        if config and hasattr(config, 'WEATHER_API_KEY'):
            api_key = config.WEATHER_API_KEY
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                speak(f"The temperature in {city} is {temp} degrees celsius with {description}")
            else:
                speak("Unable to fetch weather information")
        else:
            speak("Weather API key not configured")
    except Exception as e:
        speak("Error fetching weather data")
        print(f"Weather error: {e}")

def get_news():
    """Get latest news headlines"""
    try:
        if config and hasattr(config, 'NEWS_API_KEY'):
            api_key = config.NEWS_API_KEY
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                articles = data['articles'][:5]
                speak("Here are the top news headlines")
                for i, article in enumerate(articles, 1):
                    speak(f"News {i}: {article['title']}")
            else:
                speak("Unable to fetch news")
        else:
            speak("News API key not configured")
    except Exception as e:
        speak("Error fetching news")
        print(f"News error: {e}")

def chat_with_ai(prompt):
    """Chat with OpenAI GPT"""
    try:
        if OPENAI_AVAILABLE and config and hasattr(config, 'OPENAI_API_KEY'):
            client = OpenAI(api_key=config.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            answer = response.choices[0].message.content
            speak(answer)
        else:
            speak("AI chat is not configured. Please add your OpenAI API key")
    except Exception as e:
        speak("Error connecting to AI")
        print(f"AI error: {e}")

def open_application(app_name):
    """Open system applications"""
    apps = {
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'chrome': 'chrome.exe',
        'firefox': 'firefox.exe',
        'edge': 'msedge.exe'
    }
    
    try:
        if app_name in apps:
            os.system(apps[app_name])
            speak(f"Opening {app_name}")
        else:
            speak(f"Sorry, I don't know how to open {app_name}")
    except Exception as e:
        speak(f"Error opening {app_name}")
        print(f"App error: {e}")

def process_command(command):
    """Process user commands"""
    
    # Greetings
    if any(word in command for word in ['hello', 'hey', 'hi']):
        speak("Hello! I am Jarvis, your AI assistant. How can I help you?")
    
    # Introduction
    elif 'your name' in command:
        speak("I am Jarvis, your personal AI voice assistant")
    
    elif 'who are you' in command:
        speak("I am Jarvis, an advanced AI assistant created to help you with various tasks")
    
    # Capabilities
    elif 'what can you do' in command or 'your capabilities' in command:
        speak("I can help you with web searches, play music, tell weather, news, jokes, open applications, and much more. Just ask me!")
    
    # Time and Date
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")
    
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {date}")
    
    # Web browsing
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif 'open github' in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    
    # Search
    elif 'search for' in command or 'search' in command:
        query = command.replace('search for', '').replace('search', '').strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    # YouTube
    elif 'play' in command and 'youtube' in command:
        song = command.replace('play', '').replace('on youtube', '').strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    
    # Wikipedia
    elif 'wikipedia' in command:
        query = command.replace('wikipedia', '').strip()
        try:
            speak(f"Searching Wikipedia for {query}")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find that on Wikipedia")
    
    # Weather
    elif 'weather' in command:
        speak("Which city's weather would you like to know?")
        city_command = listen()
        if city_command != "none":
            get_weather(city_command)
        else:
            get_weather()
    
    # News
    elif 'news' in command:
        get_news()
    
    # AI Chat
    elif 'ask ai' in command or 'chat with ai' in command:
        query = command.replace('ask ai', '').replace('chat with ai', '').strip()
        chat_with_ai(query)
    
    # Jokes
    elif 'joke' in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        import random
        speak(random.choice(jokes))
    
    # Applications
    elif 'open' in command:
        app = command.replace('open', '').strip()
        open_application(app)
    
    # Screenshot
    elif 'screenshot' in command or 'take screenshot' in command:
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')
            speak("Screenshot saved")
        except:
            speak("Unable to take screenshot")
    
    # Exit
    elif any(word in command for word in ['exit', 'quit', 'goodbye', 'bye']):
        speak("Goodbye! Have a great day!")
        sys.exit()
    
    # Unknown command
    else:
        speak("I'm not sure how to help with that. Can you please rephrase?")

def main():
    """Main function"""
    speak("Initializing Jarvis AI Assistant")
    speak("Hello! I am Jarvis. How can I assist you today?")
    
    while True:
        command = listen()
        
        if command == "timeout":
            continue
        elif command == "none":
            continue
        else:
            process_command(command)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Shutting down Jarvis")
        sys.exit()
