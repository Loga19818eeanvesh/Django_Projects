from django.shortcuts import render

from django.http import HttpResponseNotFound

from django.db.models import Avg

from .models import Book

# Create your views here.

def index(request):
    all_books = Book.objects.all().order_by("-rating")
    noof_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))
    return render(request,'book_outlets/index.html',{
        "books" : all_books,
        "total_number_of_books" : noof_books,
        "average_rating" : avg_rating
    })

def book_detail(request,id):
    try:
        book = Book.objects.get(id=id)
        return render(request,'book_outlets/book_detail.html',{
            "book":book
        })
    except:
        return HttpResponseNotFound("Page not found!")

def book_detail_slug(request,slug):
    try:
        book = Book.objects.get(slug=slug)
        return render(request,'book_outlets/book_detail.html',{
            "book":book
        })
    except:
        return HttpResponseNotFound("Page not found!")

