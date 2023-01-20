from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Message
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect, render, HttpResponse,HttpResponseRedirect
from django.views.generic import UpdateView,TemplateView,ListView,DetailView,CreateView,DeleteView
from django.utils.text import slugify
from .forms import RoomForm
from django.db.models import QuerySet
from django.contrib import messages
from django.utils import timezone

# @login_required
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.none()
#     if request.method == 'POST':
#         password = request.POST.get('password')
#         if room.password == password:
#             messages = Message.objects.filter(room=room) [0:25]
#             #messages.success(request, 'Access granted')
#             return render(request, 'rooms/room.html', {'room': room, 'messages': messages})
#         else:
#             #messages.error(request, 'Access denied: Incorrect Password')
#             return redirect('rooms')
#     else:
#         return render(request, 'rooms/password.html', {'room': room})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    if request.method == 'POST':
        password = request.POST.get('password')
        if room.password == password:
            messages = Message.objects.filter(room=room)[0:25]
            return render(request, 'rooms/room.html', {'room': room, 'messages': messages})
        else:
            return redirect('rooms')
    else:
        return render(request, 'rooms/password.html', {'room': room})

# @login_required
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room) [0:25]
#     return render(request, 'rooms/room.html', {'room': room, 'messages': messages})



@login_required
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.user != room.user:
        return redirect('forbidden')
    if request.method == 'POST':
        room.delete()
        return redirect('rooms')
    return render(request, 'rooms/room_confirm_delete.html', {'room': room})


# @login_required
# def create_room(request):
#     if request.method == 'POST':
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             room = form.save(commit=False)
#             room.user = request.user
#             room.slug = slugify(f"{room.name}{room.created}")
#             room.save()
#             return redirect('rooms')
#     else:
#         form = RoomForm()
#     return render(request, 'rooms/create_room.html', {'form': form})

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('rooms')
    else:
        form = RoomForm()
    return render(request, 'rooms/create_room.html', {'form': form})

@login_required
def rooms(request):
    rooms = Room.objects.all().order_by('-created')
    return render(request, 'rooms/rooms.html', {'rooms' : rooms})



