from django.urls import path
from . import views


urlpatterns = [
    path('login', views.signin, name='login'),
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('chat/<str:pk>', views.chat, name='chat'),
    path('index', views.index, name='index'),
    path('what', views.what, name='what'),
    # path('<str:room_name>/<str:username>', views.chatroom, name='chatroom'),
    
]
