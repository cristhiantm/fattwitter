from django.db import models


class Equivalence(models.Model):	
	product_name = models.CharField(max_length = 30)
	calories = models.FloatField()
