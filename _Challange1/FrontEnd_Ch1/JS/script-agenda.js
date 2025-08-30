// JS para pop-ups de agendamento na agenda.html

document.addEventListener('DOMContentLoaded', function() {
    const agendarButtons = document.querySelectorAll('.agenda--data-botao .button--cadastro');
    
    agendarButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            alert('Consulta agendada com sucesso!');
        });
    });
});
