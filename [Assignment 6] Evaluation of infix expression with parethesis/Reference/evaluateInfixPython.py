import Stack

'''
Evaluating infix expression, where expression is represented by a list,
each of which is an operator or an integer operand.
'''

valStk = Stack.Stack()
opStk = Stack.Stack()

def doOp():
    op = opStk.pop()
    y = int(valStk.pop())
    x = int(valStk.pop())
    if op == "+":
        valStk.push(x + y)
    elif op == "-":
        valStk.push(x - y)
    elif op == "*":
        valStk.push(x * y)
    else:   # division
        valStk.push(x / y)


def prec(op):
    if op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1
    elif op == "$":
        return 0
    else:
        raise ValueError

        
def repeatOps(refOp):
    while (not opStk.isEmpty()) and (prec(refOp) <= prec(opStk.top())):
        doOp()

        
def evaluate_infix_exp(exp):
    for z in exp:
        if z.isdigit():
            valStk.push(z)
        else:
            repeatOps(z)
            opStk.push(z)
    repeatOps("$")

    return valStk.top()

if __name__ == "__main__":
    exp = ["3", "+", "4", "*", "5"]
    result = evaluate_infix_exp(exp)
    print("Exp {} evaluates {}".format("".join(exp), result))
