from tests.resources.base_test import BaseTestCase
from resources.movie import Movie


class TestMovie(BaseTestCase):
    def test_list(self):
        movies = Movie.list()
        self.assertEquals(8, len(movies))

    def test_index(self):
        movie = Movie.index('5cd95395de30eff6ebccde56')
        self.assertEquals('The Lord of the Rings Series', movie.name)

    def test_quotes(self):
        quotes = Movie.quotes('5cd95395de30eff6ebccde5c')
        self.assertGreaterlen(quotes, 10)






