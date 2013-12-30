from django.db import models

# Create your models here.
class PoorGays(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # sex = models.IntegerField()
    #age = models.IntegerField()
    #picture = models.CharField(max_length=50)
    # birthday = models.DateField()

    def __unicode__(self):
        return self.name

