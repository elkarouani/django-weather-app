import requests
from django.shortcuts import render

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a961a2cacbe8a7fd5474db43e2455a3c'
	city = 'Youssoufia'

	r = requests.get(url.format(city))
	print(r.text)

	return render(request, "weather/weather.html")