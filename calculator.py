


def convertToNum(exp):
    num = 0 
    i = len(exp)-1
    value =1 
    while i>=0:
        num = num + (int(exp[i])*value)
        value=value*10
        i=i-1
    return num

def convertToString(exp):
    if exp==" ":
        return ""
    return exp[0]

def convert(expression):
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    elements = []

    i = 0
    while i <len(expression):
        increment = 1

        if expression[i] in nums:
            while i+increment<len(expression) and expression[i+increment] in nums:
                increment=increment+1
            number = convertToNum(expression[i:i+increment])
            elements.append(number)
        else:
            s = convertToString(expression[i])
            if (s!=""):
                elements.append(s)
        i=i+increment



    
    return elements


def isNumber(element):
    return type(element)==type(0)

def isOperator(element):
    operators=["+","-","*"]
    return element in operators


def add(element1, element2):
    return element1+element2

def subtract(element1, element2):
    return element1-element2

def multiply(element1, element2):
    return element1*element2

def calculate(elements):
    if (elements[1]=="+"):
        return add(elements[0],elements[2])
    elif elements[1]=="-":
        return subtract(elements[0],elements[2])
    elif elements[1]=="*":
        return multiply(elements[0],elements[2])
    

def evaluate(elements):
    while len(elements)>1:
        i=0
        while i< len(elements):
            if elements[i]==" ":
                pass
            elif isOperator(elements[i]):
                if i-1<0 or i+1>=len(elements):
                    return "INVALID"
                elif isNumber(elements[i-1]) and isNumber(elements[i+1]):
                    answer = calculate(elements[i-1:i+2])
                    elements.pop(i+1)
                    elements.pop(i)
                    elements.pop(i-1)
                    elements.insert(i-1, answer)
                    i=len(elements)
                else:
                    return "INVALID"
            i=i+1
    return elements[0]




while(True):
    print("Enter expression:")
    exp = input()
    if exp=="exit":
        break
    elements = convert(exp)
    #print(elements)
    print(evaluate(elements))

