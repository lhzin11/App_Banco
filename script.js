// Simulação de banco de dados
let contas = [];

// Event listener para criação de conta
document.getElementById('criar-conta-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const saldo = parseFloat(document.getElementById('saldo').value);

    // Simulação de geração de ID (pode ser substituído por lógica real de ID único)
    const id = Math.floor(Math.random() * 1000000);

    // Criar objeto de conta
    const novaConta = { id: id, nome: nome, saldo: saldo };

    // Adicionar conta ao array de contas
    contas.push(novaConta);

    // Atualizar lista de contas na interface
    atualizarListaDeContas();

    // Limpar campos do formulário
    document.getElementById('nome').value = '';
    document.getElementById('saldo').value = '';
});

// Event listener para depositar
document.getElementById('depositar-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const id = parseInt(document.getElementById('depositar_id').value);
    const valor = parseFloat(document.getElementById('valor_depositar').value);

    // Encontrar conta pelo ID
    const conta = contas.find(c => c.id === id);

    if (conta) {
        // Depositar valor na conta
        conta.saldo += valor;
        // Atualizar lista de contas na interface
        atualizarListaDeContas();
    } else {
        alert('Conta não encontrada.');
    }

    // Limpar campos do formulário
    document.getElementById('depositar_id').value = '';
    document.getElementById('valor_depositar').value = '';
});

// Event listener para sacar
document.getElementById('sacar-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const id = parseInt(document.getElementById('sacar_id').value);
    const valor = parseFloat(document.getElementById('valor_sacar').value);

    // Encontrar conta pelo ID
    const conta = contas.find(c => c.id === id);

    if (conta) {
        // Verificar se há saldo suficiente
        if (conta.saldo >= valor) {
            // Sacar valor da conta
            conta.saldo -= valor;
            // Atualizar lista de contas na interface
            atualizarListaDeContas();
        } else {
            alert('Saldo insuficiente.');
        }
    } else {
        alert('Conta não encontrada.');
    }

    // Limpar campos do formulário
    document.getElementById('sacar_id').value = '';
    document.getElementById('valor_sacar').value = '';
});

// Função para atualizar a lista de contas na interface
function atualizarListaDeContas() {
    const contasLista = document.getElementById('contas-lista');
    contasLista.innerHTML = ''; // Limpar lista

    // Adicionar cada conta à lista
    contas.forEach(conta => {
        const li = document.createElement('li');
        li.textContent = `${conta.nome}: R$ ${conta.saldo.toFixed(2)}`;
        contasLista.appendChild(li);
    });
}
