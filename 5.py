# Desafio 5: Contador de Palavras
print("Contador de Palavras")
frase = input("Digite uma frase: ")

palavras_min = frase.casefold()
palavras = palavras_min.split()
cont_palavras = len(palavras)

contagem = {}

# Conta as palavras
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

# Encontra a palavra mais frequente
mais_frequente = max(contagem, key=contagem.get)

print(f"A palavra mais frequente é '{mais_frequente}', com {contagem[mais_frequente]} ocorrências.")
print(palavras)
