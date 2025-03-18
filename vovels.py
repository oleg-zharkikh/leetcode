def get_count(sentence):
    dict_of_vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for i in sentence:
        if i in dict_of_vowels:
            dict_of_vowels[i] += 1
    return (
        dict_of_vowels["a"]
        + dict_of_vowels["e"]
        + dict_of_vowels["i"]
        + dict_of_vowels["o"]
        + dict_of_vowels["u"]
    )


print(get_count("two sums is passed!"))
