#Medis.py contains a class 'Movie' in which I've created instance variables: title, release, storyline, etc.
#I used these to create a "shema" for each movie (with their data) stored in enternatinment_center.py.

class Movie():
    """This is how I store information about my favorite films"""

    def __init__(self, movie_title, release_date, movie_storyline, movie_category, movie_director, movie_writer, movie_stars, poster_image, trailer_youtube,):
        self.title = movie_title
        self.release = release_date
        self.storyline = movie_storyline
        self.category = movie_category
        self.director = movie_director
        self.writer = movie_writer
        self.stars = movie_stars
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
