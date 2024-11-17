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