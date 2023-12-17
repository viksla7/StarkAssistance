import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import os
import pyttsx3
import sys
import pyautogui
import subprocess
import keyboard
import spacy
from GoogleNews import GoogleNews

nlp = spacy.load("en_core_web_sm")

googlenews = GoogleNews()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

recognizer = sr.Recognizer()
doc = nlp("Hello, I'm Jarvis. How may I assist you?")
for sentence in doc.sents:
    print(sentence)
    engine.say(sentence)
    engine.runAndWait()

def cmd():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        engine.say('I am Listening Sir!')
        print('Listening...')
        engine.runAndWait()
        recognizer.pause_threshold = 1
        recordedaudio = recognizer.listen(source)
        engine.say('Recognized Sir!')
        print('Recognized!')
        engine.runAndWait()

    try:
        user_command = recognizer.recognize_google(recordedaudio, language='en-in')
        user_command = user_command.lower()
        print('User Said:', user_command)

        if 'exit' in user_command or 'stop' in user_command or 'quit' in user_command:
            engine.say('I am signing off sir!')
            engine.runAndWait()
            sys.exit()

        if 'search' in user_command:
            search_query = user_command.replace('search', '').strip()
            engine.say('On it sir...')
            engine.say(f"Searching Google for {search_query}")
            engine.runAndWait()
            engine.say('As per search results')
            pywhatkit.search(search_query)

        if 'describe' in user_command:
            engine.say('On it sir...')
            engine.runAndWait()
            result = wikipedia.summary(user_command, sentences=2)
            print(result)
            engine.say('As per wikipedia')
            engine.say(result)
            engine.runAndWait()

        if 'youtube' in user_command or 'play' in user_command:
            engine.say('Opening Youtube')
            engine.runAndWait()
            search_query = user_command.replace('youtube', '')
            pywhatkit.playonyt(search_query)

        if 'time' in user_command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            engine.say('The time is ' + current_time)
            engine.runAndWait()
            engine.say('For your convenience, I am printing it on the screen sir!')
            engine.runAndWait()
            print("The time is:", current_time)

        if 'news' in user_command:
            engine.say('Collecting information Sir!')
            engine.runAndWait()
            googlenews.get_news('Today news')
            googlenews.result()
            headlines = googlenews.gettext()
            print(*headlines, sep='\n')
            engine.say('Here are the headlines Sir!')
            engine.say(headlines)
            engine.runAndWait()

        if 'increase volume' in user_command or 'decrease volume' in user_command or 'mute' in user_command:
            if 'increase volume' in user_command:
                keyboard.press_and_release("volume up")
                engine.say("Volume increased.")
                engine.runAndWait()
                print("Volume increased")
            elif 'decrease volume' in user_command:
                keyboard.press_and_release("volume down")
                engine.say("Volume decreased")
                engine.runAndWait()
                print("Volume decreased.")
            elif 'mute' in user_command:
                keyboard.press_and_release("volume mute")
                engine.say("Volume muted")
                engine.runAndWait()
                print("Volume muted.")

        if 'chrome' in user_command or 'microsoft edge' in user_command or 'brave' in user_command or 'new tab' in user_command or 'close the tab' in user_command or 'bookmark' in user_command:
            if 'chrome' in user_command:
                app_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                engine.say('Opening browser')
                engine.runAndWait()
            elif 'microsoft edge' in user_command:
                app_path = 'C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe'
                engine.say('Opening browser')
                engine.runAndWait()
            elif 'brave' in user_command:
                app_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
                engine.say('Opening browser')
                engine.runAndWait()
            elif 'open new tab' in user_command:
                engine.say('Opening a new tab')
                engine.runAndWait()
                keyboard.press_and_release('ctrl+t')
                engine.say('New tab opened')
                engine.runAndWait()
            elif 'close the tab' in user_command:
                engine.say('closing the tab')
                engine.runAndWait()
                keyboard.press_and_release('ctrl+w')
                engine.say("tab closed")
                engine.runAndWait()
            elif 'bookmark' in user_command:
                keyboard.press_and_release('ctrl+d')
                engine.say('please accept to bookmark this tab')
                engine.runAndWait()

            try:
                subprocess.Popen(app_path)
            except FileNotFoundError:
                print("Application not found.")
            except Exception as e:
                print("An error occurred:", e)

        if 'notepad' in user_command:
            app_path = 'C:\\Windows\\notepad.exe'
            engine.say('Opening Notepad')
            engine.runAndWait()
            try:
                subprocess.Popen(app_path)
            except FileNotFoundError:
                engine.say("Application not found.")
                engine.runAndWait()
                print("Application not found.")
            except Exception as e:
                print("An error occurred: ", e)

        if 'screenshot' in user_command:
            engine.say('Taking a screenshot')
            engine.runAndWait()
            try:
                screenshot_path = 'C:\\Users\\KITTU\\OneDrive\\Pictures\\Screenshots'

                if not os.path.exists(screenshot_path):
                    os.makedirs(screenshot_path)

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_filename = f'screenshot_{timestamp}.png'

                screenshot = pyautogui.screenshot()
                screenshot.save(os.path.join(screenshot_path, screenshot_filename))

                engine.say(f'Screenshot saved as {screenshot_filename}')
                engine.runAndWait()

            except Exception as e:
                print("An error occurred:", e)

        if 'create a folder' in user_command:
            engine.say('Creating a new folder')
            engine.runAndWait()
            try:
                folder_path = 'C:\\Users\\KITTU\\NewFolder'
                os.makedirs(folder_path)
                engine.say(f'Folder created at {folder_path}')
                engine.runAndWait()
            except Exception as e:
                print("An error occurred:", e)

        if 'files' in user_command:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            engine.say('Opening desktop files')
            engine.runAndWait()
            try:
                os.startfile(desktop_path)
            except Exception as e:
                print("An error occurred:", e)

        if 'd drive' in user_command:
            drive_path = 'D:\\'
            engine.say(f'Opening files in {drive_path}')
            engine.runAndWait()
            try:
                os.startfile(drive_path)
            except Exception as e:
                print("An error occurred:", e)

        if 'close application' in user_command:
            engine.say("Closing Application")
            engine.runAndWait()
            keyboard.press_and_release('alt+f4')
            engine.say('application closed')
            engine.runAndWait()

    except Exception as ex:
        doc = nlp("Sorry Sir, Could not understand. Please repeat it again sir!")
        for sentence in doc.sents:
            print(sentence)
            engine.say(sentence)
            engine.runAndWait()

while True:
    cmd()
