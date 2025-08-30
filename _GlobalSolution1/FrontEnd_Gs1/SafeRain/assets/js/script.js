// FAQ - Mostrar/Ocultar respostas
function toggleResposta(element) {
    const resposta = element.nextElementSibling;
    resposta.classList.toggle('ativa');
}

// Validação simples do formulário de contato
document.getElementById('form-contato').addEventListener('submit', function(event) {
    event.preventDefault();
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();

    if (nome === '' || email === '' || mensagem === '') {
        alert('Por favor, preencha todos os campos.');
    } else {
        document.getElementById('msg-sucesso').classList.remove('oculto');
        this.reset();
    }
});

// Função para abrir abas no sistema de tabs
function abrirAba(aba) {
    var i, conteudos, botoes;
    conteudos = document.getElementsByClassName("tab-content");
    for (i = 0; i < conteudos.length; i++) {
        conteudos[i].style.display = "none";
    }
    botoes = document.getElementsByClassName("tab-btn");
    for (i = 0; i < botoes.length; i++) {
        botoes[i].classList.remove("active");
    }
    document.getElementById(aba).style.display = "block";
    event.currentTarget.classList.add("active");
}

// LocalStorage para mensagens de contato
function armazenarMensagem() {
    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const mensagem = document.getElementById("mensagem").value.trim();

    if (nome === '' || email === '' || mensagem === '') {
        alert('Por favor, preencha todos os campos.');
    } else {
        const msg = { nome, email, mensagem, data: new Date().toLocaleString() };
        let mensagens = JSON.parse(localStorage.getItem("mensagensContato")) || [];
        mensagens.push(msg);
        localStorage.setItem("mensagensContato", JSON.stringify(mensagens));
        alert('Mensagem enviada com sucesso!');
        document.getElementById("form-contato").reset();
    }
}

// Cadastro de usuário
function cadastrar() {
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const senha = document.getElementById('senha').value.trim();

    if (email === '' || senha === '' || nome === '') {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    const usuario = { nome, email, senha };
    localStorage.setItem('usuarioCadastrado', JSON.stringify(usuario));
    alert('Cadastro realizado com sucesso!');
    document.getElementById('cadastroForm').reset();
    window.location.href = 'login.html';
}

//Login 
function login() {
    const email = document.getElementById('email').value.trim();
    const senha = document.getElementById('password').value.trim();

    if (email === '' || senha === '') {
        alert('Por favor, preencha todos os campos.');
        return;
    }

     const usuarioSalvo = JSON.parse(localStorage.getItem('usuarioCadastrado'));
    if (usuarioSalvo && usuarioSalvo.email === email && usuarioSalvo.senha === senha) {
        alert('Login realizado com sucesso!');
        window.location.href = 'index.html';
    } else {
        alert('E-mail ou senha incorretos!');
    }
}