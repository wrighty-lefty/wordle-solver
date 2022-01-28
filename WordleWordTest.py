import unittest
from WordleWord import WordleWord

class TestWordleWord(unittest.TestCase):
    WordleWord.initialize(5)

    def test_match_score_zero(self):
        wordle_word = WordleWord("great")
        guessed_word = "pound"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 0)

    def test_match_score_correct(self):
        wordle_word = WordleWord("great")
        guessed_word = "great"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), WordleWord.correct_word_score)

    def test_match_score_one_yellow(self):
        wordle_word = WordleWord("great")
        guessed_word = "bends"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 3)

    def test_match_score_two_yellow(self):
        wordle_word = WordleWord("great")
        guessed_word = "adieu"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 28)

    def test_match_score_one_green(self):
        wordle_word = WordleWord("great")
        guessed_word = "count"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 162)

    def test_match_score_two_green(self):
        wordle_word = WordleWord("great")
        guessed_word = "spent"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 180)

    def test_match_score_one_yellow_one_green(self):
        wordle_word = WordleWord("great")
        guessed_word = "gland"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 11)

    def test_match_score_double_letter_one_to_two(self):
        wordle_word = WordleWord("green")
        guessed_word = "cheap"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 18)

    def test_match_score_double_letter_two_to_one(self):
        wordle_word = WordleWord("cheap")
        guessed_word = "green"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 18)

    def test_match_score_double_letter_out_of_order(self):
        wordle_word = WordleWord("stats")
        guessed_word = "tacit"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 85)

    def test_match_score_triple_letter_three_to_two(self):
        wordle_word = WordleWord("green")
        guessed_word = "eerie"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 13)

    def test_match_score_triple_letter_two_to_three(self):
        wordle_word = WordleWord("eerie")
        guessed_word = "green"
        self.assertEqual(wordle_word.compute_match_score(guessed_word), 39)

if __name__ == '__main__':
    unittest.main()
