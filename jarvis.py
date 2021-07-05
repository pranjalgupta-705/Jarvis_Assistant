import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("Hello Sir, I am Jarvis. Please tell me how may I help you")

def time():
    hour = datetime.datetime.now().strftime("%H:%M:%S")
    speak(hour + "Of Clock")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say again Please....")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # Logic for executing tasks on basis of query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=4)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("Enter command")
            command = takecommand().lower()
            webbrowser.open("https://www.youtube.com/results?search_query=" + command)

        elif 'open google' in query:
            speak("Enter command")
            command = takecommand().lower()
            webbrowser.open("https://google.com/?#q=" + command)
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            time()
        elif 'play music' in query:
            music_dir = r'D:\\New folder'
            songs = os.listdir(music_dir)
            os.startfile((os.path.join(music_dir, songs[0])))
        elif 'who is manish upreti' in query:
            speak("manish upreti is your friend")

        elif 'stop' in query:
            break



