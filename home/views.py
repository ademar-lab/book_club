from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import forms
from . import models

# Create your views here.
def index(request):
    user = request.user
    books = models.Book.objects.filter(owner=user.id)
    context = {'books':books}
    return render(request, 'home/index.html', context)

def check_book_owner(request, book_id):
    """ Returns a 404 Error if the user doesn't own the book."""
    book = models.Book.objects.get(id=book_id)
    if request.user != book.owner:
        raise Http404()
    else:
        return True

# Book related views
@login_required
def book(request, book_id):
    """Detail view of the Book model.""" 
    if check_book_owner(request, book_id):
        book = models.Book.objects.get(id=book_id)
        chapters = models.Chapter.objects.filter(book_id=book_id)
        
        context = {'book':book, 'chapters':chapters}
        return render(request, 'home/book.html', context)

@login_required
def new_book(request):
    if request.method != 'POST':
        form = forms.BookForm()
    else:
        form = forms.BookForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'home/new_book.html', context)

@login_required
def delete_book(request, book_id):
    if check_book_owner(request, book_id):
        book = get_object_or_404(models.Book, id=book_id)
        
        if request.method == 'POST':
            book.delete()
            return redirect('/')
        
        context = {'book':book}
        return render(request, 'home/delete_book.html', context)

@login_required
def edit_book(request, book_id):
    book = models.Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = forms.BookForm(instance=book)
    else:
        form = forms.BookForm(instance=book, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form, 'book':book}
    return render(request, 'home/edit_book.html', context)

# Chapter related views        
@login_required
def new_chapter(request, book_id):
    if check_book_owner(request, book_id):
        book = models.Book.objects.get(id=book_id)

        if request.method != 'POST':
            form = forms.ChapterForm()
        else:
            form = forms.ChapterForm(data=request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.book = book
                new_form.save()
                return redirect(f'/book/{book_id}')
        
        context = {'form':form, 'book':book}
        return render(request, 'home/new_chapter.html', context)

@login_required
def delete_chapter(request, chapter_id, book_id):
    if check_book_owner(request, book_id):
        chapter = get_object_or_404(models.Chapter, id=chapter_id)
        book = models.Book.objects.get(id=book_id) 
        
        if request.method == 'POST':
            chapter.delete()
            return redirect(f'/book/{book_id}')
        
        context = {'chapter':chapter, 'book':book}
        return render(request, 'home/delete_chapter.html', context)

def edit_chapter(request, chapter_id, book_id):
    chapter = models.Chapter.objects.get(id=chapter_id)
    book = models.Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = forms.ChapterForm(instance=chapter)
    else:
        form = forms.ChapterForm(instance=chapter, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/book/{book_id}')

    context = {'form':form, 'chapter':chapter, 'book':book}
    return render(request, 'home/edit_chapter.html', context)