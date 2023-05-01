/*
2 - crie uma classe para representar pessoas.
para cada pessoa teremos os atributos: nome, peso e altura;
As pessoas devem ter a capacidade de dizer o valor do seu IMC (IMC = peso/(altura * altura))
instancie uma pessoa chamada josé que tenha 70kg de peso e 1,75 de altura e peça ao josé para dizer o valor do seu IMC
*/

class pessoas {
    nome;
    peso;
    altura;

    constructor(nome, peso, altura) {
        this.nome = nome
        this.peso = peso
        this.altura = altura
    }
    calculo_de_IMC() {
        return this.peso / Math.pow(this.altura, 2)
    }
    classificar_imc() {
        const imc = this.calculo_de_IMC()
        if (imc < 18.5) {
            return ('Abaixo do peso')
        } else if (imc >= 18.5 && imc <= 25) {
            return ('Peso normal')
        } else if (imc > 25 && imc <= 30) {
            return ('Acima do peso')
        } else if (imc > 30 && imc <= 40) {
            return ('Obeso')
        } else {
            return ('Obesidade Grave')
        }
    }
}

const Jose = new pessoas(`José`, 70, 1.75)
console.log(`Eu sou o ${Jose.nome}, peso ${Jose.peso} kg, tenho ${Jose.altura} de altura e meu IMC é de ${Jose.calculo_de_IMC().toFixed(2)}, logo estou ${Jose.classificar_imc()}`)

const Fabricio = new pessoas(`Fabrício`, 54, 1.84)
console.log(`Eu sou o ${Fabricio.nome}, peso ${Fabricio.peso} kg, tenho ${Fabricio.altura} de altura e meu IMC é de ${Fabricio.calculo_de_IMC().toFixed(2)}, logo estou ${Fabricio.classificar_imc()}`)



