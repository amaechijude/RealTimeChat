from django.db import models

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.room_name
    
    

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        conc = f"{self.room} ___ {self.author}"
        return conc