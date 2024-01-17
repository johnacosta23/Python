# This is DMOJ problem ccc15j1
# https://dmoj.ca/problem/ccc15j1

# Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18.

#    If the date occurs before February 18, output the word Before.
#    If the date occurs after February 18, output the word After.
#    If the date is February 18, output the word Special.

month = int(input())
day = int(input())

if ((month == 2) and (day < 18)) or ((month < 2)):
    print("Before")
elif ((month == 2) and (day == 18)):
    print("Special")
else:
    print("After")
