from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from .models import SpiritualBook

def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def resources(request):
    # Fetch all SpiritualBook objects
    books = SpiritualBook.objects.all()
    return render(request, 'resources.html', {'books': books})

def bibleverse(request):
    return render(request, 'bibleverse.html')

def download_book(request, book_id):
    book = get_object_or_404(SpiritualBook, pk=book_id)
    
    # Debugging: Print the absolute path to the file
    print(book.document.path)

    # Open the file in binary mode for streaming
    with open(book.document.path, 'rb') as file:
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename="{book.title}.pdf"'
        return response
    
def upload_file(request):
    pass


def login(request):
    return render(request, 'login.html')

def planets(request):
    return render(request, 'planets.html')

def upload(request):
    return render(request, 'upload.html')

def prayerrequests(request):
    return render(request, 'prayer-requests.html')

def sermons(request):
    return render(request, 'sermons.html')
def spiritofprophecy(request):
    return render(request, 'spiritofprophecy.html')
def trinity(request):
    return render(request, 'trinity.html')