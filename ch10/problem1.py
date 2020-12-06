# Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists. For example:

def nested_sum(l):
    s = 0
    for i in l:
        if  isinstance(i,list):
            s += nested_sum(i)
        else:
          s += i        
    return (s)

nested_sum([1,[2,3],4,9])