numeros = [45, 12, 89, 3, 27, 56, 91, 14, 7, 66, 38, 22, 5, 73, 10]

for i in range(len(numeros)):
    menor = i

    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[menor]:
            menor = j

    numeros[i], numeros[menor] = numeros[menor], numeros[i]

print("Array ordenado com Selection Sort:")
print(numeros)