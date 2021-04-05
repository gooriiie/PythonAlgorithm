import sys

number = (int)(input())

scoreA = []
scoreB = []
representative = []

for _ in range(number):
    testcase = sys.stdin.readline().rstrip().split(" ")
    testcase_list = list(testcase)
    scoreA.append((int)(testcase_list[0]))
    scoreB.append((int)(testcase_list[1]))

for i in range(number):
    count = 0
    for j in range(number):
        if(i == j):
            continue
        if(scoreA[i] < scoreA[j] or scoreB[i] < scoreB[j]):
            count += 1
            continue
        else:
            break
    if(count == number-1):
        representative.append(i)

representative_set = set(representative)

print(len(representative_set))
