from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def books(request):
    return render(request, "books.html")

def check(request):
    return HttpResponse("текшеруу")
