# Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements.
def middle(l):
    mid = len(l)//2
    if len(l)%2 !=0:
        return(l[mid])
    else:
        return(l[mid-1],l[mid])
        
        
middle([1,2,3,4,6,7,8,5])