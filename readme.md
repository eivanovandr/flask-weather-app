Simple Python Weather App - ready for deployment on Heroku

In order to use you need DarkSky API_KEY in the Config Vars

https://flask-weather-application.herokuapp.com/

venv - this folder need to be removed, I will remove it after first stable version

pyhton -m venv venv \
source venv/bin/activate \
pip install --upgrade -r requirements.txt \
export API_KEY = your DarkSky API_KEY \
flask run \
