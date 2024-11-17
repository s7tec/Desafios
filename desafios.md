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
