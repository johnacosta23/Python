# This is DMOJ problem wc17c1j2
# https://dmoj.ca/problem/wc17c1j2

# You came across the following formula, which holds true given that F is a temperature in degrees Fahrenheit while C is that same temperature in degrees Celsius:

# C = 5 / 9 × ( F − 32 )

# Given a value of C , which is an integer between − 40 and 40 (inclusive), determine the corresponding value of F , so that you can express the equivalent temperature in degrees Fahrenheit for the Americans' benefit.

# It's guaranteed that C will be chosen such that F will come out to exactly an integer, but you may output it with 0 or more digits after the decimal point.

celsius = int(input())
fahrenheit = ((9*celsius)//5)+32
print(fahrenheit)
