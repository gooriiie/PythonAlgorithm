
n = int(input())
result = []
stack = []
cur = 1
check = True

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        check = False
        break

if check:
    for i in result:
        print(i)
else:
    print("NO")
