from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Room(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    # slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)
    
    def __str__(self):
        return self.name  + "  |  " + self.user.username
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + self.created.day)
        super(Room,self).save(*args, **kwargs)   

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messsages', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, related_name='messsages', on_delete=models.CASCADE)
    user = models.ForeignKey(User,models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',) 