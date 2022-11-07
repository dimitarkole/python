import random

numbers = []
numbersCount = 10#int(input("Count of numbers"))
for i in range(0,numbersCount):
    numbers.append(random.randint(0,100))

print(numbers)
index = 1
for i in range(0,numbersCount-1):
    sum = numbers[index-1] + numbers[index]
    numbers.insert(index, sum)
    index+=2

print(numbers)