## Desafio 1: Calculadora Básica de Descontos
Escreva um programa em Python que:

Pergunte ao usuário o preço de um produto.
Pergunte a porcentagem de desconto (ex: 10 para 10%).
Calcule o valor final do produto com o desconto aplicado.
Mostre o valor original, o valor do desconto e o preço final do produto.
Dicas:

- Você vai precisar da função input() para capturar as entradas.
- Para calcular o valor do desconto, multiplique o preço pelo percentual e divida por 100.
- Use print() para exibir os resultados.

### Desafio 2: Conversor de Temperaturas
Escreva um programa em Python que converta uma temperatura dada em graus Celsius para Fahrenheit e Kelvin.

**Requisitos**:
1. Solicite ao usuário uma temperatura em graus Celsius.
2. Converta essa temperatura para:
   - **Fahrenheit** usando a fórmula: `F = (C * 9/5) + 32`
   - **Kelvin** usando a fórmula: `K = C + 273.15`
3. Exiba o resultado com as duas temperaturas (em Fahrenheit e Kelvin).

**Exemplo de Saída**:
```
Digite a temperatura em Celsius: 25
Temperatura em Fahrenheit: 77.0 °F
Temperatura em Kelvin: 298.15 K
```

**Dicas**:
- Use `float` para garantir que a entrada e o resultado possam ter casas decimais.
- Formate a saída para duas casas decimais para uma exibição mais precisa (como `77.00` e `298.15`).

### Desafio 3: Verificador de Números Primos
Escreva um programa em Python que determine se um número fornecido pelo usuário é primo.

**Requisitos**:
1. Solicite ao usuário um número inteiro positivo.
2. Verifique se o número é primo. Um número é considerado primo se for maior que 1 e divisível apenas por 1 e ele mesmo.
3. Informe o resultado ao usuário:
   - Exemplo de saída para um número primo:  
     `O número 7 é primo.`
   - Exemplo de saída para um número não primo:  
     `O número 8 não é primo.`

**Dicas**:
- Utilize um laço de repetição para verificar os divisores do número.
- Considere usar a função `range(2, número)` para verificar se o número tem divisores além de 1 e ele mesmo.
- Caso o usuário digite um número inválido (como um número negativo ou caractere não numérico), mostre uma mensagem de erro e peça para ele tentar novamente.

---

**Exemplo de Fluxo**:

Entrada:
```
Digite um número inteiro positivo: 7
```

Saída:
```
O número 7 é primo.
```

Entrada:
```
Digite um número inteiro positivo: 8
```

Saída:
```
O número 8 não é primo.
```

---
Vamos ao **Desafio 4**! Este desafio vai introduzir um conceito um pouco mais avançado: **manipulação de strings**.

---

### Desafio 4: Palíndromo Detector

Escreva um programa que verifique se uma palavra ou frase é um **palíndromo**.  
Um palíndromo é uma palavra, frase ou sequência que pode ser lida da mesma forma de trás para frente, ignorando espaços, pontuação e diferenças entre maiúsculas e minúsculas.

**Requisitos**:
1. Solicite ao usuário uma palavra ou frase.
2. Remova os espaços e caracteres especiais, considerando apenas letras e números.
3. Verifique se o texto é igual de trás para frente.
4. Informe o resultado ao usuário:
   - Exemplo de saída para um palíndromo:  
     `"A mãe te ama" é um palíndromo.`
   - Exemplo de saída para um não-palíndromo:  
     `"Python é incrível" não é um palíndromo.`

**Dicas**:
- Use métodos de strings, como `.lower()` para tratar letras maiúsculas/minúsculas.
- Para remover espaços e caracteres especiais, utilize `replace()` ou uma compreensão de lista.
- Use slicing (`[::-1]`) para inverter a string.

---

**Exemplo de Fluxo**:

Entrada:
```
Digite uma palavra ou frase: A sacada da casa
```

Saída:
```
"A sacada da casa" é um palíndromo.
```

Entrada:
```
Digite uma palavra ou frase: Python
```

Saída:
```
"Python" não é um palíndromo.
```

---

### Desafio 5: Contador de Palavras

Escreva um programa que conte o número total de palavras em uma frase fornecida pelo usuário e identifique a palavra que aparece mais vezes. Caso todas as palavras tenham a mesma frequência, informe isso também.

---

**Requisitos**:
1. Solicite ao usuário que insira uma frase.
2. Conte quantas palavras existem na frase.
3. Identifique qual palavra aparece mais vezes ou informe que todas aparecem apenas uma vez.
4. Exiba os resultados de forma clara.

---

**Exemplo de Fluxo**:

Entrada:
```
Digite uma frase: O rato roeu a roupa do rei de Roma
```

Saída:
```
Número total de palavras: 9
Todas as palavras aparecem apenas uma vez.
```

---

Entrada:
```
Digite uma frase: A casa é azul, e a casa é bonita
```

Saída:
```
Número total de palavras: 9
A palavra que mais aparece é "casa", com 2 ocorrências.
```

---

**Dicas**:
1. Use o método `.split()` para separar as palavras da frase.
2. Normalize as palavras (converta para minúsculas e remova pontuações) para evitar contagens inconsistentes.
3. Use um dicionário para contar as ocorrências de cada palavra.
4. Utilize `max()` para encontrar a palavra mais frequente no dicionário.

---
