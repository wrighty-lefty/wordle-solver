from Wordle import *


def analyze_first_guesses():
    guessable_words = WordList(source_file="guessable_words")
    solution_words = WordList(source_file="solution_words")

    output_file = open("first_guess_analysis.csv", "w")
    output_file.write("Word,Expected Bucket Size,Max Bucket Size\n")
    for word in guessable_words:
        if wordle_config["is_solution_list_known"]:
            buckets = solution_words.bucketize(word)
            word_count = len(solution_words)
        else:
            buckets = guessable_words.bucketize(word)
            word_count = len(guessable_words)
        expected_bucket_size = 0
        max_bucket_size = 0
        for count in buckets.values():
            expected_bucket_size += (count * (count / word_count))
            if count > max_bucket_size:
                max_bucket_size = count
        output_file.write(f"{word},{expected_bucket_size},{max_bucket_size}\n")
    output_file.close()
    return


if __name__ == "__main__":
    analyze_first_guesses()
