from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
  menucode = models.CharField(max_length=5, null=False)
  menu_name = models.CharField(max_length=10, null=False)
  price = models.IntegerField(null=False)

  def __str__(self):
      return self.menu_name

class Jumun(models.Model):
  
  menucode = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  count = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
  customer = models.ForeignKey(User,on_delete=models.CASCADE)
  jumun_date = models.DateTimeField()
  today_jumun_order = models.IntegerField()

