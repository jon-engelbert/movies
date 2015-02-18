__author__ = 'jonengelbert'


import unittest
import entertainment_center

class TestEC(unittest.TestCase):

    def setUp(self):
        pass

    def test(movies):
        movies = entertainment_center.init_movies()
        assert(len(movies) == 4)
        assert(movies[0].title == "Toy Story")

if __name__ == '__main__':
    unittest.main()