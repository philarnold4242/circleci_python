from unittest import TestCase

import circleci_python.mymod as mm

class TestJoke(TestCase):
    def test_is_string(self):
        s = mm.joke()

        self.assertEqual(s, "he")
