from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def index(request):

    template = 'index.html'
    return render(request, template)

def home(request):
    form = RoomForm()
    forma = AreaForm()

    context = {
        "form": form,
        "forma": forma,
    }

    return render(request, 'home.html', context)