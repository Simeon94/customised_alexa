import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices' )
engine.setProperty('voice', voices[1], id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

    query = text
    info = wikipedia.summary(query, 1)
    print(info)
    talk(info) 
    
def take_command():
    try:
        with sr.Microphone()as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognise_google(voice)
            command  = command.lower()
            if alexa in command:
                command.replace('alexa', " ")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', *)
        talk('playing song')
        pywhatkit.playonyt(song)

    elif 'time in command':
        time = datetime.datetime.now().strftime( %I:%M:%p*)
        talk( Current time is '+time')
