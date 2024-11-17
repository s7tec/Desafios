#Desafio 3: Verificador de Números Primos
print("Verificador de números 'Primos'")
print("__________________________________________________")

num = int(input('Digite um número: '))


if num <= 1:
    print(f"O número {num} não é primo")

elif num <= 3:
    print(f"O número {num} é primo")

elif num % 2 == 0:
    print(f"O número {num} não é primo")

else:
    for i in range(2, int(num**0.5) + 1):
       if num % i == 0:
        print(f"O número {num} não é primo")
        break
    else:
        print(f"O número {num} é primo")