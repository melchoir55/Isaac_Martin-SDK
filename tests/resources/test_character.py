from tests.resources.base_test import BaseTestCase
from resources.character import Character
from filter import Filter, Operator
class TestCharacter(BaseTestCase):
    def test_list(self):
        characters = Character.list(limit=10)
        self.assertEquals(10, len(characters))
        self.assertTrue(isinstance(characters[0], Character))

    def test_index(self):
        character = Character.index('5cd99d4bde30eff6ebccfbbe')
        self.assertEquals('Adanel', character.name)

    def test_quotes(self):
        quotes = Character.quotes('5cd99d4bde30eff6ebccfea0', limit=11)
        self.assertGreater(len(quotes), 10)

    def test_filter_list(self):
        filter = Filter(field='gender',
                       operator=Operator.MATCH,
                       value='Female')
        characters = Character.list(sort='name:dsc', filters=[filter], limit=10)
        self.assertEquals(10, len(characters))
        self.assertEquals('Female', characters[0].gender)

        filter = Filter(field='name',
                       operator=Operator.REGEX_MATCH,
                       value='Gandalf')
        characters = Character.list(sort='name:dsc', filters=[filter], limit=10)
        self.assertEquals(1, len(characters))
        self.assertEquals('Gandalf', characters[0].name)








