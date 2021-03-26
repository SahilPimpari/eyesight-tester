#modules to be installed

import speech_recognition as sr #pip install speechRecognition
import pyttsx3                  #pip install pyttsx3
import webbrowser               #in-built
import pywhatkit                #pip install pywhatkit
import os                       #in-built
import datetime                 #in-built
import wikipedia                #pip install wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("I am your assistant, How may i help you")

def take_command():
    with sr.Microphone() as source:
        print('listening . . . ')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print("User:", command)

        try:
            print("Recognizing . . .")
            command = r.recognize_google(audio, language='en-in')

        except Exception as e:
            pass
        return command

if __name__ == '__main__':
    wish_me()
    while True:
        command = take_command().lower()

        if 'wikipedia' in command:
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=1)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'youtube' in command:
            webbrowser.open("youtube.com")

        elif 'google' in command:
            webbrowser.open("google.com")
            exit()

        elif 'time' in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The tme is {time}")
            print("The time is ", time)

        elif 'date' in command:
            date = datetime.datetime.today()
            speak(date)
            print(date)

        elif 'play' in command:
            object = command.replace("youtube", "")
            pywhatkit.playonyt(object)
            exit()

        elif 'exit' in command:
            exit()

        else:
            speak("you are trying to tell the command that is not programmed in me, please try again ")