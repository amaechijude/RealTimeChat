from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    # path('<str:room_name>/<str:username>', views.chatroom, name='chatroom'),
    
]