def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


numeros = [45, 12, 89, 3, 27, 56, 91, 14, 7, 66, 38, 22, 5, 73, 10]

bubble_sort(numeros)

print("Array ordenado com Bubble Sort:")
print(numeros)