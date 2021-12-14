from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from moviepages.models import Movie, Rating

# Create your views here.
def indexPageView(request):
    return render(request, 'moviepages/index.html')

def ourFavoritesPageView(request):
    return render(request, 'moviepages/favs.html')

def allMoviesPageView(request):
    movies = Movie.objects.filter(release_date__range = [datetime.today(), '2030-10-10']).order_by('release_date')

    context = {
        "movies": movies
    }
    return render(request, 'moviepages/movies.html', context)

def editMoviePageView(request, id):
    movie = Movie.objects.get(id = id)

    context = {
        "movie": movie
    }
    return render(request, 'moviepages/editMovie.html', context)

def updateMoviePageView(request):
    if request.method == 'POST':
        movie = Movie.objects.get(id = request.POST['id'])
        rating = Rating.objects.get(movie_id=request.POST['id'])

        movie.title = request.POST['title']
        movie.directors = request.POST['directors']
        movie.producers = request.POST['producers']
        movie.genre = request.POST['genre']
        movie.actors = request.POST['actors']
        if request.POST['release_date']:
            movie.release_date = request.POST['release_date']
        if request.FILES.get('poster'):
            movie.poster = request.FILES.get('poster')
        movie.trailer = request.POST['trailer']
        rating.rating = request.POST['rating']

        movie.save()
        rating.save()
    
    return allMoviesPageView(request)

def addMoviePageView(request):
    if request.method == 'POST':
        movie = Movie()
        rating = Rating()

        movie.title = request.POST['title']
        movie.directors = request.POST['directors']
        movie.producers = request.POST['producers']
        movie.genre = request.POST['genre']
        movie.actors = request.POST['actors']
        movie.release_date = request.POST['release_date']
        movie.poster = request.FILES.get('poster')
        movie.trailer = request.POST['trailer']

        movie.save()
        rating.movie_id = movie.id
        rating.rating = request.POST['rating']
        
        rating.save()

        return allMoviesPageView(request)
    else:
        return render(request, 'moviepages/addMovie.html')

def deleteMoviePageView(request, id):
    movie = Movie.objects.get(id = id)
    movie.delete()

    return allMoviesPageView(request)

