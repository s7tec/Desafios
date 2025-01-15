## Feedback Desafio 1
Você fez um ótimo trabalho ao implementar a lógica para calcular o desconto e exibir o valor final. O código está muito bom e funciona corretamente! Aqui estão alguns pontos de feedback para tornar o código ainda mais robusto:

1. **Verificar o Tipo de Dados**:
   - Atualmente, você usa `int` para o preço e o desconto. Isso funcionará bem, mas se você quiser suportar valores com centavos (ex: `199.99`), o tipo `float` pode ser mais adequado. Usar `float` permite que o usuário insira valores decimais para o preço ou desconto.

2. **Nomes de Variáveis**:
   - Os nomes das variáveis estão bons, mas você pode usar o padrão `snake_case` (por exemplo, `valor_desconto` em vez de `valorDesconto`). Esse é o estilo mais comum em Python.

3. **Formatar a Saída do Valor Final**:
   - Quando você exibe o `valorFinal`, ele pode ter muitos dígitos após o ponto decimal. Para exibir apenas duas casas decimais, você pode usar `:.2f` no `f-string`. Exemplo: `R${valorFinal:.2f}`.

4. **Tratamento de Erros (Opcional)**:
   - Para tornar o código ainda mais seguro, considere verificar se o usuário está inserindo números válidos (não negativos e não letras, por exemplo). Isso pode ser feito com `try/except` para capturar entradas incorretas.

Essas são sugestões de melhoria, mas no geral você cumpriu todos os objetivos do desafio!

## Feedback Desafio 2
Excelente trabalho! Seu código está bem escrito e executa a conversão corretamente. Aqui vai o feedback com alguns pontos de observação e sugestões de melhorias:

1. **Tratamento de Erros**:
   - A verificação de erro foi uma ótima inclusão! No entanto, observe que, se houver um `ValueError`, o programa ainda tenta calcular as conversões com `c`, mesmo que ele não tenha sido definido corretamente. Para resolver isso, você pode mover as conversões para dentro do bloco `try` ou adicionar uma condição para só executar as conversões caso a entrada seja válida.

2. **Número de Casas Decimais**:
   - No `f-string` de Kelvin, você usou `:.5`, o que exibe cinco dígitos no total (exemplo: `298.15`). Se deseja mostrar duas casas decimais, pode usar `:.2f` para mais consistência com o Fahrenheit. Exemplo: `{k:.2f} K`.

3. **Melhoria no Nome da Variável**:
   - `numero` poderia ter um nome mais claro, como `temperatura_celsius`, para que o propósito fique ainda mais evidente.

4. **Feedback ao Usuário em Caso de Erro**:
   - Depois de exibir `"Erro: Você deve apenas digitar apenas numeros"`, você pode parar a execução usando `exit()` ou um `return` para que o programa termine logo após a mensagem de erro, evitando seguir para os cálculos.

No geral, o código atende bem ao objetivo do desafio! Se quiser que eu te passe o próximo, só avisar!

## Feedback Desafio 3
Você está no caminho certo e a maior parte do seu código está funcional! No entanto, há um problema no fluxo lógico que faz com que a mensagem de "primo" seja exibida mesmo para números não primos, dependendo de como o loop `for` é executado. Aqui vai o feedback detalhado:

---

### Pontos Positivos:
1. **Verificação Inicial**:
   - Você tratou os casos em que o número é menor ou igual a 1, bem como os números 2 e 3 separadamente, o que é eficiente e correto.

2. **Uso da Raiz Quadrada**:
   - Limitar o loop até a raiz quadrada de `num` com `int(num**0.5) + 1` é uma ótima otimização para verificar a primalidade.

3. **Conceito do `for`**:
   - Usar um `for` para checar divisores é correto, mas falta uma pequena correção na forma como o fluxo decide se o número é primo.

---

### Ajustes Necessários:
1. **Erro na Lógica do `for`**:
   - O `else` do `for` está sendo executado para todos os casos onde o loop termina sem interrupção, mas isso não reflete se um número é primo corretamente. 
   - Para corrigir, você pode usar uma variável (ex.: `é_primo`) para rastrear se o número é primo.

2. **Melhoria na Saída**:
   - Caso o número seja detectado como não primo dentro do `for`, o programa imprime a mensagem de "não primo" várias vezes (uma para cada divisor encontrado). Isso pode ser ajustado para exibir a mensagem apenas uma vez.

---

### Versão Ajustada:

Aqui está uma abordagem corrigida com as suas ideias:

```python
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
    é_primo = True  # Assume que o número é primo
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            é_primo = False
            break  # Interrompe o loop assim que encontra um divisor

    if é_primo:
        print(f"O número {num} é primo")
    else:
        print(f"O número {num} não é primo")
```

---

### Pontos para Reflexão:
1. **Por que usar `break`?**  
   Interromper o loop assim que encontramos um divisor economiza processamento, especialmente para números grandes.

2. **Mensagens de Saída Duplicadas**:  
   No seu código original, o `else` do `for` foi executado independentemente de o número ser primo ou não. Essa é uma armadilha comum, porque o `else` do `for` em Python executa somente se o loop não for interrompido por um `break`.
---
## Feedback Desafio 4
Ótimo trabalho em buscar aprender mais com fontes externas! O código está funcional e verifica corretamente se uma palavra ou frase é um palíndromo. Aqui está o feedback detalhado, com sugestões de melhoria:

---

