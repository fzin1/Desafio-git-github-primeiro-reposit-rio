
//como ler numero de 1-100 divisivel por 5

function divisivel(numero,divisor){
    if (numero % divisor === 0){
        console.log(`${numero} é divisivel por ${divisor}`)
    }else if(numero % divisor !== 0){
        console.log(numero + ' não é divisivel por ' + divisor)
    }
    }
    
    divisivel(11,5)
    