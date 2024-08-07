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
            new_profile = Profile.objects.create(user=user)
            new_profile.save()
            messages.info(request, "Registration successful, Now login")
            return redirect('signin')
    form = RegisterForm()
    return render(request, 'signup.html', {"form": form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'login.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def home(request):
    form = RoomForm()
    room_filter = RoomFilter(request.GET, queryset=Room.objects.all())
    context = {
        "form": form,
        'filter': room_filter,
        }

    return render(request, 'home.html', context)


@login_required(login_url='signin')
def chat(request, pk):
    room = Room.objects.get(room_name=pk)
    members = room.members.all()
    chats = RoomChat.objects.filter(room=room)
    context = {
        "room": room,
        "chats": chats,
        "members": members,
        "user": request.user,
        }
    if request.user.profile in members:
        return render(request, 'chat.html', context)
    else:
        return redirect('home')


@login_required(login_url='signin')
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name').title()
        new_room = Room.objects.create(room_name=room_name)
        new_room.save()
        user = request.user
        profile = Profile.objects.get(user=user)
        new_room.members.add(profile)
        new_room.save()
        pk = room_name

        return redirect('chat', pk)


@login_required(login_url='signin')
def joinroom(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room = Room.objects.get(room_name=room_name)
        user = request.user
        profile = Profile.objects.get(user=user)
        pk = room_name

        if room.members.filter(pID=profile.pID).exists():
            room.members.remove(profile)
            room.save()
            return redirect('chat', pk)
        else:
            room.members.add(profile)
            room.save()
            return redirect('chat', pk)




