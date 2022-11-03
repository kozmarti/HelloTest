from django.shortcuts import render
from django.http import HttpResponse
import requests# Create your views here.
from . import services


def answer(request):
    response = requests.get('https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193')
    data = response.json()
    
    hour = "2022-11-03T06:00:00+00:00"

    print(services.prevision_for_hour(data, hour))
    print(services.min_estimation_and_hour(data))
    print(services.max_estimation_and_hour(data))
    print(services.average_prevision_for_day(data)) 
    return HttpResponse("")
