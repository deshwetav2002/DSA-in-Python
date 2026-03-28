from collections import deque

def check_pair(val1, val2):
    return (val1 == '(' and val2 == ')') or (val1 == '[' and val2 == ']') or (val1 == '{' and val2 == '}')

def check_balance(expr):
    stack = deque()

    for i in range(len(expr)):
        if expr[i] == '(' or expr[i] == '{' or expr[i] == '[':
            stack.append(expr[i])
        else:
            if len(stack) == 0:
                return False
            elif check_pair(stack[-1], expr[i]):
                stack.pop()
                continue
            return False
    return len(stack) == 0

# driver code
expr = "(){}[]"

if check_balance(expr):
    print("Balanced")
else:
    print("Not Balanced")