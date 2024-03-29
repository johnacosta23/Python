# This is DMOJ problem ccc18j1
# https://dmoj.ca/problem/ccc18j1

# Looking just at the last four digits, these properties are:

#    the first of these four digits is an 8 or 9;
#    the last digit is an 8 or 9 ;
#    the second and third digits are the same.

# For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.

# Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.
Input Specification

# The input will be 4 lines where each line contains exactly one digit in the range from 0 to 9 .

# Output Specification

# Output either ignore if the number matches the pattern for a telemarketer number; otherwise, output answer.

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

if (((first == 8) or first == 9) and ((fourth == 8) or fourth == 9)) and second == third:
    print("ignore")
else:
    print("answer")
