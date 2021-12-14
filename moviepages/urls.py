from django.urls import path
from .views import deleteMoviePageView, indexPageView, allMoviesPageView, ourFavoritesPageView, editMoviePageView, updateMoviePageView, addMoviePageView, deleteMoviePageView

urlpatterns = [
    path("movies/", allMoviesPageView, name = "movies"),
    path("favs/", ourFavoritesPageView, name = "favs"),
    path("editMovie/<int:id>", editMoviePageView, name="edit"),
    path("updateMovie/", updateMoviePageView, name = "update"),
    path("addMovie/", addMoviePageView, name = 'add'),
    path('deleteMovie/<int:id>', deleteMoviePageView, name = 'delete'),
    path("", indexPageView, name = "index"),
]