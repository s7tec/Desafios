# Desafio 4: Palíndromo Detector

print("Digite uma palavra ou uma frase Palídromo")
string = input ("-")

string = string.casefold()

rev_string = reversed(string)

if list(string) == list(rev_string):
    print("A String eh um palíndromo")
else:
    print("Não eh um palíndromo")