from django.shortcuts import render


def index(request):
    return render(request, 'products/home.html', context=None)
