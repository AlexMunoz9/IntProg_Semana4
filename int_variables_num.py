
z = int(input("Ingrese el valor de la primera variable z: "))
y = int(input("Ingrese el valor de la segunda variable (y): "))


print(f"Valores originales: z = {z}, y = {y}")


x = z
z = y
y = x


print(f"Valores intercambiados: z = {z}, y = {y}")