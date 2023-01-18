from django.urls import path
from . import views
from .views import create_room,room_delete

urlpatterns = [
    path('',views.rooms, name='rooms'),
    path('room/<int:pk>/delete/', room_delete, name='room_delete'),
    path('create_room/',views.create_room,name="create_room"),
    path('<slug:slug>/',views.room, name='room'),
    
]