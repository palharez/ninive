const inputRg = document.getElementById("rg");
const inputNome = document.getElementById("nome");
const inputStatusAntigo = document.getElementById("statusAntigo");

inputRg.addEventListener("click", () => {
    let selectedOptionIndex = inputRg.selectedIndex;
    let selectedOptions = inputRg.options;
    let rg = selectedOptions[selectedOptionIndex].text;
    getNome(rg);
});

function getNome(rg){
    fetch(`http://localhost:5000/socio/get_nome/${rg}`)
        .then(response => response.json())
        .then(json => { 
            inputNome.value = json.nome;
            inputStatusAntigo.value = json.status;
        });
};