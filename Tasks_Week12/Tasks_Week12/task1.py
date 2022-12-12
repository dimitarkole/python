from tkinter import N

def inputPositiveNumber():
    number = int(input())
    if(number < 0):
        inputPositiveNumber()
    return number

def inputNumbers(n):
    numbers = list()
    for i in range(0,n):
        number = int(input())
        numbers.append(number)

    return numbers

def getNumbersMoreThanK(numbers, k):
    result = list()
    for number in numbers:
        if number > k:
            result.append(number)

    return result

def getProductOfElements(numbers):
    result = 1
    for i in len(numbers):
        if i % 2 == 1:
            result *= numbers[i]

    return result

def getMinElementIndex(numbers):
    minElement = numbers[0]
    minElementIndex = 0
    for i in len(numbers):
        if minElement > numbers[i]:
            minElement = numbers[i]
            minElementIndex = i

    return minElementIndex

def getMinElement(numbers):
    minElement = numbers[0]
    for i in len(numbers):
        if minElement > numbers[i]:
            minElement = numbers[i]

    return minElement

def getMaxElement(numbers):
    maxElement = numbers[0]
    for i in len(numbers):
        if maxElement < numbers[i]:
            maxElement = numbers[i]

    return maxElement

def getNumbersLessThanK(numbers, k):
    result = list()
    for number in numbers:
        if number < k & number > 0:
            result.append(number)

    return result

def task1():
    n = inputPositiveNumber()
    k = inputPositiveNumber()
    numbers = inputNumbers(n)
    numbersMoreThanK = getNumbersMoreThanK(numbers, k)
    print(numbersMoreThanK)
    product = getProductOfElements(numbersMoreThanK)
    print(product)
    minElementIndex = getMinElementIndex(numbersMoreThanK)
    print(minElementIndex)
    numbersLessThanK = getNumbersLessThanK(numbers, k)
    print(numbersLessThanK)
    maxElement = getMaxElement(numbersLessThanK)
    minElement = getMinElement(numbersLessThanK)
    print(maxElement - minElement)

task1()