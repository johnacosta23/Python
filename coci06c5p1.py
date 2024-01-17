# This is DMOJ problem coci06c5p1
# https://dmoj.ca/problem/coci06c5p1

# in the link all the context is provided

# Input Specification

# The first and only line contains a string of at most 50 characters, Borko's moves.

# Each of the characters is A, B or C.
# Output Specification

# Output the index of the cup under which the ball is: 1 if it is under the left cup, 2 if it is under the middle cup or 3 if it is under the right cup.

moves = input()
position = 1

for i in moves:
    if i == "A" and position == 1:
        position = 2
    elif i == "B" and position == 2:
        position = 3
    elif i == "C" and position == 3:
        position = 1
    elif i == "C" and position == 1:
        position = 3
    elif i == "A" and position == 2:
        position = 1
    elif i == "B" and position == 3:
        position = 2

print(position)
