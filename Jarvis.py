import playsound

from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
print(">> Starting The Jarvis : Wait For Few Seconds.")
from Features.Music import Music
from Features.Location import Location
from Features.Internet import Internet
from Features.News import News
from Features.Screenshot import Screensort
from Features.Temp import Temp
from Features.Alarm import Alarm
from Features.Open import OpenApp
from Features.WhatsApp import WhatsappSender
from Features.EmailExtraction import EmailExtract
import requests
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import psutil
from pywikihow import search_wikihow


def MainExecution():
    # Speak("Welcome back Sir")
    # Speak("I'm Jarvis, I'm Ready To Assist you sir.")
    while True:
        query = MicExecution()

        if query == None or len(query) == 0:
            pass
        elif "you can sleep" in query or "sleep in" in query:
            Speak("Okay sir. call me when you need")
            break
        elif "ip" in query or 'IP' in query or 'Ip' in query:
            ip = requests.get('https://api.ipify.org').text
            Speak(f"Sir Your ip addres is {ip}")
        elif 'youtube search' in query:
            Speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'google search kro' in query or 'search on google' in query or 'google' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            query = query.replace("kro", "")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")
        elif 'repository' in query:
            Speak("Ok Sir , Launching.....")
            web = "https://github.com/amritmaurya1504"
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = MicExecution()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"According To Wikipedia : {wiki}")
        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
        elif 'music' in query:
            Music()
        elif "where i am" in query or "where we are" in query or "kaha hai avi" in query:
            Speak("wait sir, let me check")
            Location()
        elif "thank you" in query:
            Speak("your welcome sir!")
        elif "volume up" in query:
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "how much power left" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            Speak(f"sir our system have {percentage} percent battery!")
            if percentage >= 75:
                Speak("we have enough power to continue our work")
            elif percentage >= 40 and percentage <= 75:
                Speak("we should connect our system to charging point to charge our battery")
            elif percentage <= 15 and percentage <= 40:
                Speak("we don't have enough power to work, please connect to charging")
            else:
                Speak("we have ver low power, please connect to charging the system will shutdown very soon")
        elif "okay" in query:
            Speak("okay sir")
        elif "internet speed" in query or 'speed' in query or 'downloading speed' in query:
            Internet()
        elif "tell me today's top headlines" in query or "news" in query:
            Speak("please wait sir, fetching top headlines")
            News()
        elif "screenshot" in query:
            Screensort()
        elif "temperature" in query:
            Temp()
        elif "alarm" in query:
            Alarm()
        elif "open" in query:
            OpenApp(query)
        elif "email" in query or "emails" in query:
            EmailExtract()
        elif "whatsapp" in query or "message" in query or "send message" in query:
            Speak("Whom do you want do send message sir!")
            q = MicExecution()
            WhatsappSender(q)
        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
        elif 'advance' in query or 'advanced' in query:
            Speak("Entering advanced mode Sir!")
            playsound.playsound("E:\\PersonalAI(Assistant)\\Sounds\\futuristic-interface-hud-sound-effects_xxiCVAZo.mp3")
            Speak("Entered Sir.")
            while True:
                Data = MicExecution()
                Data = str(Data)

                if len(Data) == 0:
                    pass
                elif "switch" in Data or "exit" in Data:
                    break
                else:
                    Reply = ReplyBrain(Data)
                    Speak(Reply)



MainExecution()