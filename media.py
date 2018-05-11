# A class Movie containing the details of the movies

import webbrowser


class Movie():
    '''This class provides a way to store movie related information.
Attributes:
Title: Title of the movie.
Storyline: A string to store the basic plot of the movie.
Poster_image_url: A string to store the URL of the movie poster.
Trailer_youtube_url: A string to store the URL of the movie trailer.
Movie Rating: Which would display the movie rating'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
