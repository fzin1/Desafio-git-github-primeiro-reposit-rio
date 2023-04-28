const nota1 = 4
const nota2 = 4
const nota3 = 4
const media = (nota1 + nota2 + nota3) / 3

if (media < 5) {
    console.log('Sua média foi : ', media, ', está reprovado.')
} else if (media >= 5 && media <= 7) {
    console.log('Sua média foi : ', media, ', está de recuperação.')
} else {
    console.log('Sua média foi : ', media, ', está aprovado!!')
}

