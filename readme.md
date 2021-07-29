Python Weather Web App - ready for deployment on Heroku

Hosted on Vultr :  http://149.248.57.234:4000/

In order to use you need DarkSky API_KEY in the Config Vars

How to use:

$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade -r requirements.txt
$ export API_KEY=your DarkSky API_KEY
$ flask run

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

