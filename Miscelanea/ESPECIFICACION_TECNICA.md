# Especificación Técnica - Sistema de Autoevaluación

## 1. Descripción General

Sistema de autoevaluación dinámico y reutilizable implementado para los Módulos 2 y 3 del proyecto PFG, con una página de autoevaluación al final de cada tema.

**Características principales:**
- Carga dinámica de preguntas desde JSON
- Reutilizable en múltiples temas sin código duplicado
- Diseño responsivo y accesible
- Validación en tiempo real
- Cálculo automático de calificación

---

## 2. Arquitectura del Sistema

### 2.1 Componentes

```
┌─────────────────────────────────────────────────┐
│         HTML del Tema (index.html)              │
│  - Contains: <body data-module-id="...">       │
│  - Includes: /partials/autoevaluacion.html    │
│  - Scripts: autoevaluacion.js                 │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│      include.js (Sistema de includes)          │
│  - Carga dinámicamente archivos HTML            │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│    autoevaluacion.html (Componente Parcial)    │
│  - Estructura HTML del cuestionario            │
│  - Divs específicos para contenido              │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│      autoevaluacion.js (Lógica Principal)      │
│  - Clase: AutoevaluacionQuiz                   │
│  - Carga preguntas desde JSON                  │
│  - Maneja interacciones usuario                │
│  - Calcula calificaciones                      │
└─────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│      questions-data.json (Base de Datos)       │
│  - Preguntas organizadas por módulo/tema       │
│  - Estructura: ID → Título + Array de preguntas│
└─────────────────────────────────────────────────┘
```

### 2.2 Flujo de Ejecución

1. **Carga de Página**
   - Navegador carga `index.html` del tema
   - Lee atributo `data-module-id` del `<body>`
   - Ejecuta `include.js` para cargar partials

2. **Carga de Componente**
   - `include.js` detecta `data-include="/partials/autoevaluacion.html"`
   - Realiza petición GET al servidor
   - Inserta HTML en el DOM

3. **Inicialización del Quiz**
   - `autoevaluacion.js` se ejecuta al cargar la página
   - Lee `data-module-id` del body
   - Crea instancia de `AutoevaluacionQuiz`

4. **Carga de Preguntas**
   - Petición AJAX a `questions-data.json`
   - Extrae preguntas usando el ID del módulo
   - Valida que existan preguntas

5. **Renderizado**
   - Itera sobre cada pregunta
   - Crea elementos DOM dinámicamente
   - Adjunta event listeners

6. **Interacción Usuario**
   - Usuario selecciona respuestas (radio buttons)
   - Sistema registra selecciones
   - Usuario presiona "Corregir"

7. **Validación y Cálculo**
   - Verifica todas las preguntas respondidas
   - Compara respuestas con valores correctos
   - Calcula porcentaje
   - Muestra resultado

---

## 3. Especificación de Archivos

### 3.1 `js/questions-data.json`

**Tipo:** JSON
**Tamaño:** ~11 KB
**Ubicación:** `/Users/noeliaprieto/PycharmProjects/PFG/js/questions-data.json`

**Estructura:**
```json
{
  "MODULO_TEMA_ID": {
    "titulo": "Título de la autoevaluación",
    "preguntas": [
      {
        "pregunta": "Enunciado de la pregunta",
        "opciones": {
          "A": "Texto de opción A",
          "B": "Texto de opción B",
          "C": "Texto de opción C"
        },
        "respuestaCorrecta": "A"
      }
    ]
  }
}
```

**IDs de Módulos Implementados:**
- `modulo2_tema1`
- `modulo2_tema2`
- `modulo2_tema3`
- `modulo2_tema4`
- `modulo3_tema1`
- `modulo3_tema2`
- `modulo3_tema3`

**Total:** 7 módulos × 5 preguntas = 35 preguntas

### 3.2 `js/autoevaluacion.js`

**Tipo:** JavaScript (ES6+)
**Tamaño:** ~4 KB
**Ubicación:** `/Users/noeliaprieto/PycharmProjects/PFG/js/autoevaluacion.js`

**Clase Principal: `AutoevaluacionQuiz`**

```javascript
class AutoevaluacionQuiz {
  constructor(moduleId, containerSelector = '#quiz-form')
  async init()
  renderQuiz()
  attachEventListeners()
  checkAnswers()
  resetQuiz()
}
```

**Métodos:**

| Método | Descripción | Parámetros | Retorna |
|--------|-------------|-----------|---------|
| `constructor()` | Inicializa la instancia | moduleId, containerSelector | - |
| `init()` | Carga preguntas desde JSON | - | Promise |
| `renderQuiz()` | Renderiza preguntas en DOM | - | void |
| `attachEventListeners()` | Adjunta listeners a elementos | - | void |
| `checkAnswers()` | Valida y calcula calificación | - | void |
| `resetQuiz()` | Reinicia el cuestionario | - | void |

