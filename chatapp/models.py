from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from shortuuidfield import ShortUUIDField
# Create your models here.
User = get_user_model()

class Profile(models.Model):
    pID = ShortUUIDField(primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = ResizedImageField(quality=70, upload_to='media/profile', blank=True, null=True)

    def __str__(self):
        res = f"{self.first_name}"
        return res

# class Area(models.Model):
#     breadth = models.PositiveIntegerField()
#     width = models.PositiveIntegerField()
#     output = models.GeneratedField(expression=models.F("breadth") * models.F("width"),
#                                  output_field=models.IntegerField(),
#                                  db_persist=True)

class Room(models.Model):
    room_name = models.CharField(max_length=150, unique=True, primary_key=True)
    avatar = ResizedImageField(quality=70, upload_to='media/room', blank=True, null=True)
    members = models.ManyToManyField(Profile, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.room_name
    
    

class RoomChat(models.Model):
    mID = ShortUUIDField(primary_key=True, unique=True, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=300, blank=False)
    image = ResizedImageField(blank=True, null=True, quality=70, upload_to="media/chats/images")
    file = models.FileField(blank=True, null=True, upload_to='media/chats/files')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        conc = f"{self.room} ___ {self.author}"
        return conc
