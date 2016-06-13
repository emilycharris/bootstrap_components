from django.db import models

# Create your models here.

class Roster(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=5)
    height = models.CharField(max_length=5)
    weight = models.IntegerField()
    year = models.CharField(max_length=2)
    hometown = models.CharField(max_length=50)
    bio_page = models.URLField(default=None)
    picture = models.URLField(blank=True)

    def __str__(self):
        return self.name