
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.core.paginator import Paginator



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



def movie_list(request):
    # Tüm filmleri al
    film_listesi = Movie.objects.all()  
    sayfa_sayisi = 6  # Her sayfada 5 film göstermek istiyoruz
    paginator = Paginator(film_listesi, sayfa_sayisi)  # Paginator nesnesini oluştur

    # Geçerli sayfa numarasını URL'den alıyoruz. Varsayılan olarak sayfa 1.
    sayfa_numarasi = request.GET.get('sayfa', 1)
    sayfa_objesi = paginator.get_page(sayfa_numarasi)

    # İlk, son ve geçerli sayfaya göre sayfa numaralarını belirleyelim
    sayfa_numaralari = []
    if sayfa_objesi.has_previous():
        sayfa_numaralari.append(1)
    if sayfa_objesi.number > 2:
        sayfa_numaralari.append(sayfa_objesi.number - 1)
    sayfa_numaralari.append(sayfa_objesi.number)
    if sayfa_objesi.number < paginator.num_pages - 1:
        sayfa_numaralari.append(sayfa_objesi.number + 1)
    if sayfa_objesi.has_next():
        sayfa_numaralari.append(paginator.num_pages)

    return render(request, 'films/index.html', {
        'sayfa_objesi': sayfa_objesi,
        'sayfa_numaralari': sayfa_numaralari
    })