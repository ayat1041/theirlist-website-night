from django.contrib import admin
from app.models import Feedback,Genre,List,MusicGenre,MusicList,BookGenre,BookList,Review,MusicReview,BookReview,Profile,Starr,MusicStarr,BookStarr



admin.site.register(MusicGenre)
admin.site.register(MusicList)
admin.site.register(BookGenre)
admin.site.register(BookList)
admin.site.register(Genre)
admin.site.register(List)
admin.site.register(Review)
admin.site.register(MusicReview)
admin.site.register(BookReview)
admin.site.register(Profile)
admin.site.register(Starr)
admin.site.register(MusicStarr)
admin.site.register(BookStarr)
admin.site.register(Feedback)