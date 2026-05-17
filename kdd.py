import time 

# bubble sort

def bubble_sort(array):
    lista = array.copy()

    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j].lower() > lista[j + 1].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# selection sort

def selection_sort(array):
    lista = array.copy()

    for i in range(len(lista)):
        menor = i

        for j in range(i + 1, len(lista)):
            if lista[j].lower() < lista[menor].lower():
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


# leitura do .txt

palavras = []

with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.replace(",", "").replace(".", "").replace("\n", "")
        palavras.extend(linha.split())

print("Quantidade de palavras:", len(palavras))


# teste bubble sort

inicio_bubble = time.time()

resultado_bubble = bubble_sort(palavras)

fim_bubble = time.time()

tempo_bubble = fim_bubble - inicio_bubble

print("\n      BUBBLE SORT      ")
print(resultado_bubble)
print(f"Tempo de execução: {tempo_bubble:.8f} segundos")

# teste selection sort

inicio_selection = time.time()

resultado_selection = selection_sort(palavras)

fim_selection = time.time()

tempo_selection = fim_selection - inicio_selection

print("\n      SELECTION SORT      ")
print(resultado_selection)
print(f"Tempo de execução: {tempo_selection:.8f} segundos")



lista_python = palavras.copy()

inicio_python = time.time()

lista_python.sort(key=str.lower)

fim_python = time.time()

tempo_python = fim_python - inicio_python

print("\n      SORT NATIVO DO PYTHON      ")
print(lista_python)
print(f"Tempo de execução: {tempo_python:.8f} segundos")


with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo_saida:
    for palavra in lista_python:
        arquivo_saida.write(palavra + "\n")

print("\nArquivo palavras_ordenadas.txt criado com sucesso!")