from django.forms import ModelForm
from .models import Book, Chapter

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'release_year']

class ChapterForm(ModelForm):
    class Meta():
        model = Chapter
        fields = ['subtitle', 'text']