import Stack_copy as St


def prefix_evaluation(exp):
    S = St.Stack(50)
    # expression=input("Infix Expression: ")
    operators = ['+', '-', '*', '/', '//', '%', '^']
    rev_exp = exp[::-1]
    print(rev_exp)
    for ch in rev_exp:
        if ch in operators:
            op1 = S.pop()
            op2 = S.pop()
            if ch == '+':
                S.push(op1 + op2)
            elif ch == '-':
                S.push(op1 - op2)
            elif ch == '*':
                S.push(op1 * op2)
            elif ch == '/':
                S.push(op1 / op2)
            elif ch == '%':
                S.push(op1 % op2)
            elif ch == '^':
                S.push(op1 ^ op2)
        elif ch.isdigit():
            S.push(float(ch))

    print(exp, ":-", S.pop())


def infix_to_prefix():
    S = St.Stack(50)
    exp = input("Enter the Infix Expression: ")
    rev_exp = exp[::-1]
    print(rev_exp)
    operators = ['(', ')', '^', '*', '/', '%', '//', '+', '-']
    precedence = {'^': 3, '*': 2, '/': 2, '%': 2, '//': 2, '+': 1, '-': 1}

    output = ''
    for ch in rev_exp:
        if ch.isdigit() or ch.isalpha():
            output += ch
        if ch in operators:
            if ch == ')':
                S.push(ch)
            elif ch == '(':
                while (not S.isempty()) and S.peek() != ')':
                    c = S.pop()
                    output += c
                S.pop()
            elif S.isempty() or S.peek() == ')':
                S.push(ch)
            elif precedence[ch] > precedence[S.peek()]:
                S.push(ch)
            elif precedence[ch] < precedence[S.peek()]:
                while (not S.isempty()) and precedence[ch] < precedence[S.peek()]:
                    output += S.pop()
                S.push(ch)
            # CASES, when incoming operators has same precedence with TOP
            elif precedence[ch] == precedence[S.peek()] and ch != '^':
                S.push(ch)
            elif precedence[ch] == precedence[S.peek()] and ch == '^':
                while (not S.isempty()) and precedence[ch] == precedence[S.peek()]:
                    output += S.pop()
                S.push(ch)

    while not S.isempty():
        output += S.pop()

    rev_output = output[::-1]
    print("Prefix Form of", exp, "is", rev_output)

    prefix_evaluation(rev_output)


infix_to_prefix()
#prefix_evaluation('-+8/632')
#prefix_evaluation('-+7*45+20')
