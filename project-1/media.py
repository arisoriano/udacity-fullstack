import webbrowser


class Movie(object):

    """
    This is a class to create a movie object with detailed information

    Attributes:
        movie_title (str): the title of a movie
        movie_storyline (str): a short synopsis of a movie
        poster_image (str): a URL of a JPG image file for a movie
        trailer_youtube (str): a URL of a short clip of a movie
    """

    # Constructor declaration to initialize class and instance variables
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        super(Movie, self).__init__()
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Instance method for opening a trailer URL to view movie clip
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
