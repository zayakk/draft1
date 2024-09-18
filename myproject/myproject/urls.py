from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from myapp.views import current_time

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', current_time),
    path('', RedirectView.as_view(url='/time/')), 
]
