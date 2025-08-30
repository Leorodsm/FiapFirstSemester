// JS para validação do cadastro de pergunta no FAQ-pergunta.html

document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('.faq--textarea');

    const btnCadastrar = document.querySelector('.faq--botoes .button--cadastro');

    if (textarea && btnCadastrar) {
        btnCadastrar.addEventListener('click', function(e) {

            e.preventDefault();
            
            const texto = textarea.value.trim();

            if (texto.length < 100) {
                alert('Digite mais de 100 caracteres para cadastrar sua dúvida.');
                textarea.focus();
            } else {
                alert('Dúvida cadastrada com sucesso!!!');
                textarea.value = '';
            }
        });
    }
});
