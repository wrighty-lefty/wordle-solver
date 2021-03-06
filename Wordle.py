import json
import os
from enum import Enum
from random import randint

with open("data/config.json", "r") as fh:
    wordle_config = json.load(fh)
wordle_config["correct_word_score"] = (3 ** wordle_config["word_length"]) - 1


class WordleWord:

    def __init__(self, word):
        if len(word) != wordle_config["word_length"]:
            raise InvalidWordLengthError(word)

        self.word = word.upper()

    @staticmethod
    def mask_to_score(word_mask):
        return sum([(word_mask[i] * (3 ** i)) for i in range(len(word_mask))])

    def generate_word_mask(self, guessed_word):
        if len(self.word) != len(guessed_word):
            raise InvalidWordLengthError

        guessed_word = guessed_word.upper()
        # Loop through the letters twice, first handling the correct letters, then the misses
        first_pass_indices = range(wordle_config["word_length"])
        second_pass_indices = list()
        key_word = ""
        word_mask = [LetterScore.NOT_IN_WORD for i in range(wordle_config["word_length"])]
        for i in first_pass_indices:
            if self.word[i] == guessed_word[i]:
                word_mask[i] = LetterScore.CORRECT
                key_word += '_'
            else:
                second_pass_indices.append(i)
                key_word += self.word[i]
        analyzed_chars = ""
        for i in second_pass_indices:
            guessed_char = guessed_word[i]
            if guessed_char in key_word:
                if i == 0 or analyzed_chars.count(guessed_char) < key_word.count(guessed_char):
                    word_mask[i] = LetterScore.OUT_OF_ORDER
            analyzed_chars += guessed_char

        return word_mask


class LetterScore(Enum):
    NOT_IN_WORD = 0
    OUT_OF_ORDER = 1
    CORRECT = 2


class InvalidWordLengthError(Exception):
    def __init__(self, word):
        message = f"{word} is invalid because it is not the correct length."
        super().__init__(message)


class WordList:

    def __init__(self, word_list=None, source_file=None):
        if word_list:
            self.word_list = word_list
        elif source_file:
            self.load_from_file(source_file)
        self.word_set = set(self.word_list)

    def __len__(self):
        return len(self.word_list)

    def __contains__(self, item):
        return item in self.word_set

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index < len(self.word_list):
            word = self.word_list[self.iter_index]
            self.iter_index += 1
            return word
        else:
            raise StopIteration

    def load_from_file(self, source_file):
        self.word_list = list()
        file_path = os.path.join("data", wordle_config[source_file])
        file = open(file_path, "r")
        for line in file:
            word = line.rstrip()
            if len(word) == 0:
                break
            self.word_list.append(word)
        fh.close()

    def select_wordle_word(self):
        index = randint(0, len(self.word_list) - 1)
        word = self.word_list[index]
        return WordleWord(word)

    def bucketize(self, guessed_word):
        buckets = dict()
        for word in self.word_list:
            wordle_word = WordleWord(word)
            word_mask = wordle_word.generate_word_mask(guessed_word)
            match_score = WordleWord.mask_to_score(word_mask)
            if match_score in buckets.keys():
                buckets[match_score] += 1
            else:
                buckets[match_score] = 1
        return buckets

    def prune(self):
        pass
