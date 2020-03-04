from flask import Flask
from flask import render_template
from flask import request
import getWeather

#creating flask web app class
app = Flask(__name__)


#listen for routes
#listen for index route
@app.route('/')
def index_page():
        return render_template('index.html')

#listen for forecast route
@app.route('/forecast', methods=['GET'])
def forecast_page():


    #get city name from html form request
    city = str(request.args['city_input'])
    weatherData = getWeather.getWeather(city)

    #if city is real
    if weatherData != False:
        return render_template('forecast.html', temperature=weatherData['temperature'], icon=weatherData['icon'], summary=weatherData['summary'], city=city.title())


    #if city is not real
    return render_template('index.html')
