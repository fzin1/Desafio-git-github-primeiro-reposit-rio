
const valor_etanol = 5.79;
const valor_gasolina = 6.66;
const tipo_combustivel = 'etanol'
const kM_L = 10;
const distancia = 100;
const valor_gasto_etanol = (distancia / kM_L) * valor_etanol
const valor_gasto_gasolina = (distancia / kM_L) * valor_gasolina

if (tipo_combustivel === 'etanol') {
    console.log(valor_gasto_etanol.toFixed(2));
} else if (tipo_combustivel === 'gasolina') {
    console.log(valor_gasto_gasolina.toFixed(2));
}

