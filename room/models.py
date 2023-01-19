from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import now

class Room(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255,null=True, choices=[('Movie', 'Movie'), ('Music', 'Music'), ('Book', 'Book'), ('Others', 'Others')])
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(default=now, null=True)
    
    def __str__(self):
        return self.name  + "  |  " + self.user.username
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}{self.created}")
        super(Room, self).save(*args, **kwargs)        

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messsages', on_delete=models.CASCADE)
    user = models.ForeignKey(User,models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',) 