#
#
# from project.test_worker import Worker
#
# import unittest
#
#
# class WorkerTests(unittest.TestCase):
#     def setUp(self):
#         self.worker = Worker("ivo", 2000, 100)
#
#     def test_input(self):
#         result = "ivo 2000 100"
#         expected_result = "ivo 2000 100"
#         self.assertEqual(result, expected_result)
#
#     def test_rest(self):
#         result = self.worker.rest()
#         expected_result = "101"
#         self.assertNotEqual(result, expected_result)
#
#     def test_work(self):
#         result = self.worker.work()
#         expected_result = "Not enough energy."
#         self.assertEqual(result, expected_result)
#
#     def test_work2(self):
#         result = self.worker.money.work()
#         expected_result = "2000"
#         self.assertEqual(result, expected_result)
#
#     def test_work3(self):
#         result = self.worker.work()
#         expected_result = "100"
#         self.assertEqual(result, expected_result)
#
#     def test_get_info(self):
#         result = self.worker.get_info()
#         expected_result = "ivo has saved 0 money."
#         self.assertEqual(result, expected_result)
#
#
# if __name__ == '__main__':
#     unittest.main()



from project.test_worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("ivo", 2000, 100)

    def test_input(self):
        result = "ivo 2000 100"
        expected_result = "ivo 2000 100"
        self.assertEqual(result, expected_result)

    def test_rest(self):
        self.assertTrue(self.worker.rest() == 101)

    def test_work(self):
        result = self.worker.work()
        expected_result = "Not enough energy."
        self.assertEqual(result, expected_result)

    def test_work2(self):
       self.assertTrue(self.worker.money == 2000)

    def test_work3(self):
       self.assertTrue(self.worker.work() == 100)

    def test_get_info(self):
        result = self.worker.get_info()
        expected_result = "ivo has saved 0 money."
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()