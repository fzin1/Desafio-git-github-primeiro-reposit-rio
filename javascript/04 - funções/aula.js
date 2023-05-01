

function escrevaMeuNome(nome) {
    return 'Meu nome é ' + nome;

}
function verificaridade(idade) {
    if (idade >= 18) {
        return 'e eu sou maior de idade'
    } else {
        return 'e eu sou menor de idade'
    }
}
(function main() {
    console.log(escrevaMeuNome('Fabrício ') + verificaridade(21));
})()



