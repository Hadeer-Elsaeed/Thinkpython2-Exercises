# Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumu-
# lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list

def cumsum(l):
    new_list = []
    s = 0
    for i in l:
        s +=i
        new_list.append(s)
    
    return new_list
    
cumsum([1,2,3])