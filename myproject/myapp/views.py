from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
# Create your views here.

    
def current_time(request):
    # now = timezone.now()
    return HttpResponse(datetime.now())

