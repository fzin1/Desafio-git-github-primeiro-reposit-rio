Algoritmo "circulação de carros"

Var
n1, n2, media: real


Inicio

escreva ("Por favor, digite a sua 1ª nota: ")
leia (n1)
escreva ("Por favor, digite a sua 2ª nota: ")
leia (n2)
media <- (n1+n2)/2

se media >= 7 entao
escreva ("Parabéns sua média foi", media,"!!", " Você foi APROVADO!!")
fimse
se media < 7 entao
escreva ("Infelizmente a sua média foi", media, " Você foi REPROVADO.")
fimse


fimalgoritmo
