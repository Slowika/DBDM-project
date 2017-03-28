import unittest
from closure import Closure_improved

class MyTestCase(unittest.TestCase):
    def test_normal_case(self):
        fds = {frozenset(['F']): frozenset(['B', 'E', 'D']), frozenset(['B']): frozenset(['D']), frozenset(['B', 'D']): frozenset(['C']), frozenset(['E']): frozenset(['C', 'G']), frozenset(['A', 'B']): frozenset(['H', 'G']), frozenset(['H']): frozenset(['G'])}
        closure = set(['C', 'B', 'D'])
        self.assertEqual(Closure_improved(fds, set(['B', 'D'])), closure)
    def test_empty_fds(self):
        fds = {}
        self.assertEqual(Closure_improved(fds, set(['A', 'E'])), set(['A', 'E']))
    def test_right_blank(self):
        fds = {frozenset(['A']) : frozenset()}
        self.assertEqual(Closure_improved(fds, set(['A'])), set(['A']))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

