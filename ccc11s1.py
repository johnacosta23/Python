# This is DMOJ problem ccc11s1
# https://dmoj.ca/problem/ccc11s1


#    if the given text has more t and T characters than s and S characters, we will say that it is (probably) English text;
#    if the given text has more s and S characters than t and T characters, we will say that it is (probably) French text;
#    if the number of t and T characters is the same as the number of s and S characters, we will say that it is (probably) French text.

# Input Specification

# The input will contain the number N ( 0 < N < 10 000 ) followed by N lines of text, where each line has at least one character and no more than 100 characters.

# Output Specification

# Your output will be one line. This line will either consist of the word English (indicating the text is probably English) or French (indicating the text is probably French).

lines = int(input())
Ttcount = 0
Sscount = 0
for i in range(lines):
    text = str(input())
    Ttcount = Ttcount + text.count("T") + text.count("t")
    Sscount = Sscount + text.count("S") + text.count("s")
if Ttcount > Sscount:
    print("English")
elif Ttcount == Sscount:
    print("French")
elif Ttcount < Sscount:
    print("French")
