from Body.Speak import Speak
from Body.Listen import MicExecution
from bs4 import BeautifulSoup
import requests



def Temp():
    search = "temperature in kolkata"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    Speak(f"The Temperature Outside Is {temperature}!")
    if temperature > '30°C':
        Speak("Sir! temperature outside is too hot, it's better to stay indore")
        query = MicExecution()
        if 'okay' in query or 'thik' in query or 'haa' in query:
            Speak("Okay Sir!")

    Speak("Do I Have To Tell You Another Place Temperature ?")
    next = MicExecution()

    if 'yes' in next or 'haa' in next or 'ha' in next:
        Speak("Tell Me The Name Of tHE Place ")
        name = MicExecution()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        Speak(f"The Temperature in {name} is {temperature} celcius")

    else:
        Speak("no problem sir")

