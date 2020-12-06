# Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise.

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return True
    return False
   
is_sorted([1,2,3,4,5,6])