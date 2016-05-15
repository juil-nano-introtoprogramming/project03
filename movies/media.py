#!python
from collections import defaultdict
import weakref
import webbrowser

class KeepRefs(object):
    __refs__ = defaultdict(list)
    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        """Returns all instances of cls.

        Code taken from http://stackoverflow.com/a/12179752/745776"""
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class Video(KeepRefs):
    """The Video() class provides a way to store video related information.

    Args:
        duration (int): Length of video in minutes."""
    def __init__(self, title, plot, duration, genre):
        super(Video, self).__init__()
        self.title = title
        self.plot = plot
        self.duration = duration
        self.genre = genre

    def print_genre(self):
        """Return list of genres as a string."""
        genres = self.genre[0]
        if len(self.genre) > 1:
            for g in self.genre[1:]:
                genres += ', ' + g
        return genres

    @classmethod
    def in_genre(cls, genre):
        """Returns all videos with specified genre."""
        #TODO: Fix function
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if genre in inst.genre:
                yield inst

class Movie(Video):
    """The Movie() class provides a way to store movie related information."""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, plot, duration, genre, poster, trailer, info):
        super(Movie, self).__init__(title, plot, duration, genre)
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.info_url = info

    def show_trailer(self):
        """Opens the movie's trailer in a web browser."""
        print self.title + " Trailer"
        webbrowser.open(self.trailer_youtube_url)

class TVShow(Movie):
    """ The TVShow() class stores television show related information."""

    def __init__(self, title, plot, duration, genre, poster, trailer,
                info, seasons, episodes, ongoing):
        super(TVShow, self).__init__(title, plot, duration, genre, poster, trailer, info)
        self.num_seasons = seasons
        self.num_episodes = episodes
        self.is_ongoing = ongoing
