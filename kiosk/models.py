from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
  Menucode = models.IntegerField(null=False)
  Menu_kor = models.CharField(max_length=10, null=False)
  Price = models.IntegerField(null=False)

  def __str__(self):
      return self.Menu_kor

class Jumun(models.Model):
  
  Menucode = models.ForeignKey(Recipe, on_delete=models.CASCADE,null=False)
  Count = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], null=False)
  Customer = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
  Jumun_date = models.DateTimeField(null=False)
  Today_jumun_order = models.IntegerField(null=False)

