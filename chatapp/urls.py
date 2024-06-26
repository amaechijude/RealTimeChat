from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('chat', views.chat, name='chat'),
    path('index', views.index, name='index'),
    # path('<str:room_name>/<str:username>', views.chatroom, name='chatroom'),
    
]
