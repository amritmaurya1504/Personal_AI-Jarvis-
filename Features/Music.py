import pywhatkit
from Body.Listen import MicExecution
from Body.Speak import Speak
import os


def Music():
    Speak("Tell Me The NamE oF The Song!")
    musicName = MicExecution()
    if 'akeli' in musicName:
        os.startfile('E:\\Music\\akeli.mp3')
    elif 'blanko' in musicName:
        os.startfile('E:\\Music\\blanko.mp3')
    else:
        pywhatkit.playonyt(musicName)

    Speak("Your Song Has Been Started! , Enjoy Sir!")


