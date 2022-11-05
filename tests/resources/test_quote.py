from tests.resources.base_test import BaseTestCase
from isaac_martin_sdk.resources.quote import Quote


class TestQuote(BaseTestCase):
    def test_list(self):
        quotes = Quote.list(limit=10)
        self.assertEquals(10, len(quotes))
        self.assertTrue(isinstance(quotes[0], Quote))










