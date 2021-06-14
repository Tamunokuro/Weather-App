from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import pandas as pd
import requests

def index(request):
    df = pd.read_csv('worldcities.csv')
    if 'city' in request.GET:
        city = request.GET['city']  
        if df[df['city_ascii'] == city]['city_ascii'].any():
            lat = df[df['city_ascii'] == city]['lat'] 
            lon = df[df['city_ascii'] == city]['lng']
            url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"
            querystring = {"unit_system": "si","fields": ["precipitation", "precipitation_type", "temp", "cloud_cover", "wind_speed","weather_code"],"lat":lat, "lon":lon}
            headers = {
           'x-rapidapi-key': "d0efc7da3dmshc3aed05aec89ac7p167adbjsna5c311da2e10",
           'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com"
            }
            response = requests.request("GET",url,headers=headers,params=querystring).json()
            context = {'cloud_cover': response['cloud_cover']['value'],'city_name':city,'temp': response['temp']['value'],'weather_code': response['weather_code']['value'],'wind_speed': response['wind_speed']['value'],'precipitation_type': response['precipitation_type']['value']} 
            print(context)
            return render(request, 'weatherforecast/index.html', context)  
        else:
           return HttpResponseRedirect(reverse('home'))
    else:
        context = {}
        return render(request, 'weatherforecast/index.html', context)
