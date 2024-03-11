from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, default='unknown')
    article = models.CharField(max_length=255, default='unknown')
    description = models.TextField()
    price = models.CharField(max_length=255, default='unknown')
    display_type = models.CharField(max_length=255, default='constructor')
    image = models.ImageField(default='default.png')

    def __str__(self):
        return f'({self.article}) {self.title}'