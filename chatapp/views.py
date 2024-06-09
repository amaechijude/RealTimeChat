from django.shortcuts import render, redirect
from .models import Room, Message
# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_name = request.POST['room']
        
        try:
            get_room = Room.objects.get(room_name=room_name)
        except Room.DoesNotExist:
            new_room = Room(room_name=room_name)
            new_room.save()
        finally:
            return redirect('chatroom', room_name=room_name, username=username)
        
    template = 'index.html'
    return render(request, template)


def chatroom(request, room_name, username):
    if request.method == 'POST':
        chat = request.POST['chat']
        room_name = request.POST['room_name']
        room = Room.objects.get(room_name=room_name)
        new_chat = Message.objects.create(room=room, author=username, content=chat)
        new_chat.save()
        #return render('chatroom')
    room = Room.objects.get(room_name=room_name)
    chats = Message.objects.filter(room=room)
    
    context = {
        "chats": chats,
        "username": username,
        "room": room,
    }
    return render(request, 'chat.html', context)
