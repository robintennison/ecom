from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default='', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='uploads/product/', null=True, blank=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=250, default='', blank=True )
    phone =  models.CharField(max_length=20, default='', blank=True )   
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product