from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
# Create your models here.
User = get_user_model()

class Profile(models.Model):
    pID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = ResizedImageField(quality=70, upload_to='media/profile', blank=True, null=True)

class Area(models.Model):
    breadth = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    output = models.GeneratedField(expression=models.F("breadth") * models.F("width"),
                                 output_field=models.IntegerField(),
                                 db_persist=True)

class Room(models.Model):
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    room_name = models.CharField(max_length=50, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room_name
    
    

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = ResizedImageField(blank=True, quality=70, upload_to="media/chats/images", null=True)
    file = models.FileField(blank=True, null=True, upload_to='media/chats/files')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        conc = f"{self.room} ___ {self.author}"
        return conc
