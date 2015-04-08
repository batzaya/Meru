from django.shortcuts import render
from .models import Menu


def index(request):
    menu_list = Menu.objects.values_list('name_en', flat=True)
    context = {"menu_list": menu_list}
    return render(request, 'introduction/index.html', context)

def index_mn(request):
    menu_list = Menu.objects.values_list('name_mn', flat=True)
    context = {"menu_list": menu_list}
    return render(request, 'introduction/index.html', context)

# Create your views here.
