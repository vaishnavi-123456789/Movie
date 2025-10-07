# movies/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This line is the one for the main movie list page
    path('', views.movie_list, name='movie_list'),
    
    path('add/', views.add_movie, name='add_movie'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
]