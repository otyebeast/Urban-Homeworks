import unittest as ut
import runner


class RunnerTest(ut.TestCase):
    is_frozen = True

    @ut.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walk = runner.Runner('walk1')
        for i in range(10):
            walk.walk()
        self.assertEquals(walk.distance, 50)

    @ut.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = runner.Runner('run1')
        for i in range(10):
            run.run()
        self.assertEquals(run.distance, 100)

    @ut.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walk2 = runner.Runner('walk2')
        run2 = runner.Runner('run2')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEquals(walk2.distance, run2.distance)


class TournamentTest(ut.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = rat.Runner('Усэйн', speed=10)
        self.r2 = rat.Runner('Андрей', speed=9)
        self.r3 = rat.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @ut.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        test1 = rat.Tournament(90, self.r1, self.r3)
        result1 = test1.start()
        test1_result = {i: str(j) for i, j in result1.items()}
        self.all_results.append(test1_result)
        self.assertTrue(result1[2], 'Ник')

    @ut.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        test2 = rat.Tournament(90, self.r2, self.r3)
        result2 = test2.start()
        test2_result = {i: str(j) for i, j in result2.items()}
        self.all_results.append(test2_result)
        self.assertTrue(result2[2], 'Ник')

    @ut.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        test3 = rat.Tournament(90, self.r1, self.r2, self.r3)
        result3 = test3.start()
        test3_result = {i: str(j) for i, j in result3.items()}
        self.all_results.append(test3_result)
        self.assertTrue(result3[3], 'Ник')


if __name__ == '__main__':
    ut.main()
