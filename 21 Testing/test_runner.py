import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'ivo'.upper()
        expected_result = 'IVO'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()