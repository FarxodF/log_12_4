import unittest
import logging
from runner import Runner


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("John", -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
        else:
            self.assertEqual(runner.walk(), "John is walking at -5 km/h")
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)  
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            self.assertEqual(runner.run(), "123 is running at 10 km/h")
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()

