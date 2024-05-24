from django.shortcuts import render
from .models import Movie

def lista_peliculas (req):
    movies = Movie.objects.all()
    return render(req, 'peliculas.html', {'movies': movies})

# Create your views here.
