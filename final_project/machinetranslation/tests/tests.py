import unittest
from translator import englishtofrench, frenchtoenglish

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertNotEqual(englishtofrench("Hello"), "Hello")
    
    def test_f2e(self):
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchtoenglish("Bonjour"), "Bonjour")

    def test_null_input_e2f(self):
        self.assertIsNotNone(englishtofrench(None))

    def test_null_input_f2e(self):
        self.assertIsNotNone(frenchtoenglish(None))

if __name__ == '__main__':
    unittest.main()
