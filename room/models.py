from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    user = models.ForeignKey(User,models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name  + "  |  " + self.user.username     

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messsages', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='messsages', on_delete=models.CASCADE)
    user = models.ForeignKey(User,models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',) 