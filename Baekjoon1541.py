import sys

cal = list(sys.stdin.readline().rstrip().split('-'))

answer = 0

for i in cal[0].split('+'):
    answer += int(i)
for i in cal[1:]:
    temp = 0
    for j in i.split('+'):
        temp += int(j)
    answer -= temp

print(answer)

