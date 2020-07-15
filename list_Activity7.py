listNum = input("Enter Numbers seperated by comma")
newList = list(listNum.split(","))
sum = 0
for lst in newList:
    sum+=int(lst)

print(sum)