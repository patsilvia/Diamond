import unittest
import Diamond


class TestDiamond(unittest.TestCase):

    def test_Diamond(self):
        diamond = Diamond.Diamond('D')
        self.assertEqual(diamond._topChar, "D")

    def test_elaborator(self):
        diamond = Diamond.Diamond('E')
        arr_elaborate = diamond.elaborate()
        self.assertEqual(len(arr_elaborate), 9)

        diamond = Diamond.Diamond('K')
        arr_elaborate = diamond.elaborate()
        self.assertEqual(len(arr_elaborate), 21)

    def test_middle_index(self):
        diamond = Diamond.Diamond('E')
        arr_elaborate = diamond.elaborate()
        self.assertEqual(diamond.middle_index(arr_elaborate), 4)

    def test_run_topdown(self):
        diamond = Diamond.Diamond('E')
        arr_elaborate = diamond.elaborate()
        diamond.run_topdown(arr_elaborate)

        diamond = Diamond.Diamond('D')
        arr_elaborate = diamond.elaborate()
        diamond.run_topdown(arr_elaborate)
