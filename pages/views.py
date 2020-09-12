from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.models import Realtor
from states.models import State
from listings.search_choices import bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    states = State.objects.order_by('name')
    context = {
        'listings': listings,
        'states': states,  
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'pages/about.html', context)

