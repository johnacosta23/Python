# This is DMOJ problem wc16c1j1
# https://dmoj.ca/problem/wc16c1j1


#    C.C. will be absolutely satisfied if the pizza she gets has a width of 3 units and an extra-cheesiness of at least 95 % .
#    C.C. will be fairly satisfied if the pizza she gets has a width of 1 unit and an extra-cheesiness of at most 50 % .
#    C.C. will be very satisfied with any other pizza she receives.


# The first line of input will contain a single integer W ( 1 ≤ W ≤ 3 ) , denoting the width of the pizza C.C. receives.

# The second line of input will contain another integer C ( 0 ≤ C ≤ 100 ) , representing the percentage of the pizza covered in extra cheese.
# Output Specification

# A single line containing C.C.'s satisfaction with her order in the form: C.C. is M satisfied with her pizza.

# Here, M is a string describing her satisfaction, which will be one of: absolutely, fairly or very.

width = int(input())
cheese = int(input())

if width == 3 and cheese >= 95:
    print("C.C. is absolutely satisfied with her pizza.")
elif width == 1 and cheese <= 50:
    print("C.C. is fairly satisfied with her pizza.")
else:
    print("C.C. is very satisfied with her pizza.")
