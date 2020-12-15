# we can put all tables columns in one class

from django.db import models

# https://docs.djangoproject.com/en/3.1/topics/db/models/
class sql_human_Persons(models.Model):
    Persons_id=models.IntegerField()
    city=models.CharField(max_length=50)
    Persons_name=models.CharField(max_length=255)
    assets=models.IntegerField()
    is_alien=models.IntegerField()
    age=models.IntegerField()
    month_expense=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=4, decimal_places=2)
    email=models.CharField(max_length=255)
    active=models.IntegerField()
    order_date=models.DateField()

class human_talent(models.Model):
    Persons_id=models.IntegerField()
    english_spoken=models.CharField(max_length=3)