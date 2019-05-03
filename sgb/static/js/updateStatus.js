const inputTombo = document.getElementById("tombos");
const inputTitulo = document.getElementById("titulo");
const inputStatusAntigo = document.getElementById("statusAntigo");

inputTombo.addEventListener("click", () => {
    let selectedOptionIndex = inputTombo.selectedIndex;
    let selectedOptions = inputTombo.options;
    let tombo = selectedOptions[selectedOptionIndex].text;
    getTitulo(tombo);
});

function getTitulo(tombo){
    fetch(`http://localhost:5000/livro/get_nome/${tombo}`)
        .then(response => response.json())
        .then(json => { 
            inputTitulo.value = json.titulo;
            inputStatusAntigo.value = json.status;
        });
};