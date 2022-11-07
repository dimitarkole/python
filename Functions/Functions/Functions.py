def CountOfUpperLetters(text):
    count = 0
    for x in text:
        if (x >= 'A' and x<='Z'):
            count = count + 1
    return count

def CountOfLowerLetters(text):
    count = 0
    for x in text:
        x.isLower()
        if (x >= 'a' and x<='z'):
            count = count + 1
    return count

def CountOfLetters(text):
    print("Upper letters are: ", CountOfUpperLetters(text))
    print("Lower letters are: ", CountOfLowerLetters(text))

def UniqueList(inputList):
    uniqueList = list()
    for x in inputList:
        if (not uniqueList.__contains__(x)):
            uniqueList.append(x)
    return uniqueList

def IsMonotonicInc(list):
    listLen = len(list)
    return (IsMonotonicDec(list) or IsMonotonicInc(list))

def IsMonotonicInc(list):
    listLen = len(list)
    for i in range(0, listLen-1):
        if list[i] > list[i+1]:
            return False
    return True

def IsMonotonicDec(list):
    listLen = len(list)
    for i in range(0, listLen-1):
        if list[i] > list[i+1]:
            return True
    return True

def IsMonotomnaS(l):
    y = l.sort()
    r = l.sort(reverse = True)
    if (y == l  or r == l): 
        return True
    else:
        return False

def OddAndEven(numbers):
    numbersLen = len(numbers)
    for i in range(0, numbersLen):
        number = int(numbers[i])
        if(number % 2 == 0):
            print(i, "Even")
        else:
            print(i,  "Odd")

#myList = list()
#myList.append("a")
#myList.append("b")
#myList.append("c")
#myList.append("v")
#print(IsMonotomnaS(myList))

numbers = list()
numbers.append(1)
numbers.append(2)
numbers.append(5)
numbers.append(3)
OddAndEven(numbers)