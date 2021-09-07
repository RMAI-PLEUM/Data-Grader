Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # set of Operators
Priority = {'+':1, '-':1, '*':2, '/':2} # dictionary having priorities 


def infix2postfix(exp): #input exp

    stack = [] # initially stack empty
    output = '' # initially output empty

    for ch in exp:
        if ch not in Operators:  # if an operand then put it directly in postfix exp
            output+= ch

        elif ch=='(':  # else Operators should be put in stack
            stack.append('(')

        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            # lesser Priority can't be on top on higher or equal Priority    
             # so pop and put in output   
            while stack and stack[-1]!='(' and Priority[ch]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output

exp = input('Enter infix exp ')

print('infix exp: ',exp)

print('postfix exp: ',infix2postfix(exp))