class Stack:
    """ General stack implementation using a Python list at the end. """
    def __init__(self):
        self._items = []

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def isEmpty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            e = self._items.pop()
        except IndexError:
            print("Empty stack exception")
            return

        return e

    def top(self):
        return self._items[-1]


valStk = Stack()
opStk = Stack()

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

def brac(exp):
    temp = list()
    for z in exp:
        if z == '(':
            temp.append(exp.index(z))
            exp[exp.index(z)] = '{'
    return temp

def ket(exp):
    temp = list()
    for z in exp:
        if z == ')':
            temp.append(exp.index(z))
            exp[exp.index(z)] = '}'
    return temp


 
def repeatOps(refOp):
    while (not opStk.isEmpty()) and (prec(refOp) <= prec(opStk.top())):
        doOp()

        
def evaluate_infix_exp(exp):
    front = list()
    back = list()
    front = brac(exp)
    back = ket(exp)
    for i in range(front[-1]+1,back[0]):
        if exp[i].isdigit():
            valStk.push(exp[i])
        else:
            repeatOps(exp[i])
            opStk.push(exp[i])
    repeatOps("$")
    del exp[front[-1]:back[0]+1]
    exp.insert(front[-1],str(valStk.pop()))



    
    for z in exp:
        if z.isdigit():
            valStk.push(z)                    
        else:
            repeatOps(z)
            opStk.push(z)
    repeatOps("$")

    return valStk.top()

if __name__ == "__main__":
    exp = ["(","3","+","4",")","*","5"]
    temp = exp.copy()
    result = int(evaluate_infix_exp(temp))
    print("Exp {} evaluates {}".format("".join(exp), result))
