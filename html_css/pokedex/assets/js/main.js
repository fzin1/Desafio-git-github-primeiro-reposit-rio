

const offset = 0
const limit = 20

const url = `https://pokeapi.co/api/v2/pokemon?offset=${offset}&limit=${limit}`

function convertpokemontoli(pokemon, numero, numeroformatado) {

    return ` <li class="pokemon">
        <span class="number">#${numeroformatado}</span>
        <span class="name">${pokemon.name}</span>

        <div class="detail">
            <ol class="types">
                <li class="type">Grass</li>
                <li class="type">Poison</li>
            </ol>
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/${numero}.svg"
                alt="${pokemon.name}">
        </div>
    </li>
`


}

//pegando a lista de pokemon e atribuindo a uma variavel
const pokemonlist = document.getElementById('pokemonol')
// innerhtml = html que ta dentro da minha lista (pokemonlist)


// requisitar algo (nesse caso a url)
fetch(url)
    //transforma em json pra poder usar no js
    .then((response) => response.json())
    .then((jsonbody) => jsonbody.results)
    .then((pokemons) => {

        for (let i = 0; i < pokemons.length; i++) {
            const pokemon = pokemons[i];

            numero = i + 1
            numeroformatado = numero.toString().padStart(3, "0")

            pokemonlist.innerHTML += convertpokemontoli(pokemon, numero, numeroformatado)

        }

    })

    //pode usar "=>" pra servir como função e diminuir o codigo ou pode usar o "function" normal

    //vai exibirse der erro
    .catch((error) => console.error(error))
    //vai acontecer quando acabar
    .finally(() => console.log("Requisição concluida"))