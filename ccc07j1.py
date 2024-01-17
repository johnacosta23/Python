# This is DMOJ problem ccc07j1
# https://dmoj.ca/problem/ccc07j1

# The bowls can be sorted by weight with the lightest bowl being the Baby Bear's bowl, the medium bowl being the Mama Bear's bowl and the heaviest bowl being the Papa Bear's bowl.

# Write a program that reads in three weights and prints out the weight of Mama Bear's bowl. You may assume all weights are positive integers less than 100 .

bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

lst = [bowl1, bowl2, bowl3]

lst.sort()

print(lst[1])
