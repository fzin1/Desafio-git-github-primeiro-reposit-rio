/*
    1- crie uma classe para representar carros.
    Os carros possuem uma marca, cor e um gasto médio de combustivel por km rodado
    crie um método que dado a quantidade de km e o preço do combustivel nos de o valor gasto em reais para realizar o percurso
*/
class carro{
    marca;
    cor;
    gasto_medio_comb;
    constructor(marca,cor,gasto_medio_comb) {
        this.marca = marca
        this.cor = cor
        this.gasto_medio_comb = gasto_medio_comb
    }
    calcular_gasto(preço_comb,qtd_km){
        return(qtd_km * this.gasto_medio_comb * preço_comb)
    }
}
const jeep_renegade = new carro(`SUV`,`Vermelho`,1/12)
console.log(jeep_renegade.calcular_gasto(5,70).toFixed(2))
const palio = new carro(`Fiat`,`Preto`, 1/10)
console.log(palio.calcular_gasto(5,70).toFixed(2))

