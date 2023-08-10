from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')
    total_sales_amount = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)
    rating = models.FloatField()

    def __str__(self):
        return self.name
    

class Order_detail(models.Model):
    customer_name = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.FloatField()
 
   