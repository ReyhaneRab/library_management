from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from .forms import BookForm
# Create your views here.


def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_create_update(request, pk=None):
    if pk:
        book = get_object_or_404(Books, pk=pk)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/book_form.html', {'form': form})
