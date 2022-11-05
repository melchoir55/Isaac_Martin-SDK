from resources.book import ResourceBase
from tests.resources.base_test import BaseTestCase


class TestBase(BaseTestCase):
    def test_make_request_no_auth(self):
        full_path = 'https://the-one-api.dev/v2/book/'
        ResourceBase.requires_auth = lambda: False

        response = ResourceBase.make_request(full_path)
        self.assertTrue(response.ok)

    def test_request_auth(self):
        full_path = 'https://the-one-api.dev/v2/movie/'
        ResourceBase.requires_auth = lambda: True

        response = ResourceBase.make_request(full_path)
        self.assertTrue(response.ok)

    def test_erroneously_request_without_auth(self):
        full_path = 'https://the-one-api.dev/v2/movie/'
        ResourceBase.requires_auth = lambda: False

        response = ResourceBase.make_request(full_path)
        self.assertFalse(response.ok)