### Pontos Positivos:
1. **Uso do `casefold()`**:
   - Boa escolha! `casefold()` é ideal para lidar com comparações de strings ignorando diferenças de maiúsculas e minúsculas, especialmente em línguas com caracteres especiais.

2. **Lógica Geral**:
   - A abordagem de comparar a string com sua versão invertida é eficiente e funciona bem para palíndromos.

3. **Mensagens ao Usuário**:
   - Você incluiu mensagens claras para indicar se a string é ou não um palíndromo. Ótimo para usabilidade!

---

### Ajustes e Melhorias:
1. **Limpeza de Caracteres Especiais e Espaços**:
   - Atualmente, o código não ignora espaços e caracteres especiais. Para que frases como `"A sacada da casa"` sejam reconhecidas como palíndromos, você pode limpar a string antes da verificação:
     ```python
     import re
     string = re.sub(r'[^a-zA-Z0-9]', '', string)
     ```
     Isso removerá tudo que não for letra ou número.

2. **Comparação Mais Direta**:
   - Você converte a string invertida para uma lista antes da comparação. Isso funciona, mas não é necessário. Você pode comparar diretamente a string com sua versão invertida usando slicing:
     ```python
     if string == string[::-1]:
     ```

3. **Melhoria nas Mensagens**:
   - Seria interessante incluir a string original na mensagem, para dar mais contexto ao usuário. Por exemplo:
     ```python
     print(f'"{string}" é um palíndromo.')
     ```

4. **Erros de Digitação**:
   - A palavra "palíndromo" está com erro de digitação nas mensagens. Corrigir isso deixará o código mais polido.

---

### Versão Melhorada:
Com as sugestões acima implementadas, o código pode ficar assim:

```python
import re

print("Digite uma palavra ou uma frase para verificar se é um palíndromo:")
string = input("- ")

# Normaliza a string (ignora espaços, pontuação e diferenciação de maiúsculas/minúsculas)
string = re.sub(r'[^a-zA-Z0-9]', '', string).casefold()

# Verifica se a string é igual ao seu reverso
if string == string[::-1]:
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")
```

---
Parabéns por concluir o desafio! 🎉 Vamos ao feedback e explicação detalhada da contagem de palavras e ocorrências no seu código.

---

### Como funciona o código:
1. **Entrada do Usuário**:
   - O programa pede que o usuário digite uma frase.

2. **Normalização da Frase**:
   - O método `.casefold()` transforma toda a frase em letras minúsculas, garantindo que palavras como "Casa" e "casa" sejam tratadas da mesma forma.
   - Exemplo: `"Olá Mundo Mundo"` vira `"olá mundo mundo"`.

3. **Divisão da Frase em Palavras**:
   - O método `.split()` separa as palavras da frase usando os espaços como delimitadores.
   - Exemplo: `"olá mundo mundo"` vira `["olá", "mundo", "mundo"]`.

4. **Contagem das Palavras**:
   - Um dicionário `contagem` é usado para armazenar cada palavra como chave e o número de vezes que aparece como valor.
   - Para cada palavra da lista:
     - Se a palavra já está no dicionário, o valor dela é incrementado em 1 (`contagem[palavra] += 1`).
     - Caso contrário, a palavra é adicionada ao dicionário com valor inicial 1 (`contagem[palavra] = 1`).
   - Resultado final do dicionário:
     - Para `["olá", "mundo", "mundo"]`, o dicionário será:  
       `{"olá": 1, "mundo": 2}`.

5. **Palavra Mais Frequente**:
   - O `max(contagem, key=contagem.get)` encontra a chave (palavra) com o maior valor (frequência) no dicionário.
   - Exemplo: `max({"olá": 1, "mundo": 2}, key=contagem.get)` retorna `"mundo"`, pois `2` é o maior valor.

6. **Saída Final**:
   - O programa exibe qual palavra aparece mais vezes e sua contagem.
   - Além disso, o programa mostra a lista de palavras, o que ajuda a entender como a frase foi processada.

---

### Exemplo com Explicação:
**Entrada**:
```
Digite uma frase: O rato roeu a roupa do rei de Roma
```

**Processo**:
- Normalização: `"o rato roeu a roupa do rei de roma"`
- Divisão em palavras: `["o", "rato", "roeu", "a", "roupa", "do", "rei", "de", "roma"]`
- Contagem:
  ```python
  {
      "o": 1,
      "rato": 1,
      "roeu": 1,
      "a": 1,
      "roupa": 1,
      "do": 1,
      "rei": 1,
      "de": 1,
      "roma": 1
  }
  ```
- A palavra mais frequente: **Todas têm frequência 1**.

**Saída**:
```
A palavra mais frequente é 'o', com 1 ocorrência.
```

---

### O que poderia melhorar:
1. **Tratar Pontuações**:
   - Se a frase tiver pontuações, como `"o rato roeu a roupa do rei."`, o programa não reconhecerá `"rei."` como `"rei"`. 
   - Solução: Use `re` para remover pontuações antes de contar.

   ```python
   import re
   frase = re.sub(r'[^\w\s]', '', frase)
   ```

2. **Empate de Frequências**:
   - Caso mais de uma palavra tenha a mesma maior frequência, informe isso ao usuário.

   ```python
   frequencia_maxima = max(contagem.values())
   palavras_frequentes = [palavra for palavra, freq in contagem.items() if freq == frequencia_maxima]
   ```

3. **Exibir Total de Palavras**:
   - Mostre ao usuário o número total de palavras na frase.

   ```python
   print(f"Número total de palavras: {cont_palavras}")
   ```

---
