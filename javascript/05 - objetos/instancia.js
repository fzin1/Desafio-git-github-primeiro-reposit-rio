//criando classe
//dentro de classe não preciso usar o function
// isso é uma definição
// constructor define como deve ser um objeto pra ele entrar na classe

class pessoa {
    nome;
    idade;
    anodenascimento;

    constructor(nome,idade){
        this.nome = nome
        this.idade = idade
        this.anodenascimento = 2023 - idade
    }

    descrever(){
    
        console.log(`Meu nome é ${this.nome}, minha idade é ${this.idade} e eu nasci no ano de ${this.anodenascimento} `);
    }
}

//como instanciar uma pessoa nova

const fabricio = new pessoa(`Fabrício R Silva`, 21);
const milena = new pessoa(`Milena Lugão`, 20);
const jp = new pessoa('Joao Pedro', 21);



