#adivinar un numero
import random

numero_secreto = random.randint(1, 10)


numero_usuario = int(input("Dime número entre 1 y 10: "))

if(numero_secreto == numero_usuario):
    print("Felicides, Adivinaste el número")
else:
    print("Sigue intentando ")  
   