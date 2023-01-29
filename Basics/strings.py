text = "I know how to program in python"
print("sabe" in text) # true

size = len("python")
print(size)

text = text.upper()
print(text)

text = text.lower()
print(text)

text = text.swapcase()
print(text)

text = text.replace("python","Go")
print(text)

text = text.count("A")
print(text)


# Format print
template = "numb1"
template2 = "numb2"
print("test {} and test {}".format(template,template2))

number = 5.2489
print("test {0:.2}".format(number))

# f-string
print (f"testing again {template} {template2}")

number2 = 9.4589
print (f"testing again {number:.2} and {number2:.1f}")



def createTitle(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'unknown'
    

name = " Mr. Ronald , Mercado"
    
print(createTitle(name))





