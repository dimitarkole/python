import datetime
import random

def Task1():
   now = datetime.datetime.now()
   print(now)
   return 0

def Task2():
    inputData = list(input().split('.'))
    day = datetime.datetime(int(inputData[2]), int(inputData[1]), int(inputData[0]))
    print(day.strftime("%a"))
    return 0

def IsYear(year):
    return (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)

def Task3():
    year = input("Input year")
    print(IsYear(year))
    return 0

def RandomElementFromList(list):
    listLen = int(len(list))
    index = random.randrange(listLen)
    return list[index]

def RandomElementFromDict(dict):
    return random.choice(list(dict.values()))

def Task4():
    print(RandomElementFromList([0,1,2,3,4]), RandomElementFromDict({"A":0,"B":1,"C":2,"D":3,"E":4}))

def Task5():
    for i in range(3000, 4150):
        date = datetime.datetime(i, 12, 25)
        if(int(date.strftime("%w")) == 6):
             print(date.year)

Task4()