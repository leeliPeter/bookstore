from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:book_id>/delete/', views.book_delete, name='book_delete'),
] 