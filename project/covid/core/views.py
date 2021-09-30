from django.shortcuts import render
import requests
import pprint

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f8e0630aa7mshd6a04f0e8a7606ap1a041ejsn921f92f099e6"
    }

response = requests.request("GET", url, headers=headers).json()
response = response["response"]

countries = []

countries = [ dato['country'] for dato in response]#lista po compresion
countries.sort()
# Create your views here.
def home(request):
    if request.method=='POST':
        pais = request.POST['selectedcountry']
        for i in response:
            if pais == i['country']:
                new = i['cases']['new'] if i['cases']['new'] else '0'
                active = i['cases']['active'] if i['cases']['active'] else '0'
                critical = i['cases']['critical'] if i['cases']['critical'] else '0'
                recovered = i['cases']['recovered'] if i['cases']['recovered'] else '0'
                total = i['cases']['total'] if i['cases']['total'] else '0'
                deaths = int(total) - int(active) - int(recovered)
        context = {
            'new': new,
            'active': active,
            'critical': critical,
            'recovered': recovered,
            'total': total,
            'deaths': deaths,
            'pais' : pais,
            'countries': countries,
        }
        return render(request, 'core/index.html', context=context)
    return render(request, 'core/index.html', {'countries':countries})
