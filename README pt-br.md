# Jogo da Forca

## Como o jogo funciona

Eu criei uma lista de 20 palavras (todas estão em inglês), e uma delas é selecionada aleatoriamente. Seu objetivo é adivinhar a palavra letra por letra.

Toda vez que você acertar uma letra, sua posição na palavra será revelada. Porém, se a letra não estiver presente na palavra, outra parte do boneco da forca aparecerá, começando pela cabeça e gradualmente completando o corpo.

Você tem 7 chances no total, e se o corpo inteiro for completado, você perde!

## Sobre o código

Mantive a interface do console dentro de uma classe. Acho que separar a interface em sua própria classe é uma boa maneira de manter o código organizado. Dessa vez, entretanto, também armazenei nela as tentativas restantes.

Para desenhar o boneco da forca, utilizei expressões condicionais de uma linha para verificar quantas tentativas restam e determinar quais partes do corpo devem aparecer. Dessa forma, você consegue visualizar quantas partes ainda faltam. Mas, se isso for muito confuso, não se preocupe! Também existe um **contador de tentativas** exibido acima do boneco.

Quanto à exibição dos sublinhados, mantive as coisas simples. A função percorre cada letra da palavra e verifica se ela está presente na lista **letter_used**. Se não estiver, um sublinhado é impresso em seu lugar. Caso contrário, a letra é revelada.

Aqui está um exemplo:

```python
word = "fish"
letter_used = ["i"]

for letter in word: # -> Percorre cada letra da palavra
    if letter in letter_used: # -> Se a letra estiver presente em letter_used
        print(f" {letter.upper()}", end=" ") # -> Imprime a letra em maiúsculo
    else:
        print(" _", end=" ") # -> Caso contrário, imprime um sublinhado
print()
```

O jogo ainda não possui um modo PvP, mas, assim como no Rock, Paper and Scizor, provavelmente vou adicioná-lo futuramente!
