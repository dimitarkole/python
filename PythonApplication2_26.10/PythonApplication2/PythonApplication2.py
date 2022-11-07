#inputNumber = int(input("Input number: "))
#list = list()

#for x in range(1, inputNumber+1):
#    list.append(x)

#normalTuple = tuple(list)
#reverseTuple = tuple(list[::-1])

#print("Normal: ", normalTuple)
#print("Reverse: ",reverseTuple)

#task 3
#text = input();
#dict = dict();
#for x in text:
#    if x not in dict:
#        dict[x] = 0
#    dict[x] +=1

#print(dict)
    
#task 4
#n = int(input("Enter number: "))
#lst = list()
#dict = dict();
#for i in range(1, n+1):
#    lst.append(i) 
      
#for i in range(0, n):
#    dict[lst[i]] = lst[n-i-1]
      
#print(dict)s

#task 5
def func(list, number):
    listLen = len(list)
    for i in range(0, listLen):
        if list[i] > number:
            list[i] = 0;
        
list = [1,2,100, 3,4,5,6,7,8]
num = 4
func(list,num)
print(list)

