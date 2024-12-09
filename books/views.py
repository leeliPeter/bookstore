from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "home.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})

def book_add(request):
    if request.method == 'POST':
        try:
            Book.objects.create(
                title=request.POST['title'],
                author=request.POST['author'],
                year=int(request.POST['year']),
                rating=float(request.POST['rating']),
                description=request.POST['description']
            )
            messages.success(request, 'Book added successfully!')
            return redirect('books:index')
        except Exception as e:
            messages.error(request, f'Error adding book: {str(e)}')
            return render(request, "book_form.html", {
                "action": "Add",
                "book": {
                    "title": request.POST.get('title', ''),
                    "author": request.POST.get('author', ''),
                    "year": request.POST.get('year', ''),
                    "rating": request.POST.get('rating', ''),
                    "description": request.POST.get('description', '')
                }
            })
    return render(request, "book_form.html", {"action": "Add"})

def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        try:
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.year = request.POST['year']
            book.rating = request.POST['rating']
            book.description = request.POST['description']
            book.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('books:book_detail', book_id=book.id)
        except Exception as e:
            messages.error(request, f'Error updating book: {str(e)}')
            return render(request, "book_form.html", {"book": book, "action": "Edit"})
    return render(request, "book_form.html", {"book": book, "action": "Edit"})

def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('books:index')
    return render(request, "book_delete.html", {"book": book})
    