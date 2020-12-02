# Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
# and that returns True if the word uses all the required letters at least once. How many words are
# there that use all the vowels aeiou ? How about aeiouy ?

def uses_all(word,s):
    for l in s:
        return True if l in word else False
           
uses_all('hello','so')

def vowels():
    with open('words.txt', 'r') as fd:
        word_list = fd.read().splitlines()
    count = 0
    for w in word_list:
        if uses_all(w,'aeiou'):
            count = count +1
    print(count)
    return count

vowels()
    
