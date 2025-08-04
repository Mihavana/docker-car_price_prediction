from django.db import models

class PredictionHistory(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100)
    modelBrand = models.CharField(max_length=100)
    fuel = models.CharField(max_length=50)
    seller_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    km_driven = models.IntegerField()
    year = models.IntegerField()
    predicted_price = models.FloatField()
