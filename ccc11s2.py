# This is DMOJ problem ccc11s2
# https://dmoj.ca/problem/ccc11s2

# Input Specification

# The input will contain the number N ( 0 < N < 10 000 ) followed by 2 N lines. The 2 N lines are composed of N lines of student responses (with one of A, B, C, D or E on each line), followed by N lines of correct answers (with one of A, B, C, D or E on each line), in the same order as the student answered the questions (that is, if line i is the student response, then line N + i will contain the correct answer to that question).

# Output Specification

# Output the integer C ( 0 ≤ C ≤ N ) which corresponds to the number of questions the student answered correctly.

questions = int(input())
totalcorrect = 0
lststu = []
lstcorr = []

for i in range(questions):
    student = input()
    lststu.append(student)
for a in range(questions):
    correct = input()
    lstcorr.append(correct)

lsttotal = lststu + lstcorr

for i in range(questions):
        if lsttotal[i] == lsttotal[i + questions]:
            totalcorrect += 1

print(totalcorrect)
