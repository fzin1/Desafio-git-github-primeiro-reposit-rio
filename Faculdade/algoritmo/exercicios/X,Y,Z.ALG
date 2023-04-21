Algoritmo "x,y,z"

Var
x, y: inteiro  //definindo X e Y como inteiros
z: real // definindo Z como real


Inicio

leia (x) // comando para o usuário digitar o valor de X
escreva(x, " elevado ao cubo = ", x^3) // colocando na tela o resultado
escreval(" ") //comando pra pular linha (não consegui com \n)
leia (y) // usuário digita o valor de Y
escreva(x + y)  // coloca na tela o resultado de x + y
escreval(" ")   // pular linha
z <- x/y  // define Z como x/y
escreva (z)  // coloca Z na tela

z <- z + 1 // define Z como z + 1

x <- (y + x) mod 2  // define X como o resto de (x + y)/2
escreval(" ")  // pula linha
escreva(x)  // coloca o valor de X na tela

fimalgoritmo