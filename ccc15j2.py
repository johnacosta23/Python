# This is DMOJ problem ccc15j2
# https://dmoj.ca/problem/ccc15j2

# Input Specification

# There will be one line of input that contains between 1 and 255 characters.

# Output Specification

# The output is determined by the following rules:

#    If the input line does not contain any happy or sad emoticons, output none.
#    Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
#    Otherwise, if the input line contains more happy than sad emoticons, output happy.
#    Otherwise, if the input line contains more sad than happy emoticons, output sad.

happy = ":-)"
sad = ":-("

mood = input()
counthappy = mood.count(":-)")
countsad = mood.count(":-(")

if ((happy in mood) and (sad not in mood)) or ((sad in mood) and (happy in mood) and (countsad < counthappy)):
    print("happy")
elif ((happy not in mood) and (sad in mood)) or ((sad in mood) and (happy in mood) and (countsad > counthappy)):
    print("sad")
elif (sad in mood) and (happy in mood)  and (countsad == counthappy):
    print("unsure")
else:
    print("none")
