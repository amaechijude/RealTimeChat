from django.urls import path
from . import views


urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('', views.home, name='home'),
    path('chat/<str:pk>', views.chat, name='chat'),
    path('create/room', views.create_room, name='create_room'),
    path('join/room', views.joinroom, name="joinroom"),
    
]
