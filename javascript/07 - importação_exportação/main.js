
//const funcoes = require('./funcoes-auxiliares')
const { gets, print } = require('./funcoes-auxiliares') //ele declara gets e print como variavels e atribui a importação a elas

const quantidade_total = gets()
let maior_valor = 0

for (let i = 0; i < quantidade_total; i++) {
    const numero = gets()
    if (numero > maior_valor) {
        maior_valor = numero
    }
}

print(maior_valor)
