
#from django.contrib import admin

#from django.contrib import admin
#from .models import Movie
#admin.site.register(Movie)


from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'imdb_score', 'release_year')

admin.site.register(Movie, MovieAdmin)
