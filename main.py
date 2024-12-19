import random

elements = "+-/*!&$#?=@<>"
password = ""
pass_length = int(input("ingrese la longitud de la contraseña: "))

for i in range(pass_length):
    password += random.choice(elements)

print(password)
