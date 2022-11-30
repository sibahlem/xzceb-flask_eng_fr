import unittest
from unittest import TestCase

from translator import english_to_french, french_to_english

class testEnglishToFench(unittest.TestCase):
    def test1 (self):
        self.assertNotEqual(english_to_french("None"), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class testFrenchToEnglish(unittest.TestCase):
    def test1 (self):
        self.assertNotEqual(french_to_english("None"), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()