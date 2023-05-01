
class pessoa{
    nome;
    idade;
    ano_de_nascimento;

    constructor(nome,idade){
        this.nome = nome
        this.idade = idade
        this.ano_de_nascimento = 2023 - idade
    }
}
function comparar_pessoas(p1,p2){
if(p1.idade>p2.idade){
    console.log(`${p1.nome} é mais velho(a) que ${p2.nome}`);
} else if(p2.idade>p1.idade) {
    console.log(`${p2.nome} é mais velho(a) que ${p1.nome}`);
} else {
    console.log(`vocês tem a mesma idade`);
}
}
const fabricio = new pessoa(`Fabrício Ramos`, 21);
const milena = new pessoa(`Milena Lugão`, 20);
const jp = new pessoa(`Jõao Pedro`, 21);
const alberto = new pessoa(`Albero Akio`, 21);
const gustavo = new pessoa(`Gustavo Barbosa`, 23);
comparar_pessoas(fabricio,gustavo);