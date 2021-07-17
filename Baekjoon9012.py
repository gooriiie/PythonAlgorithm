import sys

T = int(input())

for _ in range(T):
    ps = list(sys.stdin.readline().rstrip())
    stack = []
    for i in ps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
