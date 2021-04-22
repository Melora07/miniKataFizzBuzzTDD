import unittest

from fizzBuzzKata.fizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def test_quand_j_ai_un_chiffre_divisible_par_2_affiche_fizz(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.check([2]), "fizz")

    def test_quand_j_ai_un_chiffre_non_divisible_par_2_affiche_buzz(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.check([3]), "buzz")

    def test_quand_j_ai_un_autre_chiffre_divisible_par_2_affiche_fizz(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.check([6]), "fizz")

    def test_quand_j_ai_un_chiffre_divisible_par_2_l_autre_non_affiche_fizz_buzz(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.check([6, 3]), "fizzbuzz")

    def test_quand_j_ai_un_chiffre_divisible_par_2_l_autre_non_affiche_buzz_fizz(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.check([5, 4]), "buzzfizz")

    def test_de_fou(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(fizzbuzz.check([1, 2, 3, 4, 5]), "buzzfizzbuzzfizzbuzz")


if __name__ == '__main__':
    unittest.main()
