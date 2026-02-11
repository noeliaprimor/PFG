document.addEventListener("DOMContentLoaded", function () {
    
    // CUESTIONARIOS

    const quizDataContainer = document.getElementById('quiz-data');
    const form = document.getElementById('quiz-form');
    const resultContainer = document.getElementById('result-container');
    const submitButton = document.getElementById('submit-btn');
    const resultBox = document.querySelector('.result-box');
    const resultText = document.getElementById('result-text');
    const resultMessage = document.getElementById('result-message');
    const resetButton = document.getElementById('reset-btn');

    // Obtener preguntas y respuestas desde el contenedor HTML
    const questions = Array.from(quizDataContainer.children);

    questions.forEach((question, index) => {
        const pregunta = question.getAttribute('data-question');
        const opciones = Array.from(question.children).filter(child => child.hasAttribute('data-option'));
        const respuesta = question.querySelector('[data-answer]').getAttribute('data-answer');
        const extra = question.querySelector('[data-extra]');
        const radioGroup = `question_${index}`;
        let questionHTML = `
            <fieldset class="quiz-fieldset">
                <legend class="quiz-legend">${pregunta}</legend>`;
        
        if (extra !== null) {
            questionHTML += `
                <img class="img-evaluacion" src="${extra.getAttribute('data-extra')}">`;
            
        }
        questionHTML += `${opciones.map(opcion => `<label class="quiz-label"><input style="margin-right: 13px" type="radio" name="${radioGroup}" value="${opcion.getAttribute('data-option')}">${opcion.textContent}</label><br>`).join('')}</fieldset>`;
        form.innerHTML += questionHTML;
    });

    resetButton.disabled = true;

    submitButton.addEventListener('click', function (event) {
        event.preventDefault();
        showResults();
        submitButton.disabled = true; // Deshabilitar el botón de enviar
        resetButton.disabled = false; // Deshabilitar el botón de enviar
    });

    resetButton.addEventListener('click', function (event) {
        resetQuiz();
        submitButton.disabled = false; // Habilitar el botón de enviar
        resetButton.disabled = true; // Deshabilitar el botón de enviar
    });

    function showResults() {
        let correctAnswers = 0;
        
        questions.forEach((question, index) => {
            const respuesta = question.querySelector('[data-answer]').getAttribute('data-answer');
            const selectedAnswer = document.querySelector(`input[name="question_${index}"]:checked`);
            const options = document.querySelectorAll(`input[name="question_${index}"]`);
            
            options.forEach(option => {
                const parentLabel = option.parentElement;
                if (option.value === respuesta) {
                    parentLabel.style.color = 'green'; // Respuesta correcta
                    parentLabel.innerHTML += ' ✅'; // Icono de check verde
                }
                if (selectedAnswer && selectedAnswer.value === option.value && option.value !== respuesta) {
                    parentLabel.style.color = 'red'; // Respuesta incorrecta
                    parentLabel.innerHTML += ' ❌'; // Icono de X roja
                }
            });

            if (selectedAnswer && selectedAnswer.value === respuesta) {
                correctAnswers++;
            }
        });

        const percentage = (correctAnswers / questions.length) * 100;
        const resultTextContent = `Respuestas correctas: ${correctAnswers} / ${questions.length} (${percentage.toFixed(2)}%)`;

        // Mensajes personalizados
        let message = '';
        if (percentage >= 0 && percentage <= 25) {
            message = "Deberías volver a repasar los conceptos. ¡Sigue intentándolo!";
        } else if (percentage > 25 && percentage <= 50) {
            message = "Todavía puedes hacerlo mejor!";
        } else if (percentage > 50 && porcentaje <= 75) {
            message = "No está mal, pero puedes seguir mejorando";
        } else if (percentage > 75 && percentage <= 85) {
            message = "¡Muy bien! Has entendido los conceptos, ¡sigue esforzándote!";
        } else if (percentage > 85 && percentage <= 100) {
            message = "¡Excelente! Tu comprensión ha sido perfecta!";
        }

        // Mostrar resultados en la caja
        resultText.textContent = resultTextContent;
        resultMessage.textContent = message;
        resultBox.style.display = 'block';
    }

    function resetQuiz() {
        // Limpiar respuestas seleccionadas y resultados
        form.reset();
        resetStyles();
        resultBox.style.display = 'none';
    }

    function resetStyles() {
        const labels = form.querySelectorAll('.quiz-label');
        labels.forEach(label => {
            label.style.color = ''; // Restaurar color original
            label.innerHTML = label.innerHTML.replace(' ✅', '').replace(' ❌', ''); // Quitar iconos
        });
    }

    
});
