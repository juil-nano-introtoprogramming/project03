#!python
import webbrowser

class Movie():
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, title, plot, poster, trailer):
        self.title = title
        self.storyline = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        print self.title + " Trailer"
        webbrowser.open(self.trailer_youtube_url)
