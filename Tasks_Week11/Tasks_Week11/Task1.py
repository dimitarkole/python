def genCodeDict():
    codeDict = dict()
    codeDict["A"] = 0
    codeDict["E"] = 9
    codeDict["O"] = 3
    codeDict["P"] = 5
    codeDict["D"] = 6
    codeDict["H"] = 6
    codeDict["I"] = 4
    codeDict["N"] = 7
    return codeDict;

def genCodeText(text):
    codeDict = genCodeDict()
    print(codeDict)
    for ch in text:
        if ch in codeDict.keys():
            result = result + str(codeDict[ch])
        else:
            result = result + ch

    return result

text = input("Input your text: ")
print(genCodeText(text))