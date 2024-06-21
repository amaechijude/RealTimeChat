from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ResizedImageField(quality=70, upload_to='media/profile')

class Area(models.Model):
    breadth = models.IntegerField()
    width = models.IntegerField()
    area = models.GeneratedField(expression=models.F("breadth") * models.F("width"),
                                 output_field=models.IntegerField(),
                                 db_persist=True)

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.room_name
    
    

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        conc = f"{self.room} ___ {self.author}"
        return conc