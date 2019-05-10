const inputTombo = document.getElementById("tombo");
const inputTitulo = document.getElementById("titulo");
const inputIdSocio = document.getElementById("idsocio");
const inputSocio = document.getElementById("socio");

inputTombo.addEventListener("keyup", () => {
    let tombo = inputTombo.value;
    getTitulo(tombo);
});

inputIdSocio.addEventListener("keyup", () => {
    let id = inputIdSocio.value;
    getNome(id);
});

function getNome(id) {
    fetch(`http://localhost:5000/socio/nome/${id}/emprestimo`)
        .then(response => response.json())
        .then(json => { 
            inputSocio.value = json.nome;
        })
        .catch(err => {
            inputSocio.value = '';
        });
}

function getTitulo(tombo) {
    fetch(`http://localhost:5000/livro/get_nome/${tombo}`)
        .then(response => response.json())
        .then(json => { 
            inputTitulo.value = json.titulo;
        })
        .catch(err => {
            inputTitulo.value = '';
        });
};