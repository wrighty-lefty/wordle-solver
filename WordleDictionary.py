from WordleWord import *
from random import randint

class WordleDictionary:
    word_list_file = "word_list.txt"

    def __init__(self):
        self.load_word_list()

    def load_word_list(self):
        self.word_set = set()
        file_handle = open(WordleDictionary.word_list_file, "r")
        for line in file_handle:
            word = line.rstrip()
            if len(word) == 0:
                break
            self.word_set.add(word)
        file_handle.close()
        self.word_list = list(self.word_set)

    def select_wordle_word(self):
        index = randint(0, len(self.word_list) - 1)
        word = self.word_list[index]
        print(f"Index: {index}, count: {len(self.word_list)}")
        return WordleWord(word)

    def is_word_in_dictionary(self, word):
        return word in self.word_set

    def bucketize(self, guessed_word):
        buckets = dict()
        for word in self.word_list:
            wordle_word = WordleWord(word)
            match_score = wordle_word.compute_match_score(guessed_word)
            if match_score in buckets.keys():
                buckets[match_score] += 1
            else:
                buckets[match_score] = 1
        expected_bucket_size = 0
        total_count = len(self.word_list)
        for count in buckets.values():
            expected_bucket_size += (count * (count / total_count))
        return expected_bucket_size
