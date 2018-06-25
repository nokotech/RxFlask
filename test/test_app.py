from src.app import hello
import unittest

class TestApp(unittest.TestCase):
    
    def test_hello(self):
        print('test_hello')
        actual = hello()
        self.assertEqual("Hello World!", actual)
