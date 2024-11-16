// Função para validar o CPF
function validarCPF() {
    // Pega o valor do input de CPF
    let cpf = document.getElementById('cpf').value;

    // Remove qualquer caractere não numérico
    cpf = cpf.replace(/\D/g, '');

    // Verifica se o CPF é válido
    if (CPF.isValid(cpf)) {
        document.getElementById('resultado').textContent = "CPF válido!";
        document.getElementById('resultado').style.color = "green";
    } else {
        document.getElementById('resultado').textContent = "CPF inválido!";
        document.getElementById('resultado').style.color = "red";
    }
}

// Adiciona um evento de input para formatar o CPF enquanto o usuário digita
document.getElementById('cpf').addEventListener('input', function() {
    let cpf = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos
    if (cpf.length <= 3) {
        this.value = cpf; // Exibe apenas os 3 primeiros números
    } else if (cpf.length <= 6) {
        this.value = cpf.slice(0, 3) + '.' + cpf.slice(3); // Adiciona o ponto após os 3 primeiros dígitos
    } else if (cpf.length <= 9) {
        this.value = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6); // Adiciona o ponto após o segundo grupo
    } else if (cpf.length <= 11) {
        this.value = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9) + '-' + cpf.slice(9, 11); // Adiciona o traço antes do último grupo
    }
});
