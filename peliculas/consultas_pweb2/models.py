from django.db import models
from django.db.models import manager

class Movie(models.Model):
    movie_id = models.IntegerField(db_column='MovieID', primary_key=True)
    title = models.CharField(max_length=70, db_column='Title')
    #year = models.IntegerField()
    #score = models.FloatField()
    #votes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'Movie'
# Create your models here.
