import math
import datetime

def LVToUSD(lv):
    return lv * 0.52

def LVToEURO(lv):
    return lv * 0.51

def LVToLira(lv):
    return lv * 9.75

def USDToLV(usd):
    return usd*1.91

def USDToEURO(usd):
    return usd*0.98

def USDToLira(usd):
    return usd*18.62

def EuroToLV(euro):
    return euro*1.95

def EuroToUSD(euro):
    return euro*1.02

def EuroToLira(euro):
    return euro*19.07

def LiraToLV(lira):
    return lira*0.10 

def LiraToUSD(lira):
    return lira*0.054

def LiraToEuro(lira):
    return lira*0.052

def Fixing(currencyFrom, currencyTo, value):
    if currencyFrom == "LV":
        if currencyTo == "USD":
            return LVToUSD(value)
        elif currencyTo == "EURO":
            return LVToEURO(value)
        elif currencyTo == "LIRA":
            return LVToLira(value)
        else:
            AttributeError("Unexpected currency")
    elif currencyFrom == "USD":
        if currencyTo == "LV":
            return USDToLV(value)
        elif currencyTo == "EURO":
            return USDToEURO(value)
        elif currencyTo == "LIRA":
            return USDToLira(value)
        else:
            AttributeError("Unexpected currency")
    elif currencyFrom == "EURO":
        if currencyTo == "LV":
            return EuroToLV(value)
        elif currencyTo == "USD":
            return EuroToUSD(value)
        elif currencyTo == "LIRA":
            return EuroToLira(value)
        else:
            AttributeError("Unexpected currency")
    elif currencyFrom == "LIRA":
        if currencyTo == "LV":
            return LiraToLV(value)
        elif currencyTo == "USD":
            return LiraToUSD(value)
        elif currencyTo == "EURO":
            return LiraToEuro(value)
        else:
            AttributeError("Unexpected currency")
    else:
        AttributeError("Unexpected currency")

def FixingTask():
  currencyFrom = input("Input currency from: ")  
  currencyTo = input("Input currency to: ")  
  value = float(input("Input value: "))
  try:
    print(Fixing(currencyFrom, currencyTo, value))
  except AttributeError:
    print("Unexpected currency")

def RadToDegreeTask():
    radian = float(input("Input radians: "))
    degree = radian*(180/math.pi)
    print(degree)

def SmallCharsInSting(string):
    result =""
    for ch in string:
        if ch.islower():
            result += ch

    return result

def SmallCharsInStingTask():
    string = input("Input string: ")
    print(SmallCharsInSting(string))

def IsFatalDay(month, year):
    return int(datetime.datetime(year, month, 13).strftime("%w")) == 4

def FatalDayTask():
    month = int(input("Input month: "))
    year = int(input("Input year: "))
    print(IsFatalDay(month, year))

def BinToHexDict():
    binToHexDict = dict()
    binToHexDict["0000"] = "0" 
    binToHexDict["0001"] = "1" 
    binToHexDict["0010"] = "2" 
    binToHexDict["0011"] = "3" 
    binToHexDict["0100"] = "4"
    binToHexDict["0101"] = "5" 
    binToHexDict["0110"] = "6" 
    binToHexDict["0111"] = "7" 
    binToHexDict["1000"] = "8"
    binToHexDict["1001"] = "9" 
    binToHexDict["1010"] = "A" 
    binToHexDict["1011"] = "B" 
    binToHexDict["1100"] = "C"
    binToHexDict["1101"] = "D" 
    binToHexDict["1110"] = "E" 
    binToHexDict["1111"] = "F"
    return binToHexDict

def BinToHex(binNumber):
    HexResult = ""
    binToHexDict = BinToHexDict()
    binNumber=binNumber[::-1]
    partOfBinNumber = ""
    for ch in binNumber:
        partOfBinNumber += ch
        if len(partOfBinNumber) == 4:
            partOfBinNumber =partOfBinNumber[::-1]
            HexResult += binToHexDict[partOfBinNumber]
            partOfBinNumber= ""
    
    if len(partOfBinNumber) != 0:
        while len(partOfBinNumber) != 4:
            partOfBinNumber += "0"
        partOfBinNumber =partOfBinNumber[::-1]
        HexResult += binToHexDict[partOfBinNumber]

    return HexResult[::-1]

def BinToHexTask():
    binNumber = input("Input bin number: ")
    print("Hex number is: ",BinToHex(binNumber))

def SqrtTask():
    number = int(input("Input number: "))
    if number<=0:
        print("Err: Wrong number. Number must be more than 0")
    else:
        print("sqrt(number) is: ",math.sqrt(number))

BinToHexTask()