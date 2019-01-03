import requests
from django.shortcuts import render

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a961a2cacbe8a7fd5474db43e2455a3c'
	city = 'Youssoufia'

	r = requests.get(url.format(city)).json()

	city_weather = {
		'city' : city,
		'temperature' : r['main']['temp'],
		'description' : r['weather'][0]['description'],
		'icon' : r['weather'][0]['icon'],
	}

	context = {'city_weather' : city_weather}

	return render(request, "weather/weather.html", context)