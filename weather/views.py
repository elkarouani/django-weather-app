import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a961a2cacbe8a7fd5474db43e2455a3c'

	if request.method == 'POST' :
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()

	weather_data = []

	for city in cities:
		r = requests.get(url.format(city)).json()

		city_weather = {
			'city' : city.name,
			'temperature' : fahrenheit_to_celsius(r['main']['temp']),
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}

		weather_data.append(city_weather)

	context = {'weather_data' : weather_data, 'form' : form}
	return render(request, "weather/weather.html", context)

def fahrenheit_to_celsius(fahrenheit):
	return int((fahrenheit - 32) * 5.0/9.0)