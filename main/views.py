from django.shortcuts import render, HttpResponse, redirect
from .models import Books, ToDo



def homepage(request):
    return render(request, "index.html")


def books(request):
    todo_list = Books.objects.all()
    return render(request, "books.html", {"todo_list": todo_list})



def add_book(request):
    form = request.POST
    book = Books(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["date"][:10]

    )

    book.save()

    return redirect(book)



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

def add_book(request):
    form = request.POST
    text = form["title"]
    books = Books(text=text)
    books.save()
    return redirect(books)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test1)

def delete_books(request, id):
    books = Books.objects.get(id=id)
    books.delete()
    return redirect(books)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test1)

def mark_books(request, id):
    books = Books.objects.get(id=id)
    books.is_favorite = True
    books.save()
    return redirect(books)    

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test1)

def unmark_books(request, id):
    books = Books.objects.get(id=id)
    books.is_favorite = False
    books.save()
    return redirect(books)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test1)

def mark_books(request, id):
    books = Books.objects.get(id=id)
    books.is_favorite = True
    books.save()
    return redirect(books)
