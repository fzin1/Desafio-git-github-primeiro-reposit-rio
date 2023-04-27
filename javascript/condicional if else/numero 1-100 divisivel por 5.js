
//como ler numero de 1-100 divisivel por 5
const numero = 110;
const isdivisivelpor5 = (numero % 5) === 0;
//usa esse is para definir como booleano



if(numero === 0){
    console.log('numero invalido');
} else if(numero>100){
    console.log('numero invalido');      
} else if (divisivelpor5){
    console.log('sim');
} else {
    console.log('não');
}





