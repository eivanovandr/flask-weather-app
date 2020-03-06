import requests
import os
from geopy.geocoders import Nominatim

def getWeather(city):

    #get city latitude and longitude or None object if city is not real
    geolocator = Nominatim(user_agent="myWeatherApp")
    location = geolocator.geocode(city)

    #if city not real quit function
    if location == None:
        return False



    #dark sky api
    key = os.environ.get('API_KEY')


    link = 'https://api.darksky.net/forecast/'

    #get data from api
    url = link + key + '/' + str(location.latitude) + ',' + str(location.longitude) + '?exclude=[minutely, hourly, daily, alerts, flags]'

    #try to make request or quit the function
    try:
        #send request
        r = requests.get(url)
        data = r.json()

        
        #get temperature, icon from data
        weatherData = {
            'summary' : data['currently']['summary'],
            'temperature' : data['currently']['temperature'],
            'icon' : data['currently']['icon']
        }

        return weatherData
    except:
        return False
