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
from config import OPENAI_API_KEY 
import pyjokes


openai.api_key = OPENAI_API_KEY 



#initialise speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150) #speed of speech

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    
import requests

# Replace with your actual API key
    
def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good Morning")
    elif 12 <=hour< 18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("Hi D.S., I'm your Assistant! EcoMind. How can I help you ?")


def answer_question(query):
    try:
        # First, try to search the question on Wikipedia
        if 'wikipedia' not in query:
            speak("Searching Wikipedia...")
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
            return
        
        # If Wikipedia doesn't provide a direct answer, fallback to OpenAI API (GPT-3)
        speak("Sorry, I couldn't find the answer on Wikipedia. Let me try my best.")
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=150
        )

        answer = response.choices[0].text.strip()
        speak(answer)

    except Exception as e:
        speak(f"Sorry, I couldn't get an answer. Error: {str(e)}")
        
        
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
        
    elif "what is" in query or "who is" in query or "how is" in query or "when is" in query:  # Identifying general questions
        answer_question(query)
        
    else:
        speak("Hmm, I'm not trained for that yet.")
    

# Run the assistant
if __name__ == "__main__":
    greet_user()
    while True:
        command = take_command()
        if command:
            perform_task(command)
            
            
  # This will show you the raw response for troubleshooting

