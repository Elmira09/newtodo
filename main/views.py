from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, "index.html")

<<<<<<< HEAD
def books(request):
    return render(request, "books.html")
=======
def test(request):
    todo_list = Books.objects.all()
    return render(request, "books.html", {"todo_list": todo_list})
>>>>>>> 384a2ba905e4c67b2195ee2ba53f930ca6fde4d0

def check(request):
    return HttpResponse("текшеруу")
