from imdb import imdb_name, imdb_rate, imdb_image
from save import save_to_json
from save import movies

def add_movie(url, r):
    name = str(imdb_name(url))
    rating = str(imdb_rate(url))
    our_rating = round(float(r), 2)
    image = str(imdb_image(url))
    if name not in [movie[0] for movie in movies]:
        movies.append((name, rating, our_rating, image))
        save_to_json(name, rating, our_rating, image)
    else:
        return movies