from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest
import time

from src.task import task_two
from test.test_logger import TestLogger

SUMMARY_TEST_LOG_FILE = "./test_results/task_2/test_summary.txt"
DETAILS_TEST_LOG_FILE = "./test_results/task_2/test_details.txt"


class TaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results(SUMMARY_TEST_LOG_FILE, DETAILS_TEST_LOG_FILE)

    def test_task_two_matura_example(self):
        input_path = "./tests_input/matura_example.txt"

        expected = ['10001011', '10111000', '10100111', '11111000', '10011100', '11100011', '10111010', '10100011', '10011010', '10110001', '11011010']
        start = time.time()

        result = None
        try:
            result = task_two(input_path)
        except Exception:
            ...

        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_two_matura_example", result == expected, duration)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
