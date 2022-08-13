import string

import Stack_copy as st


def calculaction(exp):
    S = st.Stack(50)
    operators = ['(', ')', '^', '*', '/', '%', '//', '+', '-']
    tokenlist = exp.split()
    print(tokenlist)
    for ch in tokenlist:
        if ch in operators:
            opt1 = S.pop()
            opt2 = S.pop()
            if ch == '+':
                S.push(opt1 + opt2)
            elif ch == '-':
                S.push(opt1 - opt2)
            elif ch == '*':
                S.push(opt1 * opt2)
            elif ch == '/':
                S.push(opt1 / opt2)
            elif ch == '%':
                S.push(opt1 % opt2)
            elif ch == '^':
                S.push(opt1 ^ opt2)
        elif ch.isdigit():
            S.push(float(ch))

    print(exp, ":-", S.pop())

def evaluction():
    S = st.Stack(50)
    exp = input('Enter the infix Expression')
    operators = ['(', ')', '^', '*', '/', '%', '//', '+', '-']
    valuetable = {'+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '%': 2, '^': 3}
    output = []
    tokenlist = exp.split()
    print(tokenlist)
    k = string.digits, string.ascii_uppercase

    for token in tokenlist:
        if token in k:
            output.append(k)
        elif token == '(':
            S.push(token)
        elif token == ')':
            toptoken = S.pop()
            while toptoken != '(':
                output.append(token)
                toptoken = S.pop()
        else:
            while (not S.isempty()) and (operators[S.peek()] >= valuetable[token]):
                output.append(S.pop())
            S.push(token)

    while not S.isempty():
        output.append(S.pop())

    return ' '.join(output)


k = evaluction()
print(k)
