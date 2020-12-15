import unittest
from ohe import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_tf(self):
        test_list = ["a", "b", "a"]
        actual = fit_transform(test_list)
        expected = [("a", [0, 1]), ("b", [1, 0]), ("a", [0, 1])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError) as cm:
            fit_transform()
        error = cm.exception
        self.assertIsInstance(error, TypeError)

    def test_lonely(self):
        test_string = "hello"
        actual = fit_transform(test_string)
        expected = [("hello", [1])]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        empty_list = []
        actual = fit_transform(empty_list)
        expected = []
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
