from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest
import time

from src.task import task_three
from test.test_logger import TestLogger

SUMMARY_TEST_LOG_FILE = "./test_results/task_3/test_summary.txt"
DETAILS_TEST_LOG_FILE = "./test_results/task_3/test_details.txt"


class TaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results(SUMMARY_TEST_LOG_FILE, DETAILS_TEST_LOG_FILE)

    def test_task_three_matura_example(self):
        input_path = "./tests_input/matura_example.txt"

        expected = '1110001010'
        start = time.time()

        result = None
        try:
            result = task_three(input_path)
        except Exception:
            ...

        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_matura_example", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_matura_official(self):
        input_path = "./tests_input/matura_official_test.txt"

        expected = '10011000111001'
        start = time.time()

        result = None
        try:
            result = task_three(input_path)
        except Exception:
            ...

        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_matura_official", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_big(self):
        input_path = "./tests_input/big_test.txt"

        expected = '11111111110001'
        start = time.time()

        result = None
        try:
            result = task_three(input_path)
        except Exception:
            ...

        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_big", result == expected, duration)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
