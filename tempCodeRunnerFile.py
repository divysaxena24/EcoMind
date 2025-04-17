#pip install pyttsx3 speechrecognition pyaudio

# pip install pipwin
# pipwin install pyaudio

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import requests
import wikipedia
import openai
import pywhatkit
import pyjokes
from config import OPENAI_API_KEY 

API_KEY = "YOUR_API_KEY"



#initialise speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150) #speed of speech

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    
import requests

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:
        main = data["main"]
        temp = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degrees Celsius with {weather_desc}. Humidity is {humidity} percent.")
    else:
        error_message = data.get("message", "an unknown error occurred")
        speak(f"Sorry, I couldn't get the weather for {city}. Error: {error_message}")


    
def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good Morning")
    elif 12 <=hour< 18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("Hi D.S., I'm your Assistant! EcoMind. How can I help you ?")
    
        
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print("You Said", query)
        
    except Exception:
        speak("Sorry, I didn't understood")
        return None
    return query.lower()

def perform_task(query):
    query = query.lower()
    
    if "youtube" in query and any(kw in query for kw in["open", "launch", "start"]):
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        
    elif "google" in query and any(kw in query for kw in ["open", "launch", "start"]):
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        
    elif "joke" in command:
            speak(pyjokes.get_joke())
            
    
    elif any(kw in query for kw in ["vs code", "visual studio"]) and any(action in query for action in ["open", "launch", "start"]):
        speak("Opening VS code")
        os.startfile("E:\DOWNLOADS F\Microsoft VS Code\Code.exe")
        
    elif 'weather' in command:
        speak("Which city?")
        city_command = take_command()
        get_weather(city_command)

        
    elif "time" in query and any(kw in query for kw in["what", "tell", "current"]):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        
    elif 'wikipedia' in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
    
    elif any(kw in query for kw in ['exit', 'quit', 'stop']):
        speak("Goodbye! Have a great day!")
        exit()
    
  

        
    else:
        speak("Hmm, I'm not trained for that yet.")
    

# Run the assistant
if __name__ == "__main__":
    greet_user()
    while True:
        command = take_command()
        if command:
            perform_task(command)
