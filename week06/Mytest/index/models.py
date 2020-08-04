from django.db import models

# Create your models here.
class Type(models.Model):
    typename = models.CharField(max_length = 20)

class Person(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
