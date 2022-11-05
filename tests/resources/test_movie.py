from tests.resources.base_test import BaseTestCase
from isaac_martin_sdk.resources.movie import Movie
from isaac_martin_sdk.filter import Filter, Operator


class TestMovie(BaseTestCase):
    def test_list(self):
        movies = Movie.list()
        self.assertEquals(8, len(movies))
        self.assertTrue(isinstance(movies[0], Movie))

    def test_index(self):
        movie = Movie.index('5cd95395de30eff6ebccde56')
        self.assertEquals('The Lord of the Rings Series', movie.name)

    def test_quotes(self):
        quotes = Movie.quotes('5cd95395de30eff6ebccde5c')
        self.assertGreater(len(quotes), 10)

    def test_filter_list(self):
        filter = Filter(field='runtimeInMinutes',
                       operator=Operator.GREATER_THAN_OR_EQUAL_TO,
                       value=162)
        movies = Movie.list(sort='name:dsc', filters=[filter])
        self.assertEquals(6, len(movies))









