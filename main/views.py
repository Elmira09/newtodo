from django.shortcuts import render, HttpResponse, redirect
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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test1)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test1)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test1)

