from django.urls import path, include
from .import views

app_name = "home"
urlpatterns = [
    path('', views.index, name="index"),
    path('new_book', views.new_book, name='new_book'),
    path('book/<int:book_id>', views.book, name='book'),
    path('new_chapter/<int:book_id>', views.new_chapter, name='new_chapter'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
]