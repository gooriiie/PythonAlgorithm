import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    stack = []
    check = True
    for ch in sentence:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                check = False
                break
    if not stack and check:
        print("yes")
    else:
        print("no")



