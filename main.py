print(">> Starting The Jarvis : Wait For Some Seconds.")
from Features.Wakeup import WakeUpDetected
print(">> Starting The Jarvis : Wait For Few Seconds.")
import os
import playsound
def WakeUp():
    while True:
        query = WakeUpDetected()
        if query == None or len(query) == 0:
            pass
        elif "wake up" in query or "wakeup" in query or "hello" in query or "jarvis" in query:
            print("Jarvis Started!")
            os.startfile("E:\\PersonalAI(Assistant)\\Jarvis.py")
            playsound.playsound("E:\PersonalAI(Assistant)\Sounds\JARVIS STARTUP SOUND.mp3")
        else:
            pass

WakeUp()