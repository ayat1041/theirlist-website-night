from django.urls import path
from . import views
from .views import room_form

urlpatterns = [
    path('',views.rooms, name='rooms'),
    path('<slug:slug>/',views.room, name='room'),
    path('create_room/',views.room_form,name="create_room"),
]