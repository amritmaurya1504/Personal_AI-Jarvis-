from Body.Speak import Speak
import webbrowser
import os

def OpenApp(query):
    Speak("Ok sir, wait a second!")

    if 'code' in query:
        os.startfile("C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif "spotify" in query:
        path = "C:\\Users\Dell\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
        os.startfile(path)
    elif 'telegram' in query:
        os.startfile("E:\\Applications\\Telegram Desktop\\Telegram Desktop\\Telegram.exe")
    elif 'chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif 'facebook' in query:
        webbrowser.open('https://www.facebook.com/')
    elif 'instagram' in query:
        webbrowser.open('https://www.instagram.com/')
    elif 'maps' in query:
        webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')
    elif 'youtube' in query:
        webbrowser.open('https://www.youtube.com')
    elif "note" in query:
        Speak("Opening sir. usually it's take time so be patient")
        path = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Notion\\Notion.exe"
        os.startfile(path)
    elif "command prompt" in query or "cmd" in query or "terminal" in query:
        os.system("start cmd")
    elif "sql" in query:
        path = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
        os.startfile(path)
    elif "leetcode" in query or "leet code" in query:
        webbrowser.open('http://leetcode.com/rajamrit_15')

    Speak("Your Command Has Been Completed Sir!")