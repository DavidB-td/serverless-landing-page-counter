// Será mudado automaticamente pelo script

const API_URL = 'TROCA_SCRIPT/contador';

const btnClique = document.getElementById('btn-clique');
const valorContador = document.getElementById('valor');

// Buscar contagem atual no back-end

async function buscarContadorAtual() {
    try {
        const response = await fetch(API_URL, { method: 'GET' });
        if (response.ok) {
            const data = await response.json();
            valorContador.innerText = data.quantidade !== undefined ? data.quantidade : 0;
        }
    } catch (error) {
        console.error('Erro ao buscar contador:', error);
    }
}

function verificarStatusClique() {
    if (localStorage.getItem('jaClicou')) {
        desabilitarBotao();
    }
}

function desabilitarBotao() {
    btnClique.disabled = true;
    btnClique.style.opacity = '0.6';
    btnClique.style.cursor = 'not-allowed';
}

function habilitarBotao() {
    btnClique.disabled = false;
    btnClique.style.opacity = '1';
    btnClique.style.cursor = 'pointer';
}

document.addEventListener('DOMContentLoaded', () => {
    buscarContadorAtual();
    verificarStatusClique();
});

btnClique.addEventListener('click', async () => {
    if (localStorage.getItem('jaClicou')) return;

    desabilitarBotao();

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const data = await response.json();
            valorContador.innerText = data.quantidade;
            
            localStorage.setItem('jaClicou', 'true');
        } else {
            console.error('Erro na resposta do servidor');
            habilitarBotao();
        }
    } catch (error) {
        console.error('Erro de conexão com a API:', error);
        habilitarBotao();
    }
});
