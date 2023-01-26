
### Arithmetic Operators:
x = 5
y = 3
print(x + y) # 8
print(x - y) # 2
print(x * y) # 15
print(x / y) # 1.666666
print(x // y) # 1 operator performs integer division
print(x % y) # 2
print(x ** y) # 125 (5 raised to the power of 3)

### Comparison Operators:
x = 5
y = 3
print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False

### Assignment Operators:

x = 5
x += 3 # x = x + 3
print(x) # 8
x -= 2 # x = x - 2
print(x) # 6
x *= 4 # x = x * 4
print(x) # 24
x /= 2 # x = x / 2
print(x) # 12
x %= 3 # x = x % 3
print(x) # 0
x **= 2 # x = x ** 2
print(x) # 0

### Logical Operators:

x = True
y = False
print(x and y) # False
print(x or y) # True
print(not x) # False

a = 60
b = 13
c = a & b
print('60 & 13 =', c)

### Shift Operators:

x = 10 # binary:  1010
y = x << 2 # binary: 101000 (desplazado 2 posiciones a la izquierda)
print(y) # 40

x = 10 # binary:  1010
y = x >> 1 # binary: 101 (desplazado 1 posición a la derecha)
print(y) # 5

## number negative (fill 1)
## number positive (fill 0)

### Membership Operators:

x = [1, 2, 3]
print(1 in x) # True
print(4 in x) # False
print(5 not in x) # True

### Identity Operators:

x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y) # False
print(x is z) # True
print(x is not y) # True