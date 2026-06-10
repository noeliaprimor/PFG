const autoevaluacionScriptBase = (() => {
  const scripts = Array.from(document.scripts);
  const script = scripts.reverse().find((item) => item.src && /(?:^|\/)autoevaluacion\.js(?:[?#].*)?$/.test(item.src));
  return script ? new URL('.', script.src).href : './';
})();

function resolveSiteAsset(sitePath) {
  if (window.location.protocol !== 'file:') return sitePath;
  return new URL(sitePath.replace(/^\/+/, ''), autoevaluacionScriptBase.replace(/\/js\/?$/, '/')).href;
}

function loadQuestionsScript() {
  return new Promise((resolve, reject) => {
    if (window.AUTOEVALUACION_QUESTIONS) {
      resolve(window.AUTOEVALUACION_QUESTIONS);
      return;
    }

    const script = document.createElement('script');
    script.src = new URL('questions-data.js', autoevaluacionScriptBase).href;
    script.onload = () => resolve(window.AUTOEVALUACION_QUESTIONS);
    script.onerror = () => reject(new Error('No se pudo cargar questions-data.js'));
    document.head.appendChild(script);
  });
}

async function loadQuestionsData() {
  if (window.AUTOEVALUACION_QUESTIONS) return window.AUTOEVALUACION_QUESTIONS;

  if (window.location.protocol !== 'file:') {
    const response = await fetch(resolveSiteAsset('/js/questions-data.json'));
    return response.json();
  }

  return loadQuestionsScript();
}

class AutoevaluacionQuiz {
  constructor(moduleId, containerSelector = '#quiz-form') {
    this.moduleId = moduleId;
    this.containerSelector = containerSelector;
    this.questions = [];
    this.userAnswers = {};
    this.init();
  }

  async waitForContainer(timeoutMs = 6000) {
    const stepMs = 100;
    const attempts = Math.ceil(timeoutMs / stepMs);

    for (let i = 0; i < attempts; i++) {
      if (document.querySelector(this.containerSelector)) return true;
      await new Promise((resolve) => setTimeout(resolve, stepMs));
    }

    return false;
  }

  async init() {
    try {
      const ready = await this.waitForContainer();
      if (!ready) {
        console.warn(`No se encontro el contenedor ${this.containerSelector}`);
        return;
      }

      const data = await loadQuestionsData();
      this.questions = data[this.moduleId]?.preguntas || [];
      if (this.questions.length === 0) {
        console.warn(`No preguntas encontradas para ${this.moduleId}`);
        return;
      }
      this.renderQuiz();
      this.attachEventListeners();
    } catch (error) {
      console.error('Error cargando preguntas:', error);
    }
  }

  renderQuiz() {
    const container = document.querySelector(this.containerSelector);
    if (!container) return;
    container.innerHTML = '';

    this.questions.forEach((q, index) => {
      const questionDiv = document.createElement('div');
      questionDiv.className = 'quiz-question';
      questionDiv.dataset.questionIndex = String(index);
      questionDiv.innerHTML = `
        <p class="question-text"><strong>${index + 1}. ${q.pregunta}</strong></p>
        <div class="options-group">
          ${Object.entries(q.opciones)
            .map(
              ([key, value]) => `
            <label class="option-label">
              <input type="radio" name="question-${index}" value="${key}" class="option-input">
              <span>${key}. ${value}</span>
            </label>
          `
            )
            .join('')}
        </div>
      `;
      container.appendChild(questionDiv);
    });
  }

  attachEventListeners() {
    const submitBtn = document.getElementById('submit-btn');
    const resetBtn = document.getElementById('reset-btn');

    if (submitBtn) submitBtn.addEventListener('click', () => this.checkAnswers());
    if (resetBtn) resetBtn.addEventListener('click', () => this.resetQuiz());

    document.querySelectorAll('input[type="radio"]').forEach((input) => {
      input.addEventListener('change', (e) => {
        const questionIndex = e.target.name.split('-')[1];
        this.userAnswers[questionIndex] = e.target.value;
      });
    });
  }

  checkAnswers() {
    if (Object.keys(this.userAnswers).length !== this.questions.length) {
      alert('Por favor, contesta todas las preguntas.');
      return;
    }

    // Limpia feedback visual de intentos anteriores
    document.querySelectorAll('.quiz-question').forEach((q) => q.classList.remove('question-wrong'));
    document.querySelectorAll('.option-label').forEach((l) => l.classList.remove('is-incorrect'));

    let correctCount = 0;
    this.questions.forEach((q, index) => {
      const isCorrect = this.userAnswers[index] === q.respuestaCorrecta;
      if (isCorrect) {
        correctCount++;
        return;
      }

      // Resalta en rojo la pregunta fallida y la opción elegida
      const questionBlock = document.querySelector(`.quiz-question[data-question-index="${index}"]`);
      if (questionBlock) questionBlock.classList.add('question-wrong');

      const selectedInput = document.querySelector(`input[name="question-${index}"][value="${this.userAnswers[index]}"]`);
      if (selectedInput && selectedInput.closest('.option-label')) {
        selectedInput.closest('.option-label').classList.add('is-incorrect');
      }
    });

    const percentage = Math.round((correctCount / this.questions.length) * 100);
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const resultMessage = document.getElementById('result-message');

    if (resultContainer && resultText && resultMessage) {
      resultText.textContent = `${correctCount}/${this.questions.length} respuestas correctas (${percentage}%)`;
      resultMessage.textContent =
        percentage >= 70
          ? '¡Excelente! Has superado la autoevaluación.'
          : 'Te recomendamos revisar los contenidos de la lección.';

      resultContainer.style.display = 'block';
      window.scrollTo({ top: resultContainer.offsetTop, behavior: 'smooth' });
    }
  }

  resetQuiz() {
    this.userAnswers = {};
    document.querySelectorAll('input[type="radio"]').forEach((input) => {
      input.checked = false;
    });

    // Elimina resaltados de corrección
    document.querySelectorAll('.quiz-question').forEach((q) => q.classList.remove('question-wrong'));
    document.querySelectorAll('.option-label').forEach((l) => l.classList.remove('is-incorrect'));

    const resultContainer = document.getElementById('result-container');
    if (resultContainer) resultContainer.style.display = 'none';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const moduleId = document.body.getAttribute('data-module-id');
  if (moduleId) {
    new AutoevaluacionQuiz(moduleId);
  }
});
