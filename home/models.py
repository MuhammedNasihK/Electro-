from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='brand_logo/')

    def __str__(self):
        return self.name 
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=250)
    description = models.TextField()
    specification = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')
    

class ProductVariant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    discount_price = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name}-{self.variant_name}"


class Attribute(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.attribute.name} : {self.attribute_value}"

class VariantAttribute(models.Model):
    product_variant = models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_variant} - {self.attribute_value}"






    