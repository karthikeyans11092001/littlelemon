from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.IntegerField(default=1)
    def __str__(self):
        return self.name
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    def __str__(self):
        return f'{self.customer_name} - Table {self.table_number}'
