def operationReverse(expression):

    expression = expression[::-1]
    expression = list(expression)

    for x in range(0, len(expression)):
        if (expression[x] != ')' and expression[x] != '('):
            continue
        elif (expression[x] == ")"):
            expression[x] = "("
        else:
            expression[x] = ")"

    expression = ''.join(expression)
    return expression



def operationSimplify(expression):

    if (expression.find('(') == -1):
        return expression


    if (expression[0] == '('):
        x = 1
        # numOfOpeningBrackets = maintains the count of opening brackets for finding it's corresponding closing bracket
        numOfOpeningBrackets = 1
        while (x < len(expression)):
            if (expression[x] != ')' and expression[x] != '('):
                x = x + 1
                continue
            elif (expression[x] == "("):
                numOfOpeningBrackets = numOfOpeningBrackets + 1
                x = x + 1
            else:
                numOfOpeningBrackets = numOfOpeningBrackets - 1
                if (numOfOpeningBrackets == 0):
                    posOfCloseBracket = x
                    break
                x = x + 1
        expression = operationSimplify(expression[1:posOfCloseBracket]) + expression[posOfCloseBracket + 1:]

    if (expression.find('(') == -1):
        return expression


    x = 0
    recursion = False
    numOfOpeningBrackets = 0
    while (x < len(expression)):
        if (expression[x] != ')' and expression[x] != '('):
            x = x + 1
        elif (expression[x] == "("):
            if (numOfOpeningBrackets == 0 or recursion == True):
                numOfOpeningBrackets = 0
                recursion = False
                posOfStartBracket = x
                y = x
            numOfOpeningBrackets = numOfOpeningBrackets + 1
            x = x + 1
        else:
            numOfOpeningBrackets = numOfOpeningBrackets - 1
            if (numOfOpeningBrackets == 0):
                posOfCloseBracket = x
                x = y
                expression = expression[0:posOfStartBracket + 1] + operationSimplify(
                    expression[posOfStartBracket + 1:posOfCloseBracket]) + expression[posOfCloseBracket:]
                recursion = True
            x = x + 1
    return expression


def solution(inputString):

    inputString = inputString.replace(" ", "")
    inputString = inputString.replace("\t", "")




    posOfSlash = inputString.find('/')
    if (posOfSlash == -1):
        print (inputString)
        return
    # expressionTree = Expression Tree
    expressionTree = inputString[0:posOfSlash]
    # seqOfOp = sequence of operations to be performed
    seqOfOp = inputString[posOfSlash + 1:]


    if (len(seqOfOp) == 0):
        print(expressionTree)
        return


    seqOfOp = seqOfOp.replace(r + r, '')


    while (seqOfOp.find(s + s) != -1):
        seqOfOp = seqOfOp.replace(s + s, s)


    for x in range(0, len(seqOfOp)):
        if (seqOfOp[x] == r):
            expressionTree = operationReverse(expressionTree)
        else:
            expressionTree = operationSimplify(expressionTree)
    print(expressionTree)
    return


r = 'R'
s = 'S'
while True:
    try:
        inputString = input()
        solution(inputString)
    except EOFError:
        break