**Eventos DOM Esperados:**
- `#submit-btn`: Click → `checkAnswers()`
- `#reset-btn`: Click → `resetQuiz()`
- `input[type="radio"]`: Change → Registra respuesta

### 3.3 `partials/autoevaluacion.html`

**Tipo:** HTML (fragmento/parcial)
**Tamaño:** ~1 KB
**Ubicación:** `/Users/noeliaprieto/PycharmProjects/PFG/partials/autoevaluacion.html`

**Estructura:**
```html
<section id="autoevaluacion">
  <div class="lesson-container">
    <h3>AUTOEVALUACIÓN</h3>
    <hr>

    <div class="instructions-box">
      <!-- Instrucciones -->
    </div>

    <div id="quiz-form">
      <!-- Se rellena dinámicamente por JS -->
    </div>

    <div class="button-container">
      <button id="submit-btn">Corregir</button>
      <button id="reset-btn">Restablecer</button>
    </div>

    <div id="result-container">
      <h2>CALIFICACIÓN</h2>
      <p id="result-text"></p>
      <p id="result-message"></p>
    </div>
  </div>
</section>
```

**IDs Críticos (Utilizados por JS):**
- `#quiz-form` - Contenedor para preguntas
- `#submit-btn` - Botón Corregir
- `#reset-btn` - Botón Restablecer
- `#result-container` - Sección de resultados
- `#result-text` - Texto de calificación
- `#result-message` - Mensaje de retroalimentación

### 3.4 `css/styles.css` (Sección de Autoevaluación)

**Tipo:** CSS3
**Tamaño:** ~2 KB (sección de autoevaluación)
**Ubicación:** Líneas 1524-1638 de `/css/styles.css`

**Clases CSS Principales:**

| Clase | Propósito |
|-------|-----------|
| `.instructions-box` | Caja de instrucciones con fondo azul |
| `.quiz-question` | Contenedor de cada pregunta |
| `.question-text` | Texto de la pregunta |
| `.options-group` | Grupo de opciones de respuesta |
| `.option-label` | Etiqueta de opción individual |
| `.option-input` | Input radio (respuesta) |
| `.button-container` | Contenedor de botones |
| `#submit-btn` | Botón Corregir |
| `#reset-btn` | Botón Restablecer |
| `.result-box` | Caja de resultados |

**Breakpoints Responsivos:**
- Desktop: 100% width
- Tablet (≤768px): Botones 100% width, flex-direction: column

---

## 4. Integración en Módulos

### 4.1 Cambios en Archivos index.html

**Patrón:**

```html
<!-- Antes: -->
<body>
  <div data-include="/partials/header.html"></div>
  ...
  </main>
  <script src="/js/include.js"></script>
  <script src="/js/script.js"></script>
</body>

<!-- Después: -->
<body data-module-id="modulo2_tema1">
  <div data-include="/partials/header.html"></div>
  ...
  <div data-include="/partials/autoevaluacion.html"></div>
  ...
  </main>
  <script src="/js/include.js"></script>
  <script src="/js/script.js"></script>
  <script src="/js/autoevaluacion.js"></script>
</body>
```

**Archivos Modificados:**
1. `/modulo2/Tema1/index.html`
2. `/modulo2/Tema2/index.html`
3. `/modulo2/Tema3/index.html`
4. `/modulo2/Tema4/index.html`
5. `/modulo3/Tema1/index.html`
6. `/modulo3/Tema2/index.html`
7. `/modulo3/Tema3/index.html`

---

## 5. Comportamiento del Sistema

### 5.1 Carga de Preguntas

**Proceso:**
1. Petición AJAX con `fetch('/js/questions-data.json')`
2. Parse JSON
3. Búsqueda de clave `data-module-id`
4. Extracción de array `preguntas`
5. Validación: Al menos 1 pregunta

**Manejo de Errores:**
```javascript
if (this.questions.length === 0) {
  console.warn(`No preguntas encontradas para ${this.moduleId}`);
  return; // Salir silenciosamente
}
```

### 5.2 Renderizado Dinámico

**Algoritmo:**
```
Para cada pregunta en la lista:
  1. Crear div.quiz-question
  2. Crear p.question-text con número y enunciado
  3. Crear div.options-group
  4. Para cada opción (A, B, C):
    - Crear label.option-label
    - Crear input[type="radio"]
    - Crear span con texto de opción
  5. Añadir al contenedor #quiz-form
```

### 5.3 Validación de Respuestas

