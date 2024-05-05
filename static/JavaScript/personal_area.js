document.addEventListener("DOMContentLoaded", function() {
    const loginMenu = document.querySelector(".login-menu .login");
    const signInText = document.querySelector(".login-menu .login .sign-in");
    const signUpText = document.querySelector(".login-menu .login .sign-up");
    const indicator = document.querySelector(".login-menu .login .indicator");


    // Функция для перемещения индикатора к указанному тексту
    function moveIndicator(target) {
        const targetRect = target.getBoundingClientRect(); // Получаем координаты целевого текста
        const loginMenuRect = loginMenu.getBoundingClientRect(); // Получаем координаты родительского элемента
        const indicatorWidth = indicator.offsetWidth; // Получаем ширину индикатора

        // Находим центр текста
        const textCenter = targetRect.left - loginMenuRect.left + targetRect.width / 2;
        // Перемещаем индикатор к центру текста
        const newX = textCenter - indicatorWidth / 2;

        // Перемещаем индикатор в новое положение
        indicator.style.transform = `translateX(${Math.round(newX)}px)`; // Округляем до целого числа
    }

    // Функция для обработки клика по тексту "Sign In"
    function handleSignInClick() {
        moveIndicator(signInText); // Перемещаем индикатор к тексту "Sign In"
        signInText.style.color = "#000"; // Черный цвет для "Sign In"
        signInText.style.zIndex = "999"; // Установка z-index для "Sign In"
        signUpText.style.color = "#fff"; // Белый цвет для "Sign Up"
        signUpText.style.zIndex = ""; // Сброс z-index для "Sign Up"
    }

    // Функция для обработки клика по тексту "Sign Up"
    function handleSignUpClick() {
        moveIndicator(signUpText); // Перемещаем индикатор к тексту "Sign Up"
        signUpText.style.color = "#000"; // Черный цвет для "Sign Up"
        signUpText.style.zIndex = "999"; // Установка z-index для "Sign Up"
        signInText.style.color = "#fff"; // Белый цвет для "Sign In"
        signInText.style.zIndex = ""; // Сброс z-index для "Sign In"
    }

    // Начальное положение индикатора на тексте "Sign In"
    moveIndicator(signInText);

    // Установка начального цвета и z-index для "Sign In" и "Sign Up"
    signInText.style.color = "#000"; // Черный цвет для "Sign In"
    signInText.style.zIndex = "999"; // Установка z-index для "Sign In"
    signUpText.style.color = "#fff"; // Белый цвет для "Sign Up"

    // Обработчики событий для текстов "Sign In" и "Sign Up"
    signInText.addEventListener("click", handleSignInClick);
    signUpText.addEventListener("click", handleSignUpClick);


    const eyesImage = document.querySelector('.eyes');
const closedEyesImage = document.querySelector('.closed-eyes');
const passwordInput = document.getElementById('passwordInput');

closedEyesImage.addEventListener('click', function() {
    passwordInput.type = 'text';
    closedEyesImage.style.display = 'none';
    eyesImage.style.display = 'block';
});

eyesImage.addEventListener('click', function() {
    passwordInput.type = 'password';
    eyesImage.style.display = 'none';
    closedEyesImage.style.display = 'block';
});





const confirmEyesImage = document.querySelector('.confirm-eyes');
const confirmClosedEyesImage = document.querySelector('.confirm-closed-eyes');
const passwordConfirmInput = document.getElementById('passwordConfirmInput');

confirmClosedEyesImage.addEventListener('click', function() {
    passwordConfirmInput.type = 'text';
    confirmClosedEyesImage.style.display = 'none';
    confirmEyesImage.style.display = 'block';
});

confirmEyesImage.addEventListener('click', function() {
    passwordConfirmInput.type = 'password';
    confirmEyesImage.style.display = 'none';
    confirmClosedEyesImage.style.display = 'block';
});


});