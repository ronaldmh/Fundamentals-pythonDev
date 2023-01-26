#sets
# not allowed duplicated elements
set_countries = {'Colombia','Mexico', 'Argentina'}
print(set_countries)
print(type(set_countries))

# set with several data types
set_elements = {10, "hola",True, 25.15}
print(set_elements)

numbers = [1,4,8,9,9,12]
set_numbers = set(numbers)
print(set_numbers)

size = len(set_countries)
print(size)

#find an element

print('Colombia' in  set_countries)

#add elements
set_countries.add("Cuba")

#Update
set_countries.update({"Brasil"})
print(set_countries)

#delete
set_countries.remove("Mexico")
print(set_countries)