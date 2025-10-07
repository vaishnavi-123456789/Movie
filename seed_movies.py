# seed_movies.py

import os
import django
import requests
from django.core.files.base import ContentFile

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()

from movies.models import Movie


Movie_data = [
    {
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": "Sci-Fi / Thriller",
        "synopsis": "A skilled thief who steals secrets through dream-sharing technology is given a chance to have his criminal history erased if he can successfully plant an idea in someone's mind.",
        "poster": "https://m.media-amazon.com/images/I/51xJk8H9m4L._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "year": 2008,
        "genre": "Action / Crime",
        "synopsis": "Batman faces his greatest psychological and physical test when the Joker wreaks havoc on Gotham City.",
        "poster": "https://m.media-amazon.com/images/I/71pox3vTzJL._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "year": 2014,
        "genre": "Sci-Fi / Adventure",
        "synopsis": "A group of explorers travel through a wormhole in space to find a new home for humanity as Earth becomes uninhabitable.",
        "poster": "https://m.media-amazon.com/images/I/71n58U0vvtL._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "Avatar",
        "director": "James Cameron",
        "year": 2009,
        "genre": "Sci-Fi / Fantasy",
        "synopsis": "A paraplegic Marine is sent to the moon Pandora, where he becomes torn between following orders and protecting the world he grows to love.",
        "poster": "https://m.media-amazon.com/images/I/71NlcL7Tj-L._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "Titanic",
        "director": "James Cameron",
        "year": 1997,
        "genre": "Romance / Drama",
        "synopsis": "A young aristocrat falls in love with a poor artist aboard the doomed R.M.S. Titanic.",
        "poster": "https://m.media-amazon.com/images/I/81BES+tsPLL._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994,
        "genre": "Drama",
        "synopsis": "A banker wrongly imprisoned for murder forms a friendship with a fellow inmate and finds redemption through acts of hope.",
        "poster": "https://m.media-amazon.com/images/I/71NIpQwSKVL._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "Parasite",
        "director": "Bong Joon-ho",
        "year": 2019,
        "genre": "Thriller / Drama",
        "synopsis": "A poor family schemes to become employed by a wealthy household, but their plan leads to shocking consequences.",
        "poster": "https://m.media-amazon.com/images/I/91W+z0QhO6L._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "Joker",
        "director": "Todd Phillips",
        "year": 2019,
        "genre": "Crime / Drama",
        "synopsis": "A mentally troubled comedian in Gotham City spirals into madness and becomes the infamous criminal mastermind known as the Joker.",
        "poster": "https://m.media-amazon.com/images/I/71y4kXK0RoL._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "The Lion King",
        "director": "Roger Allers, Rob Minkoff",
        "year": 1994,
        "genre": "Animation / Adventure",
        "synopsis": "A young lion prince flees his kingdom after his father’s death but must return to reclaim his throne.",
        "poster": "https://m.media-amazon.com/images/I/81qzGU16xwL._AC_UF894,1000_QL80_.jpg"
    },
    {
        "title": "Avengers: Endgame",
        "director": "Anthony & Joe Russo",
        "year": 2019,
        "genre": "Action / Superhero",
        "synopsis": "The remaining Avengers unite for one final mission to reverse the damage caused by Thanos and restore balance to the universe.",
        "poster": "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_UF894,1000_QL80_.jpg"
    }
]
  
def populate_movies():
    print("Deleting old movie data...")
    Movie.objects.all().delete() # Optional: Clears the database first
    
    print("Populating new movie data...")
    for movie_data in Movie_data:
        # Create the movie object without the poster first
        movie_obj = Movie.objects.create(
            title=movie_data['title'],
            director=movie_data['director'],
            release_year=movie_data['year'], # Note: field name is 'release_year' in model
            genre=movie_data['genre'],
            synopsis=movie_data['synopsis']
        )

        # Now, handle the poster image
        poster_url = movie_data.get('poster')
        if poster_url:
            try:
                response = requests.get(poster_url)
                if response.status_code == 200:
                    # Get the filename from the URL
                    file_name = poster_url.split('/')[-1]
                    
                    # Save the image content to the poster field
                    movie_obj.poster.save(
                        file_name,
                        ContentFile(response.content),
                        save=True
                    )
                    print(f"Successfully added '{movie_data['title']}' with poster.")
                else:
                    print(f"Could not download poster for '{movie_data['title']}'. Status code: {response.status_code}")
            except Exception as e:
                print(f"An error occurred while fetching poster for '{movie_data['title']}': {e}")
        else:
            print(f"Successfully added '{movie_data['title']}' without a poster.")
            
if __name__ == '__main__':
    populate_movies()
    print("Movie population complete!")