from collections import deque

def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    elif op=='^':
        return 3
    return 0

def infix_to_postfix(expr):
    stack=deque()
    result=" "

    for ch in expr:

        #Operand
        if ch.isalnum():
            result+=ch
        
        #opening bracket
        elif ch=='(':
            stack.append(ch)
        
        #closing bracket
        elif ch==')':
            while stack and stack[-1] != '(':
                result+=stack.pop()
            stack.pop()

        #operator
        else:
            while stack and precedence(ch) <= precedence(stack[-1]):
                result+=stack.pop()
            stack.append(ch)
        
    while stack:
        result+=stack.pop()

    return result

expr = "a+(b*c-(d/e^f)*g)*h"
postfix = infix_to_postfix(expr)
print(f"Postfix: {postfix}")