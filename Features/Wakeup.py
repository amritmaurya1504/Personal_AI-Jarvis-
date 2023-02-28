import speech_recognition as sr
import os

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
    print(query)
    return query

def WakeUpDetected():
    query = Listen()

    if "wake up" in query or "wakeup" in query or "hello" in query:
        return query
    else:
        pass

