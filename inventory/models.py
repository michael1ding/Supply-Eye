import uuid
from django.core import validators
from django.db import models

# Create your models here.

class Item(models.Model):
    # Item fields
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
    price = models.FloatField(validators=[validators.MinValueValidator(0.01)]) # price
    quantity = models.PositiveIntegerField()
    #warehouse_location = models.CharField(max_length=200) # Bonus feature
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
