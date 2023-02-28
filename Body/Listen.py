import speech_recognition as sr
from googletrans import Translator

# 1 Listen Function
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = False
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    return query

# 2 Translator
def TraslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    return data

# 3 takeCommand
def MicExecution():
    query = Listen()
    data = TraslationHinToEng(query)
    print(f"You said : {data}")
    return data
