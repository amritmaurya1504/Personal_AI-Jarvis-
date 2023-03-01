import playsound
from Body.Speak import Speak
from Body.Listen import MicExecution
import datetime

def Alarm():
    Speak("Enter The Time Sir !")
    time = input(": Enter The Time :")

    while True:
        Time_Ac = datetime.datetime.now()
        now = Time_Ac.strftime("%Y-%M-%D %H:%M:%S")

        if now == time:
            Speak("Time To Wake Up Sir!")
            while True:
                Speak("Wake up sir!")
                playsound("E:\pythonProject\jarvis\iron.mp3")
                query = MicExecution()
                if "close" in query or "stop" in query:
                    Speak("Okay Sir, Alarm Closed!")
                    break
                else:
                    playsound("E:\pythonProject\jarvis\iron.mp3")
                # playsound("E:\pythonProject\jarvis\iron.mp3")

        elif now > time:
            break

