from django.urls import path
from .views import indexPageView, allMoviesPageView, ourFavoritesPageView

urlpatterns = [
    path("movies/", allMoviesPageView, name = "movies"),
    path("favs/", ourFavoritesPageView, name = "favs"),
    path("", indexPageView, name = "index"),
]