
"""
    Date: 16 Jan 2023
    Author: Salar
    Topic: Numbers

"""

#### ================== Numbers

print("++++++++++++++ Int")
age = 23;
print(age)
print(type(age))
print(id(age))
print("\n+++++++++ After modifying object")
age = 24
print(age)
print(type(age))
print(id(age))


print("\n\n++++++++++++++ float")

price = 19.99
print(price)
print(type(price))
print(id(price))
print("\n+++++++++ After modifying object")
price = 29.99
print(price)
print(type(price))
print(id(price))

print("\n\n++++++++++++++ complex")

z = 10 + 12j
print(z)
print(type(z))
print(id(z))
print("\n+++++++++ After modifying object")
z = -100 - 200j
print(z)
print(type(z))
print(id(z))


print("\n\n\n++++++++++++++++ Casting +++++++++++")

v1 = 20.99
v2 = 150
result = 0

print(v1)
print(type(v1))
print(v2)
print(type(v2))
print("========= Casting from int to float")
v2 = float(v2)
print(v2)
print(type(v2))
print("========= Casting from float to int")
v1 = int(v1)
print(v1)
print(type(v1))

print("========= Casting from complex to int (Syntax Error)")
### z = int(z)
### print(z)
### print(type(z))
print("========= Casting from int to complex")
v1 = complex(v1)
print(v1)
print(type(v1))













































