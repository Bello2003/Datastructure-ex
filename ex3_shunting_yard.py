def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack, output = [], []
    for token in expression:
        if token.isalnum():
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1],0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ''.join(output)

print(infix_to_postfix("A*(B+C)"))
