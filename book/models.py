from django.db import models

class Book(models.Model):
    GENRE_BOOK = (
            ('Роман', 'Роман'),
            ('Поэзия', 'Поэзия'),
            ('Фантастика', 'Фантастика'),
            ('Детектив', 'Детектив'),
            ('Научная литература', 'Научная литература'),
        )  
    
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор')
    description = models.TextField(blank=True, verbose_name='Описание')
    cover = models.ImageField(upload_to='books/', verbose_name='Обложка')
    genre = models.CharField(max_length=50, choices=GENRE_BOOK, verbose_name='Жанр')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена (сом)')
    isbn = models.CharField(max_length=20, blank=True, verbose_name='ISBN')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
    def __str__(self):
        return self.title