let alimento = document.getElementById("#descricaoAlimentoTabela").value;
let porcao = document.getElementById("#porcao").value;

let alimentosjs = []
function adicionarAlimento(){
    alimentosjs.push({alimento,porcao})
}