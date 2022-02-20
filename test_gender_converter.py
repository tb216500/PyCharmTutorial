from unittest import TestCase


class Test(TestCase):
    def test_convert_gender(self):
        expected = "Male"
        actual = convert_gender("M")
        self.assertEqual(actual, expected)
