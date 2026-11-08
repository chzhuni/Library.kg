from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Person(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    
    def __str__(self):
        return self.full_name
    
class Booking(models.Model):
    PLACE_CHOICES = (
        ('Музей', 'Музей'),
        ('Конный тур', 'Конный тур'),
        ('Театр', 'Театр')
    )
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Человек')
    place = models.CharField(max_length=50, choices=PLACE_CHOICES, verbose_name='Место для посещения')
    visit_date = models.DateField(verbose_name='Дата посещения')
    
    def __str__(self):
        return f'{self.person} - {self.place}'
    
class CategoryTour(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    
    def __str__(self):
        return self.name
    
class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название тура')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена (сом)')
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(CategoryTour, blank=True, verbose_name='Категории')

    def __str__(self):
        return self.title
    
class CommetTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name= 'Тур')
    text = models.TextField(blank=True, verbose_name='Комментарий')
    mark = models.PositiveIntegerField(
    default=5,
    validators=[MinValueValidator(1), MaxValueValidator(5)],
    verbose_name='Оценка (1-5)',
)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tour} - {self.mark}'
    
