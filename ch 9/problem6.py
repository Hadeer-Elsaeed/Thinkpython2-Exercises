# Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
# appear in alphabetical order (double letters are ok). How many abecedarian words are there?


with open('words.txt', 'r') as fd:
    word_list = fd.read().split()
    
def is_abecedarian(w):
    return w == ''.join(sorted(w))
    

words = [word for word in word_list if is_abecedarian(word)]
print ("There are {} abecedarian words.".format(len(words)))