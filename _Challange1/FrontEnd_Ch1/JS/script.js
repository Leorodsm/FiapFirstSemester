// Dados dos desenvolvedores

const devsData = {
    poli: {
        nome: 'Poliana Batista Sarmento',
        rm: '565321',
        turma: '1TDSPH',
        foto: 'IMG/poli.jpg',
        linkedin: 'https://www.linkedin.com/in/poliana-sarmento-9472a0283/',
        github: 'https://github.com/polianasarm'
    },
    leo: {
        nome: 'Leonardo Rodrigues Martins',
        rm: '552417',
        turma: '1TDSPH',
        foto: 'IMG/leo.jpeg',
        linkedin: 'https://www.linkedin.com/in/leonardo-rodrigues-0913b5219/',
        github: 'https://github.com/Leorodsm'
    },
    celo: {
        nome: 'Marcelo Alexandre dos Santos',
        rm: '565465',
        turma: '1TDSPJ',
        foto: 'IMG/celo.jpg',
        linkedin: 'https://www.linkedin.com/in/celoselado/',
        github: 'https://github.com/celoselado'
    }
};

// Função para abrir o modal


function abrirModalDev(devKey) {
    const dev = devsData[devKey];
    if (!dev) return;
    const modalContent = document.getElementById('devs-modal-content');
    modalContent.innerHTML = `
        <img src="${dev.foto}" alt="Foto ${dev.nome}" class="devs--modal-foto">
        <div class="devs--modal-nome">${dev.nome}</div>
        <div class="devs--modal-rm">Rm: ${dev.rm}</div>
        <div class="devs--modal-icones">
            <a href="${dev.linkedin}" target="_blank"><img src="IMG/link.png" alt="LinkedIn"></a>
            <a href="${dev.github}" target="_blank"><img src="IMG/git.png" alt="GitHub"></a>
        </div>
        <div class="devs--modal-turma">${dev.turma}</div>
    `;
    document.getElementById('devs-modal-bg').style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

// Função para fechar o modal

function fecharModalDev() {
    document.getElementById('devs-modal-bg').style.display = 'none';
    document.body.style.overflow = '';
}

// Adiciona eventos aos botões

window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.devs--saiba-mais').forEach(btn => {
        btn.addEventListener('click', function() {
            abrirModalDev(this.getAttribute('data-dev'));
        });
    });
    // Fecha modal ao clicar no fundo escuro

    document.getElementById('devs-modal-bg').addEventListener('click', function(e) {
        if (e.target === this) fecharModalDev();
    });
});
