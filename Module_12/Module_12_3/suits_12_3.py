import unittest as ut
import tests_12_3

runtest = ut.TestSuite()
runtest.addTest(ut.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runtest.addTest(ut.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = ut.TextTestRunner(verbosity=2)
runner.run(runtest)