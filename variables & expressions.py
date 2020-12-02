# • We’ve seen that n = 42 is legal. What about 42 = n ?
    #  Syntax error 
    
# • How about x = y = 1 ?
    # No problem x will be equal 1 and also y.
    
# • In some languages every statement ends with a semi-colon, ; . What happens if you put a
#  semi-colon at the end of a Python statement?
    # no problem with semi-colon,it allows to add more statements in same line but it's not preferred.
    
#• What if you put a period [.] at the end of a statement?
    # it will be syntax error. 
    
# • In math notation you can multiply x and y like this: xy. What happens if you try that in Python?
    # it consider this is a variable 'xy'
    

# 1. The volume of a sphere with radius r is 3 4 πr 3 . What is the volume of a sphere with radius 5?
from math import pi , pow 
def volume(r):
    return 4/3 *pi* pow(r,3)

print(volume(5))



# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?

def cost(number):
    cost_piece = (24.95 - (40/100 * 24.95)) + 3
    return f"cost is {cost_piece}" if number == 1 else "cost is "+ str(cost_piece+ number * 0.75)

print(cost(60))


# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
second = 1
minute = 60 * second
hour = 60 * minute

time_for_leave_home = 6 * hour + 65 * minute
time_for_easy_pace = 2 * (8 * minute + 15 * second)
time_for_tempo = 3 * (7 * minute + 12 * second)

total_time = time_for_leave_home + time_for_easy_pace +time_for_tempo
hours = total_time // hour
part_hour = total_time % hour
minutes = part_hour // minute
seconds = part_hour % minute

