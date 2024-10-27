
from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'films/index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'films/mp2.html', {'movie': movie})

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mp2(request):
    return render(request, 'mp2.html')
