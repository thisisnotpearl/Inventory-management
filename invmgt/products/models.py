from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    category_type = [
        ('ST', 'Stationary'),
        ('LP', 'Laptops'),
        ('HP', 'Headphones'),
        ('MB', 'Mobile')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=2, choices=category_type)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    brand = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} from {self.brand}'