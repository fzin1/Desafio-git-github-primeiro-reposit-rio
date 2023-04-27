
//como ler numero de 1-100 divisivel por 5

const numero = 10;

const divisivelpor5 = (numero % 5) === 0;

if(numero === 0){
    console.log('numero invalido');
} else if (divisivelpor5){
    console.log('sim');
} else {
    console.log('não');
}





