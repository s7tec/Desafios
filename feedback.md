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
