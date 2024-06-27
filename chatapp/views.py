from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import *
from .forms import *
from .filters import RoomFilter

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            new_profile = Profile.objects.create(user=user, pID=user.id)
            new_profile.save()
            messages.info(request, "Registration successful, Now login")
            return redirect('signin')
    form = RegisterForm()
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'login.html')

def home(request):
    if request.method == 'POST':
        room_name = str(request.POST['room']).lower()
        user = request.user
        room = Room.objects.create(room_name=room_name, user=user)

        messages.info(request, 'room created')
        return redirect('home')

            

    form = RoomForm()
    forma = AreaForm()
    room_filter = RoomFilter(request.GET, queryset=Room.objects.all())
    context = {
        "form": form,
        "forma": forma,
        'filter': room_filter,
    }

    return render(request, 'home.html', context)


def chat(request, pk):
    roo
    return render(request, 'chat.html')


def what(request):
    return render(request, 'form.html')

def index(request):
    return redirect('home')
