# Ejercicio 1: Suma de los primeros N números
N = int(input("Ingrese un número N: "))
suma = 0
for i in range(1, N + 1):
    suma += i
print(f"La suma de los primeros {N} números naturales es: {suma}")

# Ejercicio 2: Factorial de un número
num = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es: {factorial}")

# Ejercicio 3: Tabla de multiplicar
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 4: Cálculo de promedio de notas
suma_notas = 0
contador = 0
while True:
    nota = float(input("Ingrese una nota (ingrese un número negativo para terminar): "))
    if nota < 0:
        break
    suma_notas += nota
    contador += 1
if contador > 0:
    promedio = suma_notas / contador
    print(f"El promedio de las notas ingresadas es: {promedio:.2f}")
else:
    print("No se ingresaron notas válidas.")


# Ejercicio 5: Serie de Fibonacci
N = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
a, b = 0, 1
print("Serie de Fibonacci:")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()

# Ejercicio 6: Potencia de un número
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = 1
for _ in range(abs(exponente)):
    resultado *= base
if exponente < 0:
    resultado = 1 / resultado
print(f"{base}^{exponente} = {resultado}")

# Ejercicio 7: Suma de números pares en un rango
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
suma_pares = 0
for i in range(A, B + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de los números pares entre {A} y {B} es: {suma_pares}")