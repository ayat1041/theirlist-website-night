from email.policy import default
from enum import auto
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy,reverse
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
#alllist
from django.db.models.signals import post_save
from django.dispatch import receiver

class MusicList(models.Model):
    title = models.CharField(max_length=120)
    genre = models.ManyToManyField('MusicGenre')
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')
    type = models.CharField(max_length=10,default="Music")
    spoiler_choices = [(False, 'No'),(True, 'Yes')]
    spoiler = models.BooleanField(default=False,null=True, choices = spoiler_choices)
    slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)


    def __str__(self):
        return f'{self.title}|{self.creator}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.posted))
        super(MusicList,self).save(*args, **kwargs)



class MusicGenre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class BookList(models.Model):
    title = models.CharField(max_length=120)
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    genre = models.ManyToManyField('BookGenre')
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')
    type = models.CharField(max_length=10,default="book")
    spoiler_choices = [(False, 'No'),(True, 'Yes')]
    spoiler = models.BooleanField(default=False,null=True, choices = spoiler_choices)
    slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)


    def __str__(self):
        return f'{self.title}|{self.creator}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.posted))
        super(BookList,self).save(*args, **kwargs)

class BookGenre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class List(models.Model):
    title = models.CharField(max_length=120)
    genre = models.ManyToManyField('Genre')
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')
    type = models.CharField(max_length=10,default="Movie")
    spoiler_choices = [(False, 'No'),(True, 'Yes')]
    spoiler = models.BooleanField(default=False,null=True, choices = spoiler_choices)
    slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)


    def __str__(self):
        return f'{self.title}|{self.creator}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.posted))
        super(List,self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(blank=True, default='', upload_to='profiles_pics')
    fav_music_genre = models.ManyToManyField('MusicGenre')
    fav_Book_genre = models.ManyToManyField('BookGenre')
    fav_movie_genre = models.ManyToManyField('Genre')
    
    def __str__(self):
        return self.user.username + " | bio : " + self.bio

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    List = models.ForeignKey(List, models.CASCADE)
    comment = models.TextField(max_length=250)
    type = models.TextField(max_length=10,default="movie")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment+ " | " + self.user.username

class BookReview(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    BookList = models.ForeignKey(BookList, models.CASCADE)
    comment = models.TextField(max_length=250)
    type = models.TextField(max_length=10,default="book")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment+ " | rating : " + str(self.rate) + " | " + self.user.username

class MusicReview(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    MusicList = models.ForeignKey(MusicList, models.CASCADE)
    comment = models.TextField(max_length=250)
    type = models.TextField(max_length=10,default="music")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment+ " | rating : " + str(self.rate) + " | " + self.user.username

class Starr(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    list = models.ForeignKey(List,models.CASCADE)
    rate = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ["user", "list"]

    def __str__(self):
        return self.user.username + " | " + self.list.title + " | " + str(self.rate)  

class MusicStarr(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    list = models.ForeignKey(MusicList,models.CASCADE)
    rate = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ["user", "list"]

    def __str__(self):
        return self.user.username + " | " + self.Musiclist.title + " | " + str(self.rate)  

class BookStarr(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    list = models.ForeignKey(BookList,models.CASCADE)
    rate = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ["user", "list"]

    def __str__(self):
        return self.user.username + " | " + self.Booklist.title + " | " + str(self.rate)  