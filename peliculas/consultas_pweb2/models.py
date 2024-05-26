from django.db import models
from django.db.models import manager

class Movie(models.Model):
    movie_id = models.IntegerField(db_column='MovieID', primary_key=True)
    title = models.CharField(max_length=70, db_column='Title')
    year = models.IntegerField(db_column='Year', null=True)
    score = models.FloatField(db_column='Score', null=True)
    votes = models.IntegerField(db_column='Votes', null=True)
    class Meta:
        managed = False
        db_table = 'Movie'
class Actor (models.Model):
    actor_id = models.AutoField(db_column='ActorId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=35, null=True )
    class Meta:
        managed = False
        db_table = 'Actor'
class Casting(models.Model):
    movie_id = models.IntegerField(db_column='MovieID')
    actor_id = models.IntegerField(db_column='ActorId')
    ordinal = models.IntegerField(db_column='Ordinal', null=True, blank=True)
    class Meta:
        unique_together = (('actor_id', 'movie_id'),)
        db_table = 'Casting'
        managed = False
        auto_created = True
