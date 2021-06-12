import speech_recognition as sr
import pyttsx3 as tts
import time
import webbrowser
import random
import subprocess
import datetime
import pywhatkit as kit
import pyjokes
from time import ctime

r = sr.Recognizer()

def robo_speak(command):

    print(command)
    engine = tts.init()
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 2.0)
    engine.say(command)
    engine.runAndWait()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            robo_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            robo_speak('Sorry, I did not get that.')
        except sr.RequestError:
            robo_speak('Sorry, my speech service is down.')
        return voice_data

def respond(voice_data):

    NOTE_STRS = ["make a note", "write this down", "remember this"]

    if "hello" in voice_data:
        print("Hello")
        robo_speak('Hey!')

    if 'what is your name' in voice_data:
        print("What is your name?")
        robo_speak('My name is Mini Robo.')

    if 'what time is it' in voice_data:
        print("What time is it?")
        robo_speak(ctime())

    if 'search' in voice_data:
        print("Search")
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        robo_speak('Here is what I found for ' + search + '.')

    if 'find location' in voice_data:
        print("Find location")
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        robo_speak('Here is the location of ' + location + '.')

    if (str(voice_data) in NOTE_STRS):
        print(str(voice_data))
        notes = record_audio("What would you like me to write down?")
        note(notes)

    if 'play a video' in voice_data:
        print("Play a video")
        video = record_audio('What is the name of the video?')
        kit.playonyt(video)
        robo_speak('Here is your video.')

    if 'play a song' in voice_data:
        print("Play a song")
        song = record_audio('What is the name of the song?')
        kit.playonyt(song)
        robo_speak('Here is your song.')

    if 'tell a joke' in voice_data:
        print("Tell a joke")
        robo_speak(pyjokes.get_joke(language='en', category= 'all'))

    if 'exit' in voice_data:
        print("Exit")
        robo_speak('Good Bye!')
        exit()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    robo_speak('I have noted:\n' + text)
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

time.sleep(1)
robo_speak('Hello, how can I help you?')
while 1:
    print("Listening...")
    voice_data = record_audio()
    respond(voice_data)