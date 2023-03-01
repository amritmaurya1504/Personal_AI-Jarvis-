from Body.Speak import Speak
import requests



def Location():
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        response = requests.get('https://ipinfo.io/json')
        resData = response.json()
        city = resData['city']
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        country = geo_data['country']
        print(country)
        Speak(f"sir i am not sure, but i think we are in {city}, city in {country}")
    except Exception as e:
        Speak("sorry sir, due to network issue i am not able to find where we are.")
        pass


