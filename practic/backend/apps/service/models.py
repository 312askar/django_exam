from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('Слаг', max_length=60, unique=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name
