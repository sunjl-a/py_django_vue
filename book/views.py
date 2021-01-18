from django.shortcuts import render
from django.http.response import JsonResponse


# Create your views here.
def home(request):
    return render(request, "index.html")


def books(request):
    books = [
        {"id": 1, "title": "python", "price": 88.12},
        {"id": 2, "title": "Flask", "price": 89.34},
        {"id": 3, "title": "Django", "price": 90.56},
    ]
    return JsonResponse(books, safe=False)
