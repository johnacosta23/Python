# This is DMOJ problem wc17c3j3
# https://dmoj.ca/problem/wc17c3j3

# The password must be a string between 8 and 12 characters long (inclusive), such that every character is either a lowercase letter (a … z), uppercase letter (A … Z), or digit (0 … 9). Furthermore, it must contain at least three lowercase letters, at least two uppercase letters, and at least one digit.

# You've got a potential password in mind, a non-empty string made up of at most 100 characters, each of which is a lowercase letter, uppercase letter, or digit. Rather than entering the password into the site and risking rejection, you'd like to determine for yourself whether or not your password would validly satisfy all of the rules.
# Input Specification

# The first and only line of input consists of a single string, the password.
# Output Specification

# Output a single string, either Valid if the password is valid, or Invalid otherwise.


def checkpassword(password1):
    upperchars, lowerchars, digits = 0, 0, 0
    length = len(password1)

    if (length >= 8) or (length <= 12):
        for i in range(0, length):
            if password1[i].isupper():
                upperchars += 1
            elif password1[i].islower():
                lowerchars += 1
            elif password1[i].isdigit():
                digits += 1
        if upperchars >= 2 and lowerchars >= 3 and digits >= 1:
                print("Valid")
        else:
                print("Invalid")
password1 = str(input())
checkpassword(password1)
