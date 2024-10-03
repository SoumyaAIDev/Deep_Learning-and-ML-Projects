import pyttsx3 as p
import speech_recognition as sr
import pyaudio

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()



r = sr.Recognizer()

speak("hello madam I am your voice assistant.How are you")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)

    text=r.recognize_google(audio)
    print(text)

if "What" and "about" and "You" in text:
    speak("I am  also having a good day sir")
speak("What can I do for you")
