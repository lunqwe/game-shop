from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, default='Название не указано')
    article = models.CharField(max_length=255, default='0000')
    description = models.TextField()
    price = models.CharField(max_length=255, default='Цена не указана')

    def __str__(self):
        return f'({self.article}) {self.title}'