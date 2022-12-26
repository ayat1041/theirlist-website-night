from django.urls import path
from . import views
from .views import BookListUpdateView,MusicListUpdateView,ListUpdateView,MusicListDeleteView,BookListDeleteView,TheirListView,TheirDetailView,ListCreateView,ListDeleteView,TheirListMusicView,TheirListBookView,TheirDetailBookView,TheirDetailMusicView,ListCreateBookView,ListCreateMusicView
from django.contrib.auth.decorators import login_required

app_name = "app"

urlpatterns = [
    path('chat_room/',views.Chat.as_view(),name='chat'),
    path('about-us/',views.AboutUs.as_view(),name='about_us'),
    path('UserComments/',views.UserComments,name='UserComments'),
    path('edit-profile/',views.EditProfile.as_view(),name='edit_profile'),
    path('userposts/',views.userpost,name='userposts'),
    # path('about-us/',login_required(views.AboutUs.as_view()),name='about_us'),
    path('feedback/',views.Feedback.as_view(),name='feedback'),
    path('guidelines/',views.Guidelines.as_view(),name='guidelines'),
    path('', views.HomeView.as_view(),name='home'),
    path('list/',TheirListView.as_view(),name = 'list'),
    path('booklist/',TheirListBookView.as_view(),name = 'booklist'),
    path('musiclist/',TheirListMusicView.as_view(),name = 'musiclist'),
    path('list/<slug:slug>/', TheirDetailView.as_view(),name='list_detail'),
    path('booklist/<slug:slug>/', TheirDetailBookView.as_view(),name='booklist_detail'),
    path('musiclist/<slug:slug>/', TheirDetailMusicView.as_view(),name='musiclist_detail'),
    path('create_book_list/',ListCreateBookView.as_view(),name="book_create_list"),
    path('create_music_list/',ListCreateMusicView.as_view(),name="music_create_list"),
    path('create_list/',ListCreateView.as_view(),name="create_list"),
    path('delete_list/<slug:slug>',ListDeleteView.as_view(),name="delete_movie"),
    path('delete_musiclist/<slug:slug>',MusicListDeleteView.as_view(),name="delete_music"),
    path('delete_booklist/<slug:slug>',BookListDeleteView.as_view(),name="delete_book"),
    path('update_list/<slug:slug>',ListUpdateView.as_view(),name="update_list"),
    path('update_musiclist/<slug:slug>',MusicListUpdateView.as_view(),name="update_musiclist"),
    path('update_booklist/<slug:slug>',BookListUpdateView.as_view(),name="update_booklist"),
    path('search/',views.search, name='search'),
    path('film/',views.film, name='film'),
    path('film/<str:query>',views.film, name='film'),
    path('music/',views.music, name='music'),
    path('music/<str:query>',views.music, name='music'),
    path('book/',views.book, name='book'),
    path('book/<str:query>',views.book, name='book'),
    path('all',views.all, name='all'),
    path('create_comment',views.create_comment, name='create_comment'),
    path('create_musiccomment',views.create_musiccomment, name='create_musiccomment'),
    path('create_bookcomment',views.create_bookcomment, name='create_bookcomment'),
    path('create_starr',views.create_starr, name='create_starr'),
    path('create_musicstarr',views.create_musicstarr, name='create_musicstarr'),
    path('create_bookstarr',views.create_bookstarr, name='create_bookstarr'),
    
]