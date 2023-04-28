const valor = 100
let desconto
let valor_final
const vezes_cartao = 4
let pagamento = 2

console.log('Selecione o tipo de pagamento\n\n 1 - Débito a vista\n 2 - Dinheiro ou pix\n 3 - Crédito\n')

if (pagamento === 1){
    console.log('Débito a vista selecionado')
} else if (pagamento === 2){
    console.log('Dinheiro ou Pix selecionado')
} else{
    console.log('Crédito selecionado')
}

switch (pagamento) {

    case 1:
        desconto = valor * 0.1
        valor_final = valor - desconto
        console.log('\nFica um total de ',valor_final,' reais')
        break

    case 2: 
        desconto = valor * 0.15
        valor_final = valor - desconto
        console.log('\nFica um total de ',valor_final,' reais')
        break

    case 3:
        if (vezes_cartao > 2){
            desconto = valor * 0.1
            valor_final = valor + desconto
            console.log('\nFica um total de ',valor_final,' reais')
        } else {
            
            console.log('\nFica um total de ',valor,' reais')
        }
        break



}