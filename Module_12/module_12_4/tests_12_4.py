import unittest as ut
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding= 'utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(ut.TestCase):
    def test_walk(self):
        try:
            walk = Runner('walk1', -3)
            for i in range(10):
                walk.walk()
            self.assertEqual(walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            run = Runner(12345)
            for i in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    ut.main()
