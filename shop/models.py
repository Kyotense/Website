from django.db import models
from django.utils import timezone
import datetime


class Company(models.Model):
	company_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="shop")
	def __str__(self):
		return self.company_name

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

# Create your models here.
class Product(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)
	description = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length=100)
	price = models.DecimalField( max_digits=4, decimal_places=2)
	#image = models.ImageField()
	def __str__(self):
		return self.name

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="shop")




