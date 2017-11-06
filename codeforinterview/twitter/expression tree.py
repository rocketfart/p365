from aetypes import Enum


def reverse(ex):
    ex=list(ex[::-1])

    for i in range(len(ex)):
        if ex[i]!=')' and ex[i]!='(':
            continue
        elif ex[i]==')':
           ex[i]='('
        else:
            ex[i]=')'
    ex=''.join(ex)
    return ex

class State(Enum):
    Before = 0
    Inside = 1
    Done   = 2

def simplify(expression):
    levels = [State.Before]
    result = []

    for c in expression:
        if c == '(':
            if levels[-1] == State.Before:
                levels[-1] = State.Inside
            else:
                result.append(c)
            levels.append(State.Before)
        elif c == ')':
            levels.pop()
            if levels[-1] == State.Inside:
                levels[-1] = State.Done
            else:
                result.append(c)
        else:
            if levels[-1] == State.Before:
                levels[-1] = State.Done
            result.append(c)

    return ''.join(result)


while True:
    try:
        inputString = input()
        '''==================== Calling function solution  ======================'''
        solution(inputString)
    except EOFError:
        break

def solution(inputString):
    '''========= Remove the spaces from the input ==============='''
    # inputString = inputString.replace("\n","")
    inputString = inputString.replace(" ", "").replace("\t", "")


    '''=============== The substring before '/' is expression tree and substring after '/' is sequence of operations  ======================'''

    posOfSlash = inputString.find('/')
    if (posOfSlash == -1):
        print (inputString)
        return
    # part1 = Expression Tree
    part1 = inputString[0:posOfSlash]
    # part2 = sequence of operations to be performed
    part2 = inputString[posOfSlash + 1:]

    '''============ If sequence Of Operations is empty then print the expression tree as it is ============== '''
    if (len(part2) == 0):
        print(part1)
        return

    '''============= Removing all the pairs of RR from the sequence Of Operations =================='''
    part2 = part2.replace('RR', '')

    '''============ All mulptiple S are replaced by one single S ================'''
    while (part2.find('SS') != -1):
        part2 = part2.replace('SS', 'S')
    '''============ If to perform operation R then call operationReverse() else if to perform operation S call operationSimplify() ================'''
    for x in range(0, len(part2)):
        if (part2[x] == 'R'):
            expressionTree = operationReverse(expressionTree)
        else:
            expressionTree = operationSimplify(expressionTree)
    print(expressionTree)
    return