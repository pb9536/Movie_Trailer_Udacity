# Details of instances which displays on browser
import fresh_tomatoes
import media

'''Creates Movie objects, initialising these objects with title,
storyline,poster image link ,youtube video trailer link and movie rating'''
toy_story = media.Movie("Toy Story",
                        "Andy's toys get mistakenly delivered to a day care.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=6M6ISoW_Gas",
                        "9.6")

avatar = media.Movie("Avatar",
                     """Story is about alien world of Pandora
                        live and humans try to occupy it.""",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     "10.0")

boss_baby = media.Movie("Boss Baby",
                        """A Little baby can talk and the two team
                           up to foil the plans of the CEO of Puppy Co.""",
                        "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=h24gEn3y82Q",
                        "8.5")

moana = media.Movie("Moana",
                    """Moana sets on a voyage to persuade Maui, a demigod
                       to return the heart of the goddess""",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=LKFuXETZUsI",
                    "8.0")

the_emoji = media.Movie("The Emoji",
                        """Gene is an emoji that lives in Textopolis,
                           digital city inside the phone of his user Alex.""",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/The_Emoji_Movie_film_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=r8pJt4dK_s4",
                        "7.5")

avengers = media.Movie("Avengers",
                       """Avengers is War 2018 American superhero film based
                          on the Marvel Comics superhero team the Avengers""",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=DjNQq0iXJYY",
                       "8.5")

beauty_beast = media.Movie("Beauty and the Beast",
                           """Belle, a village girl, embarks on a journey to
                              save her father from a creature""",
                           "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=e3Nl_TCQXuw",
                           "9.5")

# Store the movie objects in a list
movies = [toy_story, avatar, boss_baby, moana,
          the_emoji, beauty_beast, avengers]
# open the movie website in a browser using a defined module fresh_tomatoes

fresh_tomatoes.open_movies_page(movies)
