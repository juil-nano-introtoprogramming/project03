#!python
import webbrowser

class Video(object):
    """The Video() class provides a way to store video related
    information."""
    def __init__(self, title, duration, medium, genre):
        self.title = title
        self.duration = duration
        self.medium = medium
        self.genre = genre

class Movie(Video):
    """The Movie() class provides a way to store movie related information."""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, duration, medium, genre, plot, poster, trailer, info):
        self.title = title
        self.duration = duration
        self.medium = medium
        self.genre = genre
        self.storyline = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.info_url = info

    def show_trailer(self):
        print self.title + " Trailer"
        webbrowser.open(self.trailer_youtube_url)

class TVShow(Movie):
    """ The TVShow() class stores television show related information."""

    def __init__(self, title, duration, medium, genre, plot, poster, trailer,
                info, seasons, episodes, ongoing):
        self.title = title
        self.duration = duration
        self.medium = medium
        self.genre = genre
        self.storyline = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.info_url = info
        self.num_seasons = num_seasons
        self.num_episodes = num_episodes
        self.is_ongoing = is_ongoing
