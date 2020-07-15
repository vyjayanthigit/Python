listOne = [10,20,33,40,55]
listTwo = [13,44,66,77,18]

print("list one ", listOne)
print("list one ", listTwo)

thirdList = []

for lst in listOne:
    if(lst%2 != 0):
        thirdList.append(lst)
for lst in listTwo:
    if(lst%2 == 0):
        thirdList.append(lst)
print("3rd list", thirdList)