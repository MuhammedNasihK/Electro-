from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField()
    slug = models.CharField()

    def __str__(self):
        return self.name
    

class Brands(models.Model):
    name = models.CharField()
    description = models.TextField()
    logo = models.ImageField(upload_to='brand_logo/')

class Products(models.Model):
    name = models.CharField()
    slug = models.CharField()
    description = models.TextField()
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.OneToOneField(Brands,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

