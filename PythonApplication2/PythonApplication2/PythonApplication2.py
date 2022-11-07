#import math

#def CallTrapesoiteS(a,b,c,d):
#    p = (a+b+c+d)/2
#    return math.sqrt(p*(p-a)*(p-b)*(p-c)*(p-d))

#def CallTrapesoiteP(a,b,c,d):
#    return a+b+c+d

#def CallTrapesoite():
#    a = float(input("Input a:"))
#    b = float(input("Input b:"))
#    c = float(input("Input c:"))
#    d = float(input("Input d:"))
#    print("P = ", CallTrapesoiteS(a,b,c,d))
#    print("S = ", CallTrapesoiteP(a,b,c,d))

#def CallTriangleS(a,b,c):
#    p = (a+b+c)/2
#    return math.sqrt(p*(p-a)*(p-b)*(p-c))

#def CallTriangleP(a,b,c):
#    return a+b+c

#def CallTriangle():
#    a = float(input("Input a:"))
#    b = float(input("Input b:"))
#    c = float(input("Input c:"))
#    print("P = ", CallTriangleS(a,b,c))
#    print("S = ", CallTriangleP(a,b,c))

#def CallSqareP(a):
#    return 4*a;

#def CallSqareS(a):
#    return a;

#def CallSqare():
#    a = float(input("Input a:"))
#    print("P = ", CallSqareP(a))
#    print("S = ", CallSqareS(a))

#def CallRecS(a, b):
#    return a*b;

#def CallRecP(a, b):
#    return 2*(a+b);

#def CallRec():
#    a = float(input("Input a:"))
#    b = float(input("Input b:"))
#    print("S = ", CallRecS(a,b))
#    print("P = ", CallRecP(a,b))

#def CallFact(n):
#    if n < 0:
#        ArithmeticError("The number must be more than ziro.")
#    fact = 1
#    for x in range(1,n+1):
#        fact *= x
#    return fact

#def IsPalindrom(n):
#    nLen = len(n)
#    middleIndex = int(nLen/2)
#    for i in (0,middleIndex-1):
#        if(n[i] != n[nLen - 1 - i]):
#           return False
#    return True

#def Task1():
#    figure = int(input("Input figure type"))
#    if figure == 1: 
#        CallSqare()
#    elif figure == 2:
#        CallRec()
#    elif figure == 3:
#        CallTriangle()
#    elif figure == 3:
#        CallTrapesoite()

#def Task2():
#    a = float(input("Input first number:"))
#    b = float(input("Input second number:"))
#    sigh = chr(input("Input sigh:"))
#    if sigh == '+': 
#        print(a+b)
#    elif sigh == '-': 
#        print(a-b)
#    elif sigh == '*':
#        print(a*b)
#    elif sigh == '/':
#        print(a/b)
#    else: 
#        print("Error command")

#def Task3():
#    n = int(input("Input number:"))
#    print("Fact: ", CallFact(n))
##Task1()
##Task3()

#print(IsPalindrom("BoB"))
#print(IsPalindrom("Palindromordnilap"))

#print( CallTrapesoiteS(26,11,26,25))
#CallTriangleS(20, 13.09, )

text = input("Input text: ")
textDict = dict()
for x in text:
    if(not textDict.__contains__(x)):
        textDict[x] = 0
    textDict[x] +=1

print(textDict)