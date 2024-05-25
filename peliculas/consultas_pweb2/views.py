from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse
from django.http import JsonResponse

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
def vista_index(req):
    return render(req, 'consultas_pweb2/index.html')

def get_datos (req):
    tabla = req.GET.get('tabla')
    if (tabla == 'movies'):
        movie =  Movie.objects.all().values()
        lista = list(movie)
        return JsonResponse(lista, safe=False)
        #return 
    return JsonResponse({'error:': 'Tabla no encontrada'}, status=400)

# Create your views here.
