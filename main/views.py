from django.shortcuts import render, HttpResponse
from .models import Books


def homepage(request):
    return render(request, "index.html")


def books(request):
    todo_list = Books.objects.all()
    return render(request, "books.html", {"todo_list": todo_list})



def check(request):
    return HttpResponse("текшеруу")
