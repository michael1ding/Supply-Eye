import uuid
from django.core import validators
from django.db import models

# Create your models here.

class Item(models.Model):
    # Item fields
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
    price = models.FloatField(validators=[validators.MinValueValidator(0.01)]) # price
    quantity = models.PositiveIntegerField()
    deleted = models.BooleanField(default=False)
    deleted_comments = models.CharField(max_length=2500, default="")

    def __str__(self):
        return self.name

    def set_deleted(self, val):
        self.deleted = val
    
    def set_deleted_comments(self, val):
        self.deleted_comments = val
