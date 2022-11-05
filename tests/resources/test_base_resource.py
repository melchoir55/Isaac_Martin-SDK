from resources.book import ResourceBase
from tests.resources.base_test import BaseTestCase
from resources.base_resource import _apply_parameters
from filter import Filter, Operator


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

    def test_limit_page_offset(self):
        self.assertEquals('?limit=2', _apply_parameters('', limit=2))
        self.assertEquals('?offset=3&page=1', _apply_parameters('', offset=3, page=1))
        self.assertEquals('', _apply_parameters(''))
        self.assertEquals('?sort=name:asc', _apply_parameters('', sort='name:asc'))

    def test_filter(self):
        self.assertEquals('?name=Gandalf', _apply_parameters('',
                                                             filters=[Filter(field='name',
                                                                           operator=Operator.MATCH,
                                                                           value='Gandalf')]))
        self.assertEquals('?name!=Frodo', _apply_parameters('',
                                                            filters=[Filter(field='name',
                                                                           operator=Operator.NEGATE_MATCH,
                                                                           value='Frodo')]))
        self.assertEquals('?race=Hobbit,Human&race!=Orc,Goblin', _apply_parameters('',
                                                                                   filters=[Filter(field='race',
                                                                           operator=Operator.INCLUDE,
                                                                           value='Hobbit,Human'),
                                                                    Filter(field='race',
                                                                           operator=Operator.EXCLUDE,
                                                                           value='Orc,Goblin')
                                                                    ]))
        self.assertEquals('?name', _apply_parameters('',
                                                     filters=[Filter(field='name',
                                                                           operator=Operator.EXISTS,
                                                                           value=None)]))
        self.assertEquals('?!name', _apply_parameters('',
                                                      filters=[Filter(field='name',
                                                                           operator=Operator.NOT_EXISTS,
                                                                           value=None)]))
        self.assertEquals('?name=/foot/i', _apply_parameters('',
                                                             filters=[Filter(field='name',
                                                                           operator=Operator.REGEX_MATCH,
                                                                           value='foot')]))
        self.assertEquals('?name!=/foot/i', _apply_parameters('',
                                                              filters=[Filter(field='name',
                                                                           operator=Operator.REGEX_NOT_MATCH,
                                                                           value='foot')]))
        self.assertEquals('?budgetInMillions<100', _apply_parameters('',
                                                                     filters=[Filter(field='budgetInMillions',
                                                                           operator=Operator.LESS_THAN,
                                                                           value=100)]))
        self.assertEquals('?academyAwardWins>0', _apply_parameters('',
                                                                   filters=[Filter(field='academyAwardWins',
                                                                           operator=Operator.GREATER_THAN,
                                                                           value=0)]))
        self.assertEquals('?runtimeInMinutes>=160', _apply_parameters('',
                                                                      filters=[Filter(field='runtimeInMinutes',
                                                                           operator=Operator.GREATER_THAN_OR_EQUAL_TO,
                                                                           value=160)]))







