import fresh_tomatoes
import media
__author__ = 'jonengelbert'

def init_movies():
    """initializes movies structure, then returns it.  Future versions should pull movies from a database"""
    toy_story = media.Movie("Toy Story",
                            120,
                           "A story of a boy and his toys",
                           "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    avatar = media.Movie("Avatar",
                           120,
                           "A marine on an alien planet",
                           "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=5PSNL1qE6VY")

    sting = media.Movie("Sting",
                        120,
                        "A couple of grifters pull a big scam",
                        "http://www.adammcdaniel.com/AmselArt/sting_xlg.jpg",
                        "https://www.youtube.com/watch?v=LN2hBOIXhBs")

    princess_bride = media.Movie("Princess Bride",
                                 120,
                                 "romance/comedy",
                                 "http://ia.media-imdb.com/images/M/MV5BMTkzMDgyNjQwM15BMl5BanBnXkFtZTgwNTg2Mjc1MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                                 "https://www.youtube.com/watch?v=VYgcrny2hRs")

    movies = [toy_story, avatar, sting, princess_bride]
    return movies

def test(movies):
    """
    :param movies: list of movies.  Test to verify that it's populated correctly
    :return:None
    """
    assert(len(movies) == 4)
    assert(movies[0].title == "Toy Story")

movies = init_movies()
test(movies)
fresh_tomatoes.open_movies_page(movies)

