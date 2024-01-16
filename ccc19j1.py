# This is DMOJ problem ccc19j1
# https://dmoj.ca/problem/ccc19j1

# Input Specification

# The first three lines of input describe the scoring of the Apples, and the next three lines of input describe the scoring of the Bananas. For each team, the first line contains the number of successful 3 -point shots, the second line contains the number of successful 2 -point field goals, and the third line contains the number of successful 1 -point free throws. Each number will be an integer between 0 and 100 , inclusive.

# Output Specification


# The output will be a single character. If the Apples scored more points than the Bananas, output A. If the Bananas scored more points than the Apples, output B. Otherwise, output T, to indicate a tie.

Apples3 = int(input())
Apples2 = int(input())
Apples1 = int(input())
Bananas3 = int(input())
Bananas2 = int(input())
Bananas1 = int(input())
totalApples = (3*Apples3) + (2*Apples2) + (Apples1)
totalBananas = (3*Bananas3) + (2*Bananas2) + (Bananas1)

if totalBananas > totalApples:
    print("B")
elif totalBananas < totalApples:
    print("A")
else:
    print("T")
