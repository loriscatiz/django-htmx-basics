from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from core.forms import MyForm
from core.models import Country, State, City

# Create your views here.

class CountryView(View):
    def get(self, request):
        form = MyForm()
        countries = Country.objects.all()

        context = {
            'countries': countries,
            'form': form
        }


        return render(request, 'country.html', context)


class HxStateView(View):
    def get(self, request):
        country_id = request.GET.get('country')
        states = State.objects.filter(country_id=country_id)
        return render(request, 'state_options.html', {'states': states})
    

class HxCityView(View):
    def get(self, request):
        state_id = request.GET.get('state')
        cities = City.objects.filter(state_id=state_id)
        return render(request, 'city_options.html', {'cities': cities})
    
