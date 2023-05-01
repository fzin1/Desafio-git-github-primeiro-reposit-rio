const preçoetiqueta = 100

function aplicardesconto(valor, desconto) {
    return (valor - (valor * (desconto / 100)));
}
function aplicarjuros(valor, juros) {
    return (valor + (valor * juros / 100))
}
function verificarpagamento(pagamento) {
    switch (pagamento) {
        case 1: 
        console.log('Deu um total de '+ aplicardesconto(preçoetiqueta, 10) + ' reais')
            break;

        case 2: console.log('Deu um total de '+ aplicardesconto(preçoetiqueta, 15) + ' reais')
            break;

        case 3: console.log('Deu um total de '+ preçoetiqueta + ' reais')
            break;
            
        case 4: console.log('Deu um total de '+ aplicarjuros(preçoetiqueta, 10) + ' reais')
        break;
}
}

verificarpagamento(4)