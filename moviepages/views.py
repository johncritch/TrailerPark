from django.shortcuts import render
from django.http import HttpResponse

from moviepages.models import Movie

# Create your views here.
def indexPageView(request):
    return render(request, 'moviepages/index.html')

def ourFavoritesPageView(request):
    return render(request, 'moviepages/favs.html')

def allMoviesPageView(request):
    movies = Movie.objects.all().order_by('-release_date')

    context = {
        "movies": movies
    }
    return render(request, 'moviepages/movies.html', context)

