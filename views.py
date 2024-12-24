from django.shortcuts import render
import requests
from django.contrib import messages

# Create your views here.

def index(request):
    city = 'kathmandu'
    if 'city' in request.POST:

        city=request.POST['city']
    
    else:
        city = 'kathmandu'

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e2b45374cea69dbd11015d827cfe79a2"
    parms={'units':'metric'}
    
    try:
        data=requests.get(url,parms).json()
        temp=data['main']['temp']
        icon=data['weather'][0]['icon']
        desc=data['weather'][0]['description']
        wind=data['wind']['speed']
        hum=data['main']['humidity']
            
        return render(request, 'index.html',{'temp':temp,'city':city , 'icon':icon,'desc':desc , 'wind':wind, 'hum':hum, })
    except:
        data=requests.get
        temp=0
        desc='No Data Found'
        messages.error(request,"NO Data")

        return render(request, 'index.html',{'temp':temp,'desc':desc,'city':city})