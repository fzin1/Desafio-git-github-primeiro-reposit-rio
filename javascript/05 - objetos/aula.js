//criando classe
//dentro de classe não preciso usar o function
// isso é uma definição
class pessoa {
    nome;
    idade;

    descrever(){
    
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade} `);
    }

}


//declarando objeto dinamicamente = fabricio.altura = 1.80;
//deletando objeto = delete fabricio.altura;
//objeto = {chave:valor}

// Isso é uma instancia

const fabricio = {
    nome: 'fabricio',
    idade: 21,
    descrever: function () {
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade} `);
    }
}






