from django.shortcuts import render

# Create your views here.
from fan_app.models import Roster


def index_view(request):
    return render(request, 'index.html')

def detail_view(request):
    roster = Roster.objects.all()
    return render(request, 'detail.html', {"roster": roster})

def about_me_view(request):
    return render(request, 'about_me.html')
