from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Drink(models.Model):
    name = models.CharField(max_length=225)
    recipe = models.TextField()
    summary = models.TextField()
    categories = models.ManyToManyField('Category', related_name='drinks')
    image = models.ImageField(upload_to='drinks/%Y/%m')