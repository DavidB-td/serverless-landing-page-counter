const API_URL = 'https://jnfsg3lf9i.execute-api.us-east-2.amazonaws.com/contador';

const btnClique = document.getElementById('btn-clique');
const valorContador = document.getElementById('valor');

// 1. Função para buscar a quantidade atual no backend
async function buscarContadorAtual() {
    try {
        const response = await fetch(API_URL, { method: 'GET' });
        if (response.ok) {
            const data = await response.json();
            valorContador.innerText = data.quantidade || data.hits || 0;
        }
    } catch (error) {
        console.error('Erro ao buscar contador:', error);
    }
}

// 2. Função para atualizar o estado visual do botão caso já tenha sido clicado
function verificarStatusClique() {
    if (sessionStorage.getItem('jaClicou')) {
        desabilitarBotao();
    }
}

function desabilitarBotao() {
    btnClique.disabled = true;
    btnClique.style.opacity = '0.6';
    btnClique.style.cursor = 'not-allowed';
}

// 3. Evento acionado quando a página carrega
document.addEventListener('DOMContentLoaded', () => {
    buscarContadorAtual();
    verificarStatusClique();
});

// 4. Evento de clique para incrementar o contador
btnClique.addEventListener('click', async () => {
    // Trava preventiva se já clicou nesta sessão
    if (sessionStorage.getItem('jaClicou')) return;

    desabilitarBotao();

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const data = await response.json();
            valorContador.innerText = data.quantidade || data.hits;
            
            // Marca no sessionStorage após o sucesso da requisição
            sessionStorage.setItem('jaClicou', 'true');
        } else {
            console.error('Erro na requisição');
            // Restaura o botão caso ocorra erro na API
            btnClique.disabled = false;
            btnClique.style.opacity = '1';
            btnClique.style.cursor = 'pointer';
        }
    } catch (error) {
        console.error('Erro de conexão:', error);
        btnClique.disabled = false;
        btnClique.style.opacity = '1';
        btnClique.style.cursor = 'pointer';
    }
});