# Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace)
def words(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) >20:
            print(word)

words('words.txt')

# Exercise 9.2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
# does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to
# do.
# In fact, it is difficult to construct a solitary thought without using that most common symbol. It is
# slow going at first, but with caution and hours of training you can gradually gain facility.
# All right, I’ll stop now.
# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
# it.
# Write a program that reads words.txt and prints only the words that have no “e”. Compute the
# percentage of words in the list that have no “e”
