from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('NEW', 'Новый'),
        ('PROCESSING', 'В обработке'),
        ('SHIPPING', 'Доставляется'),
        ('DELIVERED', 'Доставлен'),
        ('CANCELED', 'Отменён'),
    )
    customer_name= models.CharField('Имя покупателя', max_length=20)
    phone= models.CharField('Номер телефона', max_length=20)
    address = models.CharField('Адрес доставки', max_length=100)
    product_name= models.CharField('Название товара', max_length=100)
    product_image= models.ImageField('Фото товара', upload_to='orders/', blank=True)
    quantity = models.PositiveIntegerField('Количество', default=1)
    price = models.DecimalField('Цена за штуку (сом)', max_digits=10, decimal_places=2)
    status= models.CharField('Статус заказа', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at= models.DateTimeField(auto_now_add=True)
    
@property 
def total_price(self):
    return self.price * self.quantity

def __str__(self):
    return f'Заказ №{self.id} - {self.product_name}'