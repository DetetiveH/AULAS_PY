# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando a estrutura for
for numeros in numeros:
    if numeros % 2 == 0:
        print(f"{numeros} é par.")
    else:
        print(f"{numeros} é ímpar.")

# Usando a estrutura while
contador = 0
while contador < len(numeros):
    print(f"Posição {contador}: {numeros[contador]}")
    contador += 1
