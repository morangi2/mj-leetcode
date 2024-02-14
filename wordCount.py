def wordCount(input_string):
    input_string = input_string.split()  # split the input sentence
    output_dict = {}
    stop_words = ["the", "and", "but", "or"]  # words we'd like to exclude

    for one_word in input_string:
        one_word = one_word.strip(".,!?")  # should not count punctuation
        one_word = one_word.lower()  # to ensure the function is case insensitive

        if one_word in stop_words:  # check if the word is in the stop_words list, and skip the word if it is
            continue

        # call .get() method on the dict to get the value of the key, if the key is not in the dict, return 0
        output_dict[one_word] = output_dict.get(one_word, 0) + 1

        """
        another way to write the above line is:
        if one_word in output_dict:
            output_dict[one_word] += 1
        else:
            output_dict[one_word] = 1

        OR
        output_dict.getDefault(one_word, 0)
        output_dict[one_word] += 1
        """

    return output_dict


# {'this': 1, 'is': 1, 'a': 1, 'sample': 2, 'sentence': 2, 'repeated': 1}
print(wordCount("This is a sample sentence. Sentence and sample are repeated."))
# {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'barks': 1, 'loudly': 1}
print(wordCount("The quick brown fox jumps over the lazy dog. The dog barks loudly."))
