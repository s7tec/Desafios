# Desafio 2: Conversor de Temperaturas
print('Conversor de Temperaturas')

try:
    temperatura_celsius = input('Digite a temperatura em Celcius: ')
    c = float(temperatura_celsius)
except :
    print("Erro: Você deve apenas digitar apenas numeros")
    exit()

f = (c * 9/5) + 32
k = c + 273.15

print(f"Temperatura em Fahrenheit: {f:.2f} ºF \nTemperatura em Kelvin: {k:.5} K")