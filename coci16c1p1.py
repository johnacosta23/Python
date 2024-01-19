# This is DMOJ problem coci16c1p1
# https://dmoj.ca/problem/coci16c1p1

# Input Specification

# The first line of input contains the integer X ( 1 ≤ X ≤ 100 ) .
# The second line of input contains the integer N ( 1 ≤ N ≤ 100 ) .
# Each of the following N lines contains an integer P i ( 0 ≤ P i ≤ 10 000 ) , the number of megabytes spent in each of the first N months of using the plan. Numbers P i will be such that Pero will never use more megabytes than he actually has.

# Output Specification

# The first and only line of output must contain the required value from the task.

Mb = int(input())
months = int(input())
remain = 0

for i in range(0, months):
    used = int(input())
    remain = remain + Mb - used

print(Mb + remain)
