from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from book.models import Book


def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('-id')
        return render(request, 'book_list.html', {'books': books})


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        return render(request, 'book_detail.html', {'book_id': book_id})

def about_me(request):
    return HttpResponse("<h1>Обо мне</h1><p>Меня зовут Николь, люблю активный образ жизни и читать книги</p>")

def my_favourite_writers(request):
    return HttpResponse("<p>1. Харуки Мураками</p><p>2. Ли Харпер</p><p>3. Агустина Бастеррика</p>")

def sayings_of_great_poets(request):
    return HttpResponse("""
        <img src="https://www.m24.ru/b/d/nBkSUhL2hFYum8mxPqzJrMCqzJ3z8Zin2XyQ2q2C_2OZcGuaSnvVjCdg4M4S7FjDvM_AtC_QbIk8W7zj1GdwKSGT_w=xOeenpwBu4eGNGh3jIHXBg.jpg"width="200">
        <p><b>Харуки Мураками</b></p>
        <p>“СМЕРТЬ – НЕ ПРОТИВОПОЛОЖНОСТЬ ЖИЗНИ, А ЕЕ ЧАСТЬ.”</p>
        
    
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREp_yfet91PHtgIq8DVN8Ojy0zqaE1aioFpYyDscvjpA&s" width="200">  
            <p><b>Ли Харпер</b></p>
            <p>«Мужество — это когда заранее знаешь, что ты проиграл, и все-таки берешься за дело и наперекор всему на свете идешь до конца. Побеждаешь очень редко, но иногда...»</p> 
            
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrd7jCaK0sunJHQP1fSG9rQ2Na9EOKM9bmqmvcKXBDnJVtn-2WCWUQRU7zFqHR6crNUJb2UdaZZEff8N91lxSZ3aSSlwtgPaEbKLI_pyeg&s=10" width="200">
            <p><b>Агустина Бастеррика</b></p>  
            <p>«Будь мы все чисты и непорочны, наша жизнь представляла бы из себя сплошную серую унылость».</p>
             
    """)