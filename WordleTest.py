import unittest
from Wordle import *


class TestWordleWord(unittest.TestCase):

    def test_match_score_zero(self):
        wordle_word = WordleWord("great")
        guessed_word = "pound"
        self.assertEqual(0, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_correct(self):
        wordle_word = WordleWord("great")
        guessed_word = "great"
        self.assertEqual(wordle_config["correct_word_score"], wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_one_yellow(self):
        wordle_word = WordleWord("great")
        guessed_word = "bends"
        self.assertEqual(3, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_two_yellow(self):
        wordle_word = WordleWord("great")
        guessed_word = "adieu"
        self.assertEqual(28, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_one_green(self):
        wordle_word = WordleWord("great")
        guessed_word = "count"
        self.assertEqual(162, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_two_green(self):
        wordle_word = WordleWord("great")
        guessed_word = "spent"
        self.assertEqual(180, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_one_yellow_one_green(self):
        wordle_word = WordleWord("great")
        guessed_word = "gland"
        self.assertEqual(11, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_double_letter_one_to_two(self):
        wordle_word = WordleWord("green")
        guessed_word = "cheap"
        self.assertEqual(18, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_double_letter_two_to_one(self):
        wordle_word = WordleWord("cheap")
        guessed_word = "green"
        self.assertEqual(18, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_double_letter_out_of_order(self):
        wordle_word = WordleWord("stats")
        guessed_word = "tacit"
        self.assertEqual(85, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_triple_letter_three_to_two(self):
        wordle_word = WordleWord("green")
        guessed_word = "eerie"
        self.assertEqual(13, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_triple_letter_two_to_three(self):
        wordle_word = WordleWord("eerie")
        guessed_word = "green"
        self.assertEqual(39, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_match_score_double_double(self):
        wordle_word = WordleWord("perky")
        guessed_word = "gyppy"
        self.assertEqual(171, wordle_word.compute_match_score(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

if __name__ == '__main__':
    unittest.main()
