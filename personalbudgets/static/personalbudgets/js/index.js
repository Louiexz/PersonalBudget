// Função para definir o tema no localStorage
function setLocalStorage(tema) {
    localStorage.setItem('tema', tema);
}

// Função para obter o tema do localStorage
function getLocalStorage() {
    return localStorage.getItem('tema');
}

// Aplica o tema armazenado antes do carregamento completo da página
(function applySavedTheme() {
    const savedTheme = getLocalStorage();
    const html = document.getElementsByTagName('html')[0];
    
    // Se um tema estiver salvo, aplica-o
    if (savedTheme) {
        html.setAttribute('data-bs-theme', savedTheme);
        if (savedTheme === 'dark') {
            document.querySelector('body').style.color = '#ffd';
            document.querySelector('.summary').style.backgroundColor = '#001';
        } else {
            document.querySelector('body').style.color = '#001';
            document.querySelector('.summary').style.backgroundColor = '#eee';
        }
    }
})();

// Evento de clique para alternar entre os temas
document.getElementById('toggle-mode').addEventListener('click', () => {
    const html = document.getElementsByTagName('html')[0];

    if (html.getAttribute('data-bs-theme') !== 'dark') {
        html.setAttribute('data-bs-theme', 'dark');
        document.querySelector('body').style.color = '#ffd';
        document.querySelector('.summary').style.backgroundColor = '#001';
        setLocalStorage('dark'); // Armazena o tema "dark"
    } else {
        html.setAttribute('data-bs-theme', 'light');
        document.querySelector('body').style.color = '#001';
        document.querySelector('.summary').style.backgroundColor = '#eee';
        setLocalStorage('light'); // Armazena o tema "light"
    }
});