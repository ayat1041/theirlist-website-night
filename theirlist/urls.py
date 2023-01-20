from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('app.urls')),
    path('',RedirectView.as_view(url='home/all')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')), 
    # path('oauth/', include('social_django.urls', namespace='social')),
    path('rooms/',include('room.urls')),
] 
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
