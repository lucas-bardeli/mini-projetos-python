
import random

maiuscula = chr(random.randint(65, 90))
minuscula = chr(random.randint(97, 122))
char_especial = random.choice('!@#$%&*')
numeros = []

for i in range (5): # 5 números
    num = random.randint(0, 9)
    numeros.append(num)

random.shuffle(numeros)
numeros = str(numeros)[1:-1]
numeros = numeros.replace(',', '') 

print(f"\nSua senha é: ", maiuscula, minuscula, numeros, char_especial) # 8 dígitos, estão com espaço