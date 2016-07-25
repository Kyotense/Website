from django.db import models
from django.utils import timezone
import datetime


class Company(models.Model):
	company_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="shop")
	def __str__(self):
		return self.company_name

# Create your models here.
class Product(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length=100)
	price = models.FloatField(default=0.0)
	#image = models.ImageField()
	def __str__(self):
		return self.name

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="shop")

