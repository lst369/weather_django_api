import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    appid ='329f36eee051dc1c0c2691fc1e4e13c0'
    url ='https://api.openweathermap.org/data/2.5/weather?q={}&&units=metric&appid=' + appid
    
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_cities = []
    
    cities = City.objects.all()

    for city in cities:        
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
    }
    
    return render(request, 'weather/index.html', context)