from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from states.models import State
from .search_choices import bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    states = State.objects.order_by('name')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list =  queryset_list.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list =  queryset_list.filter(city__iexact=city)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list =  queryset_list.filter(state__name_short__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list =  queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list =  queryset_list.filter(price__lte=price)
    context = {
        'listings': queryset_list,
        'states': states,  
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
