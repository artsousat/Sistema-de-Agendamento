const botao = document.querySelector('btn');
botao.addEventListener('click', function() {
    const nome = document.querySelector('#nome').value;
    const email = document.querySelector('#email').value;
    const mensagem = document.querySelector('#mensagem').value;});

    if (nome === '' || email === '' || mensagem === '') {
        alert('Por favor, preencha todos os campos.');
    } else {
        alert('Mensagem enviada com sucesso!');
    }