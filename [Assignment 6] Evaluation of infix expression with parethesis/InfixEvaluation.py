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
    count =0
    front = list()
    back = list()
    while True:
        count = count +1
        #print("count : " ,count)
        front = brac(exp)
        back = ket(exp)
        if front == [] and back == []:
            break
        temp = list()
        #print("frontblock_Index: {}, backblock_Index: {}".format(front,back))
        for i in front:
            if i < back[0]:
                temp.append(i)
        for i in range(temp[-1]+1,back[0]):
            if exp[i].isdigit():
                valStk.push(exp[i])
            else:
                repeatOps(exp[i])
                opStk.push(exp[i])
        repeatOps("$")
        #print("{} = {}".format("".join(exp[temp[-1]:back[0]+1]), valStk.top()))
        del exp[temp[-1]:back[0]+1]
        exp.insert(temp[-1],str(valStk.pop()))
        for i in exp:
            if i == '{':
                exp[exp.index(i)] = '('
            elif i == '}':
                exp[exp.index(i)] = ')'
        #print("Exp : {}".format("".join(exp)))
        #print("\n")

    
    for z in exp:
        if z.isdigit():
            valStk.push(z)                    
        else:
            repeatOps(z)
            opStk.push(z)
    repeatOps("$")

    return valStk.top()

if __name__ == "__main__":
    exp = ['(', '(', '5', '+', '3', ')', '/', '2', '+', '3', '*', '(', '2', '+', '7', ')', ')']
    temp = exp.copy()
    result = int(evaluate_infix_exp(temp))
    print("Exp {} evaluates {}".format("".join(exp), result))
