import unittest
from mock import MagicMock
from dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_dictionary(self):
        d = Dictionary("mocks/mockDictionary.txt")

        self.assertTrue(d.is_word("fabricate"))
        self.assertFalse(d.is_word("illusion"))
