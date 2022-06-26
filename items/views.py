from django.shortcuts import render


def items(request):
    return render(request, 'items/items.html')


def detail(request, id):
    return render(request, 'items/detail.html')


def search(request):
    return render(request, 'items/search.html')