### Desafio 4: Palíndromo Detector
#### Curiosidades que eu não conhecia neste desafio

---
**Python casefold**
O casefold() o método em Python é usado para converter uma string em sua forma minúsculamas é mais agressivo e completo em comparação com o lower() método. Este método é particularmente útil para comparações de strings insensíveis a maiúsculas e minúsculas e para lidar com caracteres não ASCII, como a letra alemã ‘’ ‘’, que é convertida em ss. Aqui estão alguns pontos-chave sobre o casefold() método:

Sintaxe: str.casefold()
Parâmetros: Não toma nenhum parâmetro.
Valor Retorno: Ele retorna uma nova string com todos os caracteres convertidos em minúsculas.
Por exemplo, se você tiver uma string text = "pYtHon", usando text.casefold() irá convertê-lo para 'python'.

O casefold() o método é mais agressivo porque converte mais caracteres em minúsculas em comparação com o lower() método. Isso faz com que seja uma escolha melhor para comparações de strings insensíveis a casos e para lidar com casos especiais em alguns idiomas.

---
**Python revertida**
Em Python, o reversed() função retorna um iterador que acessa a sequência dada em ordem inversa. Essa função pode ser aplicada a listas, tuplas e strings, mas não a conjuntos, já que os conjuntos não são ordenados. Por exemplo, para reverter uma lista, você pode usar reversed() da seguinte forma:

```original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
```
Alternativamente, você pode reverter uma string usando reversed() e então junte os personagens novamente:

```original_string = "hello"
reversed_string = ''.join(reversed(original_string))
print(reversed_string)  # Output: "olleh"
```
---