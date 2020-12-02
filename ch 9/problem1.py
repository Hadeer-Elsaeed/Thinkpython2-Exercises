# Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace)
def words(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) >20:
            print(word)

words('words.txt')
