from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "home.html", {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('books:index')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('books:index')
        messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('books:index')

@login_required
def book_add(request):
    if request.method == 'POST':
        try:
            Book.objects.create(
                title=request.POST['title'],
                author=request.POST['author'],
                year=int(request.POST['year']),
                rating=float(request.POST['rating']),
                description=request.POST['description'],
                user=request.user
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

@login_required
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.user != request.user:
        messages.error(request, "You can't edit this book.")
        return HttpResponseForbidden("You can't edit this book.")
    
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

@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.user != request.user:
        messages.error(request, "You can't delete this book.")
        return HttpResponseForbidden("You can't delete this book.")
    
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('books:index')
    return render(request, "book_delete.html", {"book": book})
    