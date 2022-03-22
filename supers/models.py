from tkinter import CASCADE
from django.db import models

from super_types.models import SuperTypes

# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length=255)

    


class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    # primary_ability = models.CharField(max_length=255)
    # secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperTypes, on_delete=models.CASCADE, default=None)
    powers = models.ForeignKey(Power, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name


