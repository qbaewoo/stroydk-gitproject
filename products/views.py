from django.shortcuts import render
from items.models import Item

def home(request):
    popular_items = Item.objects.order_by('-created_date').filter(is_popular=True)
    data = {
        'popular_items':popular_items,
    }
    return render(request, 'products/home.html',data)


def about(request):
    return render(request, 'products/about.html')


def delivery(request):
    return render(request, 'products/delivery.html')