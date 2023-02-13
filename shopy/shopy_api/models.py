from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.IntegerField()
    image = models.ImageField(upload_to='games/')

    class Meta:
        db_table  = 'products'
        def __str__(self):
            return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)
    freight = models.DecimalField(max_digits=10,  decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10,  decimal_places=2, null=True, blank=True)


