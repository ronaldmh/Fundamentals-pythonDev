myList = ["juan","luciana","lina","ronald"]
print(myList[2])

myList.append("montreal")
print(myList[-1])

#A ddition of list

myList2 = [1,5,6,7,8,1]

myList3 = myList + myList2
print(myList3)

# index

index = myList3.index(7)
print(index)
# Update a value in a specific position
myList3[index] = 39
print(myList3)