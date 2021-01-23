from django.shortcuts import render, HttpResponse
from .models import Books, ToDo



def homepage(request):
    return render(request, "index.html")


def books(request):
    todo_list = Books.objects.all()
    return render(request, "books.html", {"todo_list": todo_list})



def check(request):
    return HttpResponse("текшеруу")

def test1(request):
    todo_list = ToDo.objects.all()
    return render(request, "test1.html", {"todo_list": todo_list}) 
