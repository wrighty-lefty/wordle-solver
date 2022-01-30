import unittest
from Wordle import *


class TestWordleWord(unittest.TestCase):

    def test_word_mask_zero(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "POUND"
        expected = [LetterScore.NOT_IN_WORD for i in range(5)]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_correct(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "GREAT"
        expected = [LetterScore.CORRECT for i in range(5)]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_one_yellow(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "BENDS"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.OUT_OF_ORDER, LetterScore.NOT_IN_WORD,
                    LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_two_yellow(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "ADIEU"
        expected = [LetterScore.OUT_OF_ORDER, LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD,
                    LetterScore.OUT_OF_ORDER, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_one_green(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "COUNT"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD,
                    LetterScore.NOT_IN_WORD, LetterScore.CORRECT]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_two_green(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "SPENT"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD, LetterScore.CORRECT,
                    LetterScore.NOT_IN_WORD, LetterScore.CORRECT]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_one_yellow_one_green(self):
        wordle_word = WordleWord("GREAT")
        guessed_word = "GLAND"
        expected = [LetterScore.CORRECT, LetterScore.NOT_IN_WORD, LetterScore.OUT_OF_ORDER,
                    LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_double_letter_one_to_two(self):
        wordle_word = WordleWord("GREEN")
        guessed_word = "CHEAP"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD, LetterScore.CORRECT,
                    LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_double_letter_two_to_one(self):
        wordle_word = WordleWord("CHEAP")
        guessed_word = "GREEN"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD, LetterScore.CORRECT,
                    LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_double_letter_out_of_order(self):
        wordle_word = WordleWord("STATS")
        guessed_word = "TACIT"
        expected = [LetterScore.OUT_OF_ORDER, LetterScore.OUT_OF_ORDER, LetterScore.NOT_IN_WORD,
                    LetterScore.NOT_IN_WORD, LetterScore.OUT_OF_ORDER]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_triple_letter_three_to_two(self):
        wordle_word = WordleWord("GREEN")
        guessed_word = "EERIE"
        expected = [LetterScore.OUT_OF_ORDER, LetterScore.OUT_OF_ORDER, LetterScore.OUT_OF_ORDER,
                    LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_triple_letter_two_to_three(self):
        wordle_word = WordleWord("EERIE")
        guessed_word = "GREEN"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.OUT_OF_ORDER, LetterScore.OUT_OF_ORDER,
                    LetterScore.OUT_OF_ORDER, LetterScore.NOT_IN_WORD]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")

    def test_word_mask_double_double(self):
        wordle_word = WordleWord("PERKY")
        guessed_word = "GYPPY"
        expected = [LetterScore.NOT_IN_WORD, LetterScore.NOT_IN_WORD, LetterScore.OUT_OF_ORDER,
                    LetterScore.NOT_IN_WORD, LetterScore.CORRECT]
        self.assertEqual(expected, wordle_word.generate_word_mask(guessed_word),
                         f"Solution: {wordle_word.word}, Guess: {guessed_word}")


if __name__ == '__main__':
    unittest.main()
