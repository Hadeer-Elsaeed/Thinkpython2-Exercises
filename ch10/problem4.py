# Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None

def chop(l):
    del l[0] , l[len(l)-1]
    return l    

chop([1,2,3,4,5,6,7])