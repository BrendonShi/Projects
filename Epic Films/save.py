import json

def load_from_json():
    with open('movies.json', 'r') as json_file:
        movies_json = json.load(json_file)
    movies = [
        (movie["name"], movie["rating"], movie["our_rating"], movie["image"])
        for movie in movies_json
    ]
    return movies


movies = load_from_json()

## EXAMPLE:
# movies = [
#     ("Castiel", "10.0", ["Epic", "Cool"], "example1.jpg"),
# ]

def save_to_json(name, rating, our_rating, image):
    movies_json = [
        {
            "name": name,
            "rating": rating,
            "our_rating": our_rating,
            "image": image
        }
        for name, rating, our_rating, image in movies
    ]
    with open('movies.json', 'w') as json_file:
        json.dump(movies_json, json_file, indent=4)