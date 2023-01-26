'''
Date: 23 Jan 2023
Ronald Mercado
LaSalle College
Topic: Sequence // String

'''

### Sequence of characters

msg = "I´m a student"
msg2 = 'I\´m a student'
print(id(msg2))

msg2 = "I´m a teacher"

print(id(msg2))


print("********  Traverse into a sequence")

print(msg[0])
print(msg[1])
print(msg[2])
print(msg[3])
print(msg[4])
print(msg[-1])# to go from the rigth to left
print(msg[-2]) 


print("********  Slice a sequence")

print(msg2[8:])

msg3 = msg2.upper()

print(msg3)
print(msg3[4:5])

### I´m A student

msg4 = msg2[:4] + "A" + msg2[5:]
print (msg4)



msg5 = "introduction to Python"

print(msg5.count('py'))
print(msg5.count('Py'))

print(msg5.find("o"))
print(msg5.find("o",5))


shopping = "fish, Meat, Water, Veg"

myList = shopping.split(", ")
print(myList)

msg6 = "     hello   "

print(msg6.strip()) # Remove spaces 


## next class input / String Format / F-String