const inputId = document.getElementById("id");
const inputNome = document.getElementById("nome");
const inputStatusAntigo = document.getElementById("statusAntigo");

inputId.addEventListener("click", () => {
    let selectedOptionIndex = inputId.selectedIndex;
    let selectedOptions = inputId.options;
    let id = selectedOptions[selectedOptionIndex].text;
    getNome(id);
});

function getNome(id){
    fetch(`http://localhost:5000/socio/get_nome/${id}`)
        .then(response => response.json())
        .then(json => { 
            inputNome.value = json.nome;
            inputStatusAntigo.value = json.status;
        });
};