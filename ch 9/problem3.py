# Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
   
def avoids(word,s):
    return True if s not in word else False
        
# avoids('hello','o')
  
  
  
  
# Write a program that prompts the user to enter a string of forbidden letters and then prints the
# number of words that don’t contain any of them.Can you find a combination of 5 forbidden letters
# that excludes the smallest number of words?     

def forbideden_names(s):
    count = 0
    words = input().split()
    for w in words:
        if avoids(w,s):
            count = count + 1     
    print(count)
    return count
        
forbideden_names('e')

