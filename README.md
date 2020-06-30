# Python
Seus amigos inventaram um jogo chamado “Arremesso de bolas”. O objetivo é simples, basta arremessar uma bola de forma que ela caia dentro de um buraco N metros a frente.
Quando a bola é arremessada a uma velocidade inteira V, ela permanece no ar por V metros e então quica. Ela repete esse processo V vezes. Após ela quicar V vezes, ela muda sua velocidade para V-1, e o processo anterior se repete, até que a velocidade seja igual a 0.
Por exemplo, se a bola for arremessada a uma velocidade igual a 3, ela quicará nos seguintes pontos: 3, 6, 9, 11, 13, 14; conforme pode ser visto na imagem.

arremesso
É possível arremessar a bola à uma velocidade inteira igual a V. Dada a distância do buraco, diga se é possível que a bola quique exatamente no buraco, acertando-o.

Entrada
Há diversos casos de teste. Em cada caso há dois inteiros, N e V (1 ≤ N ≤ 1000, 1 ≤ V ≤ 30), representando a distância do buraco e a velocidade máxima que pode-se arremessar a bola. O último caso de teste é indicado por N = V = 0, e não deverá ser processado.

Saída
Para cada caso de teste, imprima uma linha contendo a palavra “possivel” (sem aspas), caso seja possível arremessar a bola a uma velocidade igual a V acertando o buraco, ou “impossivel”, caso contrário. Após a impressão da palavra, salte uma linha.
