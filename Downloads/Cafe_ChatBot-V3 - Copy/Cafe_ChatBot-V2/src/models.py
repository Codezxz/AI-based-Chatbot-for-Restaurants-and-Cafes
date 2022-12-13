from django.db import models

# Create your models here.
class Order(models.Model):
    Order_Number = models.CharField(max_length=122)
    items = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.Order_Number

class Kitchen_Order(models.Model):
    Order_Number = models.CharField(max_length=122)
    items = models.CharField(max_length=122)
    paymentid = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.Order_Number