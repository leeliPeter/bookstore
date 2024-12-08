from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    books = [
        {
            "id": 1,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year": 1960,
            "rating": 4.8,
            "description": "A gripping and heart-wrenching tale of racial injustice in the Deep South."
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "rating": 4.7,
            "description": "A dystopian novel exploring the dangers of totalitarianism and extreme political ideology."
        },
        {
            "id": 3,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "rating": 4.4,
            "description": "A critique of the American Dream set in the Jazz Age."
        },
        {
            "id": 4,
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "year": 1813,
            "rating": 4.6,
            "description": "A romantic novel exploring themes of love, class, and social expectations."
        },
        {
            "id": 5,
            "title": "Moby-Dick",
            "author": "Herman Melville",
            "year": 1851,
            "rating": 4.2,
            "description": "An epic tale of obsession and revenge on the high seas."
        }
    ]
    return render(request, "home.html", {"books": books})
    
def book_detail(request, book_id):
    books = [
        {
            "id": 1,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year": 1960,
            "rating": 4.8,
            "description": "A gripping and heart-wrenching tale of racial injustice in the Deep South."
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "rating": 4.7,
            "description": "A dystopian novel exploring the dangers of totalitarianism and extreme political ideology."
        },
        {
            "id": 3,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year": 1925,
            "rating": 4.4,
            "description": "A critique of the American Dream set in the Jazz Age."
        },
        {
            "id": 4,
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "year": 1813,
            "rating": 4.6,
            "description": "A romantic novel exploring themes of love, class, and social expectations."
        },
        {
            "id": 5,
            "title": "Moby-Dick",
            "author": "Herman Melville",
            "year": 1851,
            "rating": 4.2,
            "description": "An epic tale of obsession and revenge on the high seas."
        }
    ]
    
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return HttpResponse("Book not found", status=404)
        
    return render(request, "book_detail.html", {"book": book})
    