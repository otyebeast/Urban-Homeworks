import unittest as ut
import runner

class RunnerTest(ut.TestCase):
    def test_walk(self):
        walk = runner.Runner('walk1')
        for i in range(10):
            walk.walk()
        self.assertEquals(walk.distance, 50)


    def test_run(self):
        run = runner.Runner('run1')
        for i in range(10):
            run.run()
        self.assertEquals(run.distance, 100)


    def test_challenge(self):
        walk2 = runner.Runner('walk2')
        run2 = runner.Runner('run2')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEquals(walk2.distance, run2.distance)



if __name__ == '__main__':
    ut.main()