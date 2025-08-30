// Máscara de CPF

function mascaraCPF(input) {
    let value = input.value.replace(/\D/g, '');
    if (value.length > 11) value = value.slice(0, 11);
    value = value.replace(/(\d{3})(\d)/, '$1.$2');
    value = value.replace(/(\d{3})(\d)/, '$1.$2');
    value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    input.value = value;
}

// Validação e envio do formulário

window.addEventListener('DOMContentLoaded', function() {
    const formCadastro = document.querySelector('.form--cadastro');
    if (formCadastro) {
        // Adiciona a máscara de CPF ao campo correspondente

        const cpfInput = formCadastro.querySelector('#cpf');
        if (cpfInput) {
            cpfInput.addEventListener('input', function() {
                mascaraCPF(this);
            });
        }
        formCadastro.addEventListener('submit', function(e) {
            e.preventDefault();
            const campos = formCadastro.querySelectorAll('.form--input');
            let preenchido = true;
            campos.forEach(campo => {
                if (!campo.value) preenchido = false;
            });
            if (preenchido) {
                alert('Cadastro realizado com sucesso!');
                window.location.href = 'menu.html';
            } else {
                // Verifica e destaca campos não preenchidos
                
                let msg = 'Preencha todos os campos corretamente:';
                campos.forEach(campo => {
                    if (!campo.value) {
                        campo.style.border = '2px solid #e53935';
                        msg += `\n- ${campo.previousElementSibling ? campo.previousElementSibling.innerText : campo.name}`;
                    } else {
                        campo.style.border = '';
                    }
                });
                alert(msg);
            }
        });
    }
});
