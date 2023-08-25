#Create python script which whenever you make  copy for text , it stores that and upon presseing alt+shift+s it will append what is stored into your notes.txt

import keyboard
import pyperclip

def on_trigger():
    with open('Paste_List.txt', 'a') as f:
        f.write(pyperclip.paste() + '\n')

def listen():
    sc = "ctrl + alt + s"

    keyboard.add_hotkey(sc, on_trigger)

    keyboard.wait()

listen()
