from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    cuisine_type = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    is_open = models.BooleanField(default=True)
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ["-rating"]

    def __str__(self):
        return f"{self.name} ({self.city})"
