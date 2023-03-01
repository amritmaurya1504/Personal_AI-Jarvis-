from Body.Speak import Speak
import requests

def News():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=29f4cc4276a14cfebe4a2ee7c47211ea"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "Second", "third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        Speak(f"today's {day[i]} new is : {head[i]}!")

