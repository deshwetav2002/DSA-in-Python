from collections import deque


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_prefix(expr):

    #step 1: reverse expression
    expr = expr[::-1]

    #step 2: change brackets
    new_expr = " "
    for ch in expr:
        if ch=='(':
            new_expr+=')'
        elif ch==')':
            new_expr+='('
        else:
            new_expr+=ch

    #step 3: convert to postfix
    stack=deque()
    postfix = " "

    for ch in new_expr:
        if ch == '(':
            stack.append(ch)
        elif ch==')':
            while stack and stack[-1] != '(':
                postfix+=stack.pop()
            stack.pop()
        elif ch.isalnum():
            postfix+=ch
        else:
            while stack and precedence(ch)<=precedence(stack[-1]):
                postfix+=stack.pop()
            stack.append(ch)
    while stack:
        postfix+=stack.pop()
    
    # Step 4: reverse postfix → prefix
    prefix = postfix[::-1]
    return prefix


# Driver
expr = "A+(B*C-(D/E^F)*G)*H"
print("Prefix:", infix_to_prefix(expr))