import unittest

from project.cat import Cat


class TestCat(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("snow")

    def test_eat(self):
        self.assertFalse(self.cat.eat() == 1)

    def test_eat1(self):
        self.assertTrue(self.cat.sleepy.eat())

    def test_eat3(self):
        result = self.cat.fed.eat()
        expected_result = "Already fed."
        self.assertEqual(result, expected_result)

    def test_sleep(self):
        result = self.cat.sleepy.sleep()
        expected_result = "Cannot sleep while hungry"
        self.assertEqual(result, expected_result)

    def test_sleep1(self):
        self.assertFalse(self.cat.sleepy.sleep())


if __name__ == '__main__':
    unittest.main()