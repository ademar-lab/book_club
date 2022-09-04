from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models

# Create your views here.
def index(request):
    books = models.Book.objects.all()
    context = {'books':books}
    return render(request, 'home/index.html', context)

def new_book(request):
    if request.method != 'POST':
        form = forms.BookForm()
    else:
        form = forms.BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'home/new_book.html', context)

def book(request, book_id):
    book = models.Book.objects.get(id=book_id)
    chapters = models.Chapter.objects.filter(book_id=book_id)
    context = {'book':book, 'chapters':chapters}
    return render(request, 'home/book.html', context)

def new_chapter(request, book_id):
    book = models.Book.objects.get(id=book_id)

    if request.method != 'POST':
        form = forms.ChapterForm()
    else:
        form = forms.ChapterForm(data=request.POST)
        if form.is_valid():
            form.book = book_id
            form.save()
            return redirect(f'/book/{book_id}')
        
    context = {'form':form, 'book':book}
    return render(request, 'home/new_chapter.html', context)

def delete_book(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('/')
    
    context = {'book':book}
    return render(request, 'home/delete_book.html', context)