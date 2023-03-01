from Body.Speak import Speak
from Body.Listen import MicExecution
import pyautogui
import os

def Screensort():
    Speak("Ok Sir , What Should I Name That File ?")
    path = MicExecution()
    path1name = path + ".png"
    path1 = "D:\\Screensort\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    Speak("Do you want to open it sir?")
    query = MicExecution()
    if "yes" in query or "haa" in query or "yup" in query:
        os.startfile(path1)
        Speak("Here Is Your ScreenShot")
    else:
        Speak("Okay sir, No problem!")

