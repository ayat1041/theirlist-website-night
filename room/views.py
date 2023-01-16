from django.shortcuts import render
from .models import Room, Message
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect, render, HttpResponse,HttpResponseRedirect
from django.views.generic import UpdateView,TemplateView,ListView,DetailView,CreateView,DeleteView


from .forms import RoomForm

def room_form(request, id):
    if request.method == 'POST':
        cf = RoomForm(request.POST or None)
        if cf.is_valid():
            name = request.POST.get('name')
            room = Room.objects.create(room = room, user = request.user, name = name)
            room.save()
            return redirect(room.get_absolute_url())
        else:
            cf = RoomForm()
        context ={
            'room_form':cf,
        }
        return render(request, 'rooms/create_room.html', context)

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms.html', {'rooms' : rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room) [0:25]
    return render(request, 'rooms/room.html', {'room': room, 'messages': messages})

