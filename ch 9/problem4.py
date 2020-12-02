# Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
# that returns True if the word contains only letters in the list. Can you make a sentence using only
# the letters acefhlo ? Other than “Hoe alfalfa”?


def uses_only(word,s):
    for letter in word:
        if letter not in s:
            return False
    return True


def target():
    letters = 'acefhlo'
    with open('words.txt', 'r') as fd:
        word_list = fd.read().splitlines()

    words = [word for word in word_list if uses_only(word, letters)]
    print(words)
    return words

target()