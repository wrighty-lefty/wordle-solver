from enum import Enum

class WordleWord:

    @staticmethod
    def initialize(word_length):
        WordleWord.word_length = 5
        WordleWord.correct_word_score = (3 ** word_length) - 1

    def __init__(self, word):
        if len(word) != WordleWord.word_length:
            raise InvalidWordLengthError

        self.word = word.upper()

    def compute_match_score(self, guessed_word):
        if len(self.word) != len(guessed_word):
            raise InvalidWordLengthError

        key_word = self.word
        guessed_word = guessed_word.upper()
        analyzed_chars = ""
        match_score = 0
        for i in range(WordleWord.word_length):
            letter_score = LetterScore.NOT_IN_WORD
            guessed_char = guessed_word[i]
            if key_word[i] == guessed_char:
                letter_score = LetterScore.CORRECT
            elif guessed_char in key_word:
                if i == 0 or analyzed_chars.count(guessed_char) < key_word.count(guessed_char):
                    letter_score = LetterScore.OUT_OF_ORDER

            analyzed_chars += guessed_char
            match_score += (letter_score.value * (3 ** i))

        return match_score

class LetterScore(Enum):
    NOT_IN_WORD = 0
    OUT_OF_ORDER = 1
    CORRECT = 2

class InvalidWordLengthError(Exception):
    def __init__(self, word):
        message = f"{word} is invalid because it is not the correct length."
        super().__init__(message)
