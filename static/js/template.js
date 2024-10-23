 // Efecto de scroll suave para los enlaces de anclaje
 document.querySelectorAll('#menu a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Ocultar el logo al hacer scroll y ajustar la altura del header
window.addEventListener('scroll', function() {
    const header = document.getElementById('header');
    const logo = document.getElementById('logo');
    const menu = document.getElementById('menu');
    const scrollPosition = window.scrollY;

    if (scrollPosition > 50) {
        logo.style.opacity = '0'; // Desvanecer el logo
        header.style.height = '50px'; // Ajustar altura del header a la del menú
        menu.style.transition = 'height 0.3s'; // Transición suave para el menú
    } else {
        logo.style.opacity = '1'; // Mostrar el logo
        header.style.height = 'auto'; // Restablecer altura del header
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabId = button.getAttribute('data-tab');

            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            button.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // Set the first tab as active by default
    if (tabButtons.length > 0) {
        tabButtons[0].classList.add('active');
        tabContents[0].classList.add('active');
    }
});