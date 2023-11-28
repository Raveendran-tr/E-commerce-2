from django.db import models
from shop.models import Product
# Create your models here.
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q


def search(request):
    products = None;
    query = None;
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    else:
        messages.error(request, "No such item is found")
    return render(request, 'search.html', {'query': query, 'products': products})




# Create your views here.
