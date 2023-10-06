import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import subprocess as sp
from GoogleNews import GoogleNews


googlenews=GoogleNews()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)


googlenews=GoogleNews()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)


recognizer=sr.Recognizer()


def cmd():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        engine.say('I am Listening Sir!')
        print('Listening...')
        engine.runAndWait()
        recognizer.pause_threshold=1
        recordedaudio=recognizer.listen(source)
        engine.say('Recognized Sir!')
        print('Recognized!')
        engine.runAndWait()
    
    try:
        user_command=recognizer.recognize_google(recordedaudio,language='en-in')
        user_command.lower()
        print('User said: ',format(user_command))
        
    except Exception as ex:
        engine.say('Sorry Sir, Could not understand, Please repeat it again sir!')
        engine.runAndWait()
        user_command='None'
        return user_command
                   
    if 'search' in user_command:
        engine.say('On it sir...')
        engine.runAndWait()
        result=wikipedia.summary(user_command,sentences=2)
        print(result)
        engine.say('As per search results')
        engine.say(result)
        engine.runAndWait()
            
    if 'play' in user_command:
        engine.say('Opening Youtube')
        engine.runAndwait()
        pywhatkit.playonyt(user_command)
                   
    if 'time' in user_command:
        time=datetime.datetime.now()
        engine.say('The time is')
        engine.say(time)
        engine.runAndWait()
        engine.say('For your convenience, I am printing it on the sceen sir!')
        engine.runAndWait()
        print(time)
                   
    if 'news' in user_command:
        engine.say('Collecting information Sir!')
        engine.runAndWait()
        googlenews.get_news('Today news')
        googlenews.result()
        googlenews.get_text()
        print(*google.get_text(),sep='\n')
        engine.say('Here are the headlines Sir!')
        engine.say(googlenews.get_text())
        engine.runAndWait()
                   
    if 'chrome' in user_command:
        engine.say('Opening Chrome')
        engine.runAndWait()
        browser=sp.Popen('[C:\Program Files (x86)\Google\Chrome\Application\chrome.exe]')
                   
    if 'exit' in user_command:
        engine.say('I am signing off sir!')
        engine.runAndWait()
          
while True:
    cmd()