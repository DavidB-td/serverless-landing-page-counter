// Substituir o valor pela URL do API Gateway
const API_URL = 'https://SUA-API.execute-api.us-east-1.amazonaws.com/prod/clique';

const btnClique = document.getElementById('btn-clique');
const valorContador = document.getElementById('valor');

btnClique.addEventListener('click', async () => {

    btnClique.disabled = true;
    btnClique.style.opacity = '0.6';
    btnClique.style.cursor = 'not-allowed';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        if (response.ok) {
            const data = await response.json();
            valorContador.innerText = data.quantidade || data.hits;
        } else {
            console.error('Erro na requisição');
        }
    } catch (error) {
        console.error('Erro de conexão:', error);
    } finally {
        // Reabilita o botão após a resposta (ou erro)
        btnClique.disabled = false;
        btnClique.style.opacity = '1';
        btnClique.style.cursor = 'pointer';
    }
});