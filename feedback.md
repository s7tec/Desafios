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