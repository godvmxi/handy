from django.db import models

# Create your models here.
class PoorGays(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # sex = models.IntegerField()
    #age = models.IntegerField()
    picture = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,null=True)
    # birthday = models.DateField()

    def __unicode__(self):
        return self.name

