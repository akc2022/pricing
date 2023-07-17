from django.db import models

# Create your models here.

class City_House_Price(models.Model):
	city= models.CharField(max_length=60)
	state = models.CharField(max_length=60)
	average_price = models.FloatField()

	def __str__(self):
		return self.city



class Avocado_Price(models.Model):
	average_price = models.FloatField()
	total_volume =	models.FloatField()
	avocado_4046 = models.FloatField()
	avocado_4225 = models.FloatField()
	avocado_4770 = models.FloatField()
	total_bags = models.FloatField()
	small_bags = models.FloatField()
	large_bags = models.FloatField()
	xlarge_bags = models.FloatField()
	avocado_type = models.CharField(max_length=60)
	city = models.ForeignKey(City_House_Price, blank = True, null = True, on_delete = models.CASCADE)

	def __str__(self):
		return str(self.city)
