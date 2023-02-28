from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Wakeup import WakeUpDetected
print(">> Starting The Jarvis : Wait For Few Seconds.")

def MainExecution():
    Speak("Welcome back Sir")
    # Speak("I'm Jarvis, I'm Ready To Assist you sir.")

    while True:
        Data = MicExecution()
        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)

def WakeUp():
    query = WakeUpDetected()
    if "wake up" in query or "wakeup" in query or "hello" in query:
        print("")
        print("Jarvis Started!")
        print("")
        MainExecution()
    else:
        pass

WakeUp()