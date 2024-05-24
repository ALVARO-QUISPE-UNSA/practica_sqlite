from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse

def lista_peliculas (req):
    movies = Movie.objects.all()
    first_id = ''
    titulo = ''
    if movies.exists():
        first_id = movies.first().movie_id
        titulo = movies.first().title
    #return render(req, '')
    msg = f"<p>El primer id es: {first_id} y el titulo: {titulo}</p>"
    return HttpResponse(msg.encode('utf-8'), content_type='text/html')


# Create your views here.
