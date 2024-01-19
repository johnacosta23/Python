# This is DMOJ problem ccc18j2
# https://dmoj.ca/problem/ccc18j2

# Input Specification

# The first line of input contains the integer N ( 1 ≤ N ≤ 100 ) . The second and third lines of input contain N characters each. The second line of input records the information about yesterday's parking spaces, and the third line of input records the information about today's parking spaces. Each of these 2 N characters will either be C to indicate an occupied space or . to indicate it was an empty parking space.

# Output Specification

# Output the number of parking spaces which were occupied yesterday and today.

places = int(input())
yesterday = input()
today = input()
occupied = 0

for i in range(0, places):
    if today[i] == "C" and yesterday[i] == "C":
        occupied += 1
print(occupied)
