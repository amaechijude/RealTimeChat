from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


def index(request):

    template = 'index.html'
    return render(request, template)

def home(request):
    if request.method == 'POST':
        room_name = str(request.POST['room']).lower()
        user = request.user

        try:
            room = Room.objects.get(room_name=room_name)
            return 
        except:
            romm = Room.objects.create(room_name=room_name, user=user)
            return

    form = RoomForm()
    forma = AreaForm()

    context = {
        "form": form,
        "forma": forma,
    }

    return render(request, 'home.html', context)


def chat(request):
    return render(request, 'chat.html')


def what(request):
    return render(request, 'form.html')

