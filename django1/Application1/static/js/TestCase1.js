let Default_or_Extended = "Default";

function updateLinks() {
    const selectedOption = document.querySelector('input[name="Info"]:checked').value;
    const links = document.querySelectorAll('.server-link');
    
    links.forEach(link => {
        const index = link.textContent.split('.')[0]; // Получаем индексы из текста ссылки
        link.href = `server/${index}/${selectedOption}`; // Обновляем href
    });
    
    ChangeText(); // Изменяем текст на основе выбранного значения
}

function ChangeText() {
    document.querySelector(".settextbox").textContent = Default_or_Extended;
}

// Обновление выбранного значения при клике на радио-кнопку
document.querySelectorAll('input[name="Info"]').forEach((radio) => {
    radio.addEventListener('change', () => {
        Default_or_Extended = radio.value;
        updateLinks(); // Обновляем ссылки при изменении radio
    });
});