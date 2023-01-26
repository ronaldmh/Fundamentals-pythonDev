""" Game project"""

import random

#tupla
options = ('piedra','papel','tijera')

print("welcome")

user = input("piedra ,papel o tijera => ")
user = user.lower()
computer = random.choice(options)
print('computer chose => ', computer)    
        

if user == computer:
    print("empate")
   
elif user == "piedra" and computer == "tijera":
        print("piedra gana a tijera")
        print("user gana")
        
elif user == "papel" and computer == "piedra":
        print("papel gana a piedra")
        print("user gana")
        
elif user == "tijera" and computer == "papel":
        print("tijera gana a papel")
        print("user gana")
        
else:
    print("computer gana")

    
        


