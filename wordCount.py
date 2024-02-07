def wordCount(input_string):
    input_string = input_string.split()  # split the input sentence
    output_dict = {}
    stop_words = ["the", "and", "but", "or"]  # words we'd like to exclude

    for one_word in input_string:
        one_word = one_word.strip(".,!?")  # should not count punctuation
        one_word = one_word.lower()  # to ensure the function is case insensitive

        if one_word in stop_words:
            continue

        output_dict[one_word] = output_dict.get(one_word, 0) + 1

    return output_dict


print(wordCount("This is a sample sentence. Sentence and sample are repeated."))
print(wordCount("The quick brown fox jumps over the lazy dog. The dog barks loudly."))
