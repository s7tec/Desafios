#Desafio 1: Calculadora Básica de Descontos
print("Produtos Preços e descontos!")
print("__________________________________________________")

produto = int(input('Digite o valor do produto: R$ '))
desconto = int(input('Digite o valor de desconto: \n(ex: 10 para 10%) \n-'))
valorDesconto = (desconto * produto ) / 100
valorFinal = produto - valorDesconto

print(f"O valor do produto cheio: R${produto} \nO desconto e de {desconto}% \nValor com desconto aplicado: R${valorFinal}")