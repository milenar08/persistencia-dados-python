texto = list()

texto.append("Python é uma linguagem poderosa.")
texto.append("Manipulação de arquivos em Python.")
texto.append("Persistência de dados com Python.")

with open("texto.txt", "w", encoding="utf-8") as arquivo:
    for linha in texto:
        arquivo.write(linha + "\n")

print("Arquivo texto.txt criado com sucesso!")