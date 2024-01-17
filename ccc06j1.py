# This is DMOJ problem ccc06j1
# https://dmoj.ca/problem/ccc06j1

# Input Specification

# The program should input a number for each type of item then calculate and display the Calorie total. The first line will be the customer's choice of burger, the second will be the choice of side, then drink, then dessert. You may assume that each input will be a number from 1 to 4. That is, each customer has to pick exactly one number from each of the four options out of each of the four categories.

# Output Specification

# The program prints out the total Calories of the selected meal, and stops executing after this output.


menu1 = [461, 431, 420, 0]
menu2 = [100, 57, 70, 0]
menu3 = [130, 160, 118, 0]
menu4 = [167, 266, 75, 0]

menu1choice = int(input())
menu2choice = int(input())
menu3choice = int(input())
menu4choice = int(input())

print("Your total Calorie count is" + " " + str(menu1[menu1choice-1] + menu2[menu2choice-1] + menu3[menu3choice-1] + menu4[menu4choice-1]) + ".")
