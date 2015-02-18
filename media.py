import webbrowser

__author__ = 'jonengelbert'

class Video():
    """Video documentation"""
    def __init__(self, _title, _duration):
        self.title = _title
        self.duration = _duration

class Movie(Video):
    """Movie documentation"""
    MOVIE_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, _title, _duration, _storyline, _image, _trailer):
        Video.__init__(self, _title, _duration)
        self.storyline = _storyline
        self.poster_image_url = _image
        self.trailer_youtube_url = _trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

class TvShow(Video):
    """TvShow documentation-- not implemented yet"""
    def __init__(self, _title, _duration, _season, _episode, _tv_station):
        Video.__init__(_title, _duration)
        self.season = _season
        self.episode = _episode
        self.tv_station = _tv_station

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_local_listing(self):
        webbrowser.open(self.poster_image_url)