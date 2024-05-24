from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse

def lista_peliculas (req):
    movies = Movie.objects.all()
    first_id = ''
    if movies.exists():
        first_id = movies.first().movie_id
    #return render(req, '')
    msg = f"<p>El primer id es: {first_id}</p>"
    return HttpResponse(msg.encode('utf-8'))


# Create your views here.
