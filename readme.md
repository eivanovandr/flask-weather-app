Simple Python Weather App - ready for deployment on Heroku

Hosted on Heroku :  [https://flask-weather-application.herokuapp.com/](https://flask-weather-application.herokuapp.com/)

In order to use you need DarkSky API_KEY in the Config Vars

How to use: pyhton -m venv venv  
source venv/bin/activate  
pip install --upgrade -r requirements.txt  
export API_KEY = your DarkSky API_KEY  
flask run

- Technologies used:  
	- Backend/Server:  
		- Python: 
			- Flask 
			- requests 
			- geopy 
			 - os 
			 - gunicorn  
	- Frontend:  
		- HTML, CSS, JS 
		- skycons.js
skycons.js
