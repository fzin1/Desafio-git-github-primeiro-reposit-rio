
const valor_etanol = 5.79;
const valor_gasolina = 6.66;
const tipo_combustivel = 'gasolina'
const kM_L = 10;
const distancia = 100;
let valor

if (tipo_combustivel === 'etanol') {
    valor = (distancia / kM_L) * valor_etanol
} else if (tipo_combustivel === 'gasolina') {
    valor = (distancia / kM_L) * valor_gasolina
}

console.log(valor)