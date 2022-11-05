from tests.resources.base_test import BaseTestCase
from resources.chapter import Chapter


class TestChapter(BaseTestCase):
    def test_list(self):
        chapters = Chapter.list(limit=10)
        self.assertEquals(10, len(chapters))
        self.assertTrue(isinstance(chapters[0], Chapter))










