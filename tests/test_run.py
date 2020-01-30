import unittest
from run import hello_world

class TestRun(unittest.TestCase):


    def test_print_hello_world(self):
        expected = 'HELLO WORLD!!!'

        actual = hello_world()

        self.assertEqual(expected, actual)