from django.db import models
from django.db.models import manager

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=70)
    year = models.IntegerField()
    score = models.FloatField()
    votes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'Movie'
# Create your models here.
