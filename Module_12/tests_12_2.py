import unittest as ut
import runner as rat


class TournamentTest(ut.TestCase):

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


    def test_tournament_1(self):
        test1 = rat.Tournament(90, self.r1, self.r3 )
        result1 = test1.start()
        test1_result = {i: str(j) for i, j in result1.items()}
        self.all_results.append(test1_result)
        self.assertTrue(result1[2], 'Ник')

    def test_tournament_2(self):
        test2 = rat.Tournament(90, self.r2, self.r3 )
        result2 = test2.start()
        test2_result = {i: str(j) for i, j in result2.items()}
        self.all_results.append(test2_result)
        self.assertTrue(result2[2], 'Ник')

    def test_tournament_3(self):
        test3 = rat.Tournament(90, self.r1, self.r2, self.r3 )
        result3 = test3.start()
        test3_result = {i: str(j) for i, j in result3.items()}
        self.all_results.append(test3_result)
        self.assertTrue(result3[3], 'Ник')


if __name__ == "__main__":
    ut.main()
