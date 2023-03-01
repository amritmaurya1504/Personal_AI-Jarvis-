import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Windows Based

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

# options = Options()
# options.add_argument('--log-level=3')
# options.headless = True
# # options.add_argument('--headless=new')
# driver = webdriver.Chrome(executable_path="./Database/chromedriver.exe",options=options)
# driver.maximize_window()
# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')
#
# def Speak(Text):
#     lengthOfText = len(str(Text))
#     if lengthOfText == 0:
#         pass
#     else:
#         print("")
#         print(f"AI : {Text}")
#         print("")
#         Data = str(Text)
#         xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
#         driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
#
#         if lengthOfText >= 10:
#             sleep(4)
#
#         elif lengthOfText >= 40:
#             sleep(6)
#         elif lengthOfText >=55:
#             sleep(8)
#         elif lengthOfText >=70:
#             sleep(10)
#         elif lengthOfText >=100:
#             sleep(13)
#         elif lengthOfText >=120:
#             sleep(14)
#         else:
#             sleep(3)
#
