from django.shortcuts import render
from django.http import HttpResponse
from .models import Board  # make sure your Board model is imported

def home(request):
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})
