import unittest
from unrepeated import unrepeated_counter, adv_unrepeated_counter

class TestUnrepeated(unittest.TestCase):

    def test_unrepeated_counter(self):
        self.assertEqual(unrepeated_counter('abcabcbb'), 3)
        self.assertEqual(unrepeated_counter('bbbbb'), 1)
        self.assertEqual(unrepeated_counter('abcdefghijklaxyz'), 15)
        self.assertEqual(unrepeated_counter('abcdefghijklmnobpqrstu'), 20)
        self.assertEqual(unrepeated_counter('abcdefghijklmnopqcrstuvwxyz'), 24)

    def test_adv_unrepeated_counter(self):
        self.assertEqual(adv_unrepeated_counter('abcabcbb'), 3)
        self.assertEqual(adv_unrepeated_counter('bbbbb'), 1)
        self.assertEqual(adv_unrepeated_counter('abcdefghijklaxyz'), 15)
        self.assertEqual(adv_unrepeated_counter('abcdefghijklmnobpqrstu'), 20)
        self.assertEqual(adv_unrepeated_counter('abcdefghijklmnopqcrstuvwxyz'),
                                                24)


if __name__ == '__main__':
    unittest.main()
