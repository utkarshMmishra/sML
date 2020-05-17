import ctypes
import speech_recognition as sr
import pyautogui
import webbrowser
import re
import random
import pyttsx3
import datetime
import os

speech = sr.Recognizer()
try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initilize')

voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)


class gui():
    value = (420, 340)


def start():
    pyautogui.click(gui.value)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    play_sound(mp3)


def read_voice_cmd():
    voice_text = ''
    print ('listening.....')

    try:
        with sr.Microphone() as source:
            print("Say something")
            speech.pause_threshold = 1
            audio= speech.listen(source)

        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        speak_text_cmd('i cannot understand sir')
        print('i cannot understand sir')
        pass
    except sr.RequestError as e:
        speak_text_cmd('there is network error')
        print('Network error')
        pass

    return voice_text

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak_text_cmd("Good Morning!")

    elif hour>=12 and hour<18:
        speak_text_cmd("Good Afternoon!")  

    else:
        speak_text_cmd("Good Evening!") 

    speak_text_cmd("I am Smith Sir. Please tell me how may I help you")  

if __name__ == '__main__':
    wishMe()
    while True:
        voice_note = read_voice_cmd()
        voice_note = voice_note.lower()
        print('cmd : {}'.format(voice_note))
        if 'hello' in voice_note:
            speak_text_cmd('hello sir how may i help you')
            continue

        elif 'open fb' in voice_note:
            url = 'https://www.facebook.com/'
            webbrowser.open(url)
            print('Done!')
            speak_text_cmd('sure sir')
            continue

        elif 'play music' in voice_note:
            music_dir = 'C:\\Users\\Utkarsh\\Music\\14 - KISHORE NAUGHTY MOOD'
            songs = os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[0]))
            continue

        elif 'the time' in voice_note:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"Sir, the time is {strTime}")
            continue

        elif 'lock my' in voice_note:
            for value in ['pc', 'computer', 'system']:
                ctypes.windll.user32.LockWorkStation()
            speak_text_cmd("take a break sir")

        elif 'play a song' in voice_note:
            speak_text_cmd('which song sir:')
            song = read_voice_cmd()
            reg_ex = re.search('open youtube (.*)', song)
            url = ('https://www.youtube.com/results?search_query=' + song + '%2F')
            webbrowser.open(url)
            speak_text_cmd('here we go sir')
            print('Done!')
            speak_text_cmd("do you want to play it sir")
            continue

        elif 'select that' in voice_note:
            start()
            continue

        elif 'open wikipedia' in voice_note:
            speak_text_cmd('on which topic sir:')
            topic = read_voice_cmd()
            reg_ex = re.search('open wikipedia (.*)', topic)
            url = ('https://en.wikipedia.org/wiki/' + topic)
            webbrowser.open(url)
            speak_text_cmd('here is the information about' + topic)
            print('Done!')
            continue

        elif 'bye' in voice_note:
            speak_text_cmd('have a nice day sir')
            exit()

