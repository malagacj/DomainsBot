import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_unrepeated_counter(self):
        self.assertEqual(is_palindrome('Anna'), True)
        self.assertEqual(is_palindrome('Mary'), False)
        self.assertEqual(is_palindrome('As I pee, sir, I see Pisa!'), True)
        self.assertEqual(is_palindrome('Hello Dean'), False)
        self.assertEqual(is_palindrome('Avid diva'), True)

if __name__ == '__main__':
    unittest.main()
