from WordleWord import *
from WordleDictionary import *

def main():
    WordleWord.initialize(5)
    wordle_dictionary = WordleDictionary()

    file_handle = open("output.csv", "w")
    file_handle.write("Word,Expected Bucket Size\n")
    for word in wordle_dictionary.word_list:
        expected_bucket_size = wordle_dictionary.bucketize(word)
        file_handle.write(f"{word},{expected_bucket_size}\n")
    file_handle.close()
    return

if __name__ == "__main__":
    main()
