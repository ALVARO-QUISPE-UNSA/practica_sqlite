from django.db import models
from django.db.models import manager

class Movie(models.Model):
    movie_id = models.IntegerField(db_column='MovieID', primary_key=True)
    title = models.CharField(max_length=70, db_column='Title')
    year = models.IntegerField(db_column='Year', null=True)
    score = models.FloatField(db_column='Score', null=True)
    votes = models.IntegerField(db_column='Votes', null=True)
    #year = models.IntegerField()
    #score = models.FloatField()
    #votes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'Movie'
class Actor (models.Model):
    actor_id = models.IntegerField(db_column='ActorId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=35, null=True )
    class Meta:
        managed = False
        db_table = 'Actor'
