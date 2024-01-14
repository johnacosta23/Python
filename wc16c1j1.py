# This is DMOJ problem wc16c1j1
# https://dmoj.ca/problem/wc16c1j1

# its spookiness level can, in fact, be measured and represented as a single integer S ( 2 ≤ S ≤ 20 ) . However, a simple number doesn't truly do the spooky sensation justice. As such, it can also be described with the word spoo...ooky, with exactly S o's.

# Given the integer S , can you cast a spooky incantation on your computer to have it produce the corresponding spooky word?

S = int(input())
print("sp" + "o"*S + "ky")


