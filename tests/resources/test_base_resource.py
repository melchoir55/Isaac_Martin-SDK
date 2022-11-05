from resources.base_resource import ResourceBase
from tests.resources.base_test import BaseTestCase


class TestBase(BaseTestCase):
    def test_list_no_auth(self):
        base = ResourceBase()
        base.auth_header = None
        base.endpoint = '/book/'

        response = base.list()
        self.assertTrue(response.ok)

    def test_list_auth(self):
        base = ResourceBase()
        base.endpoint = '/movie/'

        response = base.list()
        self.assertTrue(response.ok)






