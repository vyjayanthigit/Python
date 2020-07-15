listNum = input("Enter Numbers seperated by comma")
newList = list(listNum.split(","))

firstElement = newList[0]
lastElement = newList[-1]

if int(firstElement) == int(lastElement):
    print("both are equal")
else:
    print("not equal")
