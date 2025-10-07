# movies/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    """
    This view fetches all movie objects from the database, orders them,
    and passes them to the movie_list.html template to be displayed.
    """
    movies = Movie.objects.all().order_by('-release_year')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    """
    This view fetches a single movie based on its ID (primary key) and
    passes it to the movie_detail.html template. If the movie is not
    found, it raises a 404 error.
    """
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movie_detail.html', context)

def add_movie(request):
    """
    This view handles the form for adding a new movie.
    - If the request is GET, it displays a blank form.
    - If the request is POST, it processes the submitted data. If the
      form is valid, it saves the new movie and redirects to the movie list.
    """
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    context = {
        'form': form,
    }
    return render(request, 'movies/add_movie.html', context)