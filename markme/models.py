from django.db import models

# Create your models here.
class PoorGays(models.Model):
    name = models.CharField(max_length=20)
    # sex = models.CharField(max_length=20)
    age = models.IntegerField()
    #picture = models.CharField(max_length=50)
    # birthday = models.DateField()


