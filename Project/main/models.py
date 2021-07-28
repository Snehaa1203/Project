from django.db import models

# Create your models here.
class Product(models.Model):
	name=models.CharField( max_length=100)
	quantity= models.IntegerField(default=2)
	image=models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.name
