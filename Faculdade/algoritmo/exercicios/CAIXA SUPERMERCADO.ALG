Algoritmo "caixa supermercado"
// 
//  
// Descrição   : caixa supermecado
// Autor(a)    : Fabricio
// Data atual  : 11/04/2023
Var

valor_produto,valor_total_produto,total_compra,num_produto: real


Inicio

valor_total_produto <- 0

escreva("Por favor, digite o número do produto: ")
leia (num_produto)

enquanto num_produto > 0 faça

total_compra <- total_compra + 1

escreva("Por favor, digite o valor do produto: ")
leia (valor_produto)

valor_total_produto <- valor_produto + valor_total_produto

escreval()
escreva("Por favor, digite o número do novo produto: ")
leia (num_produto)

fimenquanto

se valor_total_produto = 1 então

escreval()
escreval("Você possui ",total_compra," itens no seu carrinho")
escreval()
escreva("O valor total da sua compra foi",valor_total_produto," real.")
escreval()

senao

escreval()
escreval("Você possui ",total_compra," itens no seu carrinho")
escreval()
escreva("O valor total da sua compra foi",valor_total_produto," reais.")
escreval()

fimse


Fimalgoritmo