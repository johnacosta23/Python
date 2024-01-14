# This is DMOJ problem dmopc15c7p2
# https://dmoj.ca/problems/?search=dmopc15c7p2

#The Challenge
#Count the number of words provided. For this problem, a word is any se-
#quence of lowercase letters. For example, hello is a word, but so are non-
#English “words” like bbaabbb

text = input()
numberofwords = text.count( " ") + 1
print( "Total of words in your text is" + " " +str(numberofwords))