**Lógica:**
1. Verifica que todas las preguntas estén respondidas
2. Si alguna está vacía: `alert('Por favor, contesta todas las preguntas.')`
3. Itera sobre respuestas del usuario
4. Compara con `respuestaCorrecta` de cada pregunta
5. Cuenta aciertos
6. Calcula porcentaje: `(aciertos / total) * 100`

### 5.4 Mostrar Resultados

**Formato:**
```
Respuestas correctas: 4/5 (80%)
Mensaje:
  - Si >= 70%: "¡Excelente! Has superado la autoevaluación."
  - Si < 70%: "Te recomendamos revisar los contenidos de la lección."
```

**Presentación:**
- Se muestra `#result-container` con `display: block`
- Scroll suave al resultado
- Resultado permanece visible hasta presionar "Restablecer"

### 5.5 Reinicio del Cuestionario

**Acciones:**
1. Limpia objeto `userAnswers`
2. Destilda todos los radio buttons
3. Oculta `#result-container`
4. Usuario puede responder nuevamente

---

## 6. Requisistos Técnicos

### 6.1 Navegador

**Mínimo requerido:**
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

**Tecnologías usadas:**
- ES6+ (const, let, arrow functions, async/await)
- Fetch API
- DOM Level 3
- CSS3 (Flexbox, Gradients, Transitions)

### 6.2 Servidor

**Requisitos:**
- Soporte de peticiones HTTP GET
- MIME types correctos: `application/json`, `text/html`
- CORS (si es necesario en desarrollo)

**Rutas esperadas:**
- `/js/questions-data.json`
- `/partials/autoevaluacion.html`
- `/js/autoevaluacion.js`
- `/css/styles.css`

### 6.3 Dependencias

**Externas (existentes):**
- `/js/include.js` - Sistema de includes
- `/css/styles.css` - Estilos generales

**Internas (nuevas):**
- `/js/autoevaluacion.js`
- `/js/questions-data.json`
- `/partials/autoevaluacion.html`

---

## 7. API Pública

### 7.1 Inicialización Manual

```javascript
// Crear instancia manual (sin depender de data-module-id)
const quiz = new AutoevaluacionQuiz('modulo2_tema1', '#mi-contenedor');
```

### 7.2 Propiedades de Instancia

| Propiedad | Tipo | Descripción |
|-----------|------|-------------|
| `moduleId` | String | ID del módulo (ej: modulo2_tema1) |
| `questions` | Array | Array de preguntas cargadas |
| `userAnswers` | Object | Respuestas del usuario {pregunta#: respuesta} |

---

## 8. Mantenimiento y Extensión

### 8.1 Añadir Nueva Pregunta

1. Abrir `js/questions-data.json`
2. Ir a la sección del tema
3. Añadir objeto a array `preguntas`:
```json
{
  "pregunta": "Tu pregunta",
  "opciones": {"A": "...", "B": "...", "C": "..."},
  "respuestaCorrecta": "A"
}
```
4. Guardar (JSON se valida automáticamente)

### 8.2 Crear Autoevaluación para Nueva Lección

1. En `questions-data.json`, crear nueva entrada:
```json
"modulo2_tema1_leccion1": {
  "titulo": "...",
  "preguntas": [...]
}
```

2. En HTML de lección:
```html
<body data-module-id="modulo2_tema1_leccion1">
  ...
  <div data-include="/partials/autoevaluacion.html"></div>
  ...
  <script src="/js/autoevaluacion.js"></script>
</body>
```

### 8.3 Cambiar Estilos

Editar sección `/* ========== ESTILOS PARA AUTOEVALUACIÓN ========== */` en `css/styles.css`

---

## 9. Pruebas

### 9.1 Página de Prueba

Ubicación: `/test-autoevaluacion.html`

Uso: Acceder a `http://localhost:port/test-autoevaluacion.html` para probar la funcionalidad en aislamiento.

### 9.2 Checklist de Validación

- [ ] JSON válido (sin errores de sintaxis)
- [ ] JavaScript carga sin errores
- [ ] Preguntas aparecen en la página
- [ ] Seleccionar respuesta funciona
- [ ] Botón Corregir funciona
- [ ] Calificación se calcula correctamente
- [ ] Botón Restablecer limpia respuestas
- [ ] Diseño es responsivo
- [ ] Mensajes son claros

---

## 10. Notas de Implementación

- Sistema usa **vanilla JavaScript** (sin dependencias como jQuery)
- Arquitectura **evento-basada** para máxima flexibilidad
- Preguntas en **JSON** para facilitar mantenimiento
- CSS **modular** y fácil de personalizar
- Código **comentado** para facilitar comprensión
- Manejo de errores **graceful** (no rompe la página)

---

## 11. Historial de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 12/03/2026 | Release inicial con 7 temas y 35 preguntas |


