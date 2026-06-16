# 🚀 Guía Rápida de Implementación - Autoevaluación

## Para Desarrolladores

### Opción 1: Añadir Autoevaluación a un Tema Existente

Si deseas añadir autoevaluación a un tema que aún no la tiene:

#### Paso 1: Actualizar el HTML del Tema

En el archivo `index.html` del tema:

```html
<!-- ANTES -->
<body>
  <div data-include="/partials/header.html"></div>
  ...
</body>

<!-- DESPUÉS -->
<body data-module-id="modulo2_tema1">
  <div data-include="/partials/header.html"></div>
  ...
  <div data-include="/partials/autoevaluacion.html"></div>
  ...
  <script src="/js/autoevaluacion.js"></script>
</body>
```

#### Paso 2: Asegúrate de que las Preguntas Existan

Verifica que `js/questions-data.json` tenga una entrada para ese tema:

```json
{
  "modulo2_tema1": {
    "titulo": "Autoevaluación - Módulo 2, Tema 1",
    "preguntas": [ ... ]
  }
}
```

### Opción 2: Crear Autoevaluación para una Lección Individual

Si deseas autoevaluación al final de una lección (no solo tema):

#### Paso 1: Añadir Preguntas al JSON

```json
{
  "modulo2_tema1_leccion1": {
    "titulo": "Autoevaluación - Lección 1",
    "preguntas": [
      {
        "pregunta": "Tu pregunta aquí",
        "opciones": {
          "A": "Opción A",
          "B": "Opción B",
          "C": "Opción C"
        },
        "respuestaCorrecta": "A"
      }
    ]
  }
}
```

#### Paso 2: Actualizar HTML de la Lección

```html
<body data-module-id="modulo2_tema1_leccion1">
  <div data-include="/partials/header.html"></div>
  <main>
    <!-- Contenido de la lección -->

    <!-- Autoevaluación al final -->
    <div data-include="/partials/autoevaluacion.html"></div>
  </main>

  <script src="/js/include.js"></script>
  <script src="/js/script.js"></script>
  <script src="/js/autoevaluacion.js"></script>
</body>
```

---

## Formato de Preguntas en JSON

### Estructura Básica

```json
{
  "pregunta": "¿Cuál es la respuesta correcta?",
  "opciones": {
    "A": "Esta es la opción A",
    "B": "Esta es la opción B",
    "C": "Esta es la opción C"
  },
  "respuestaCorrecta": "B"
}
```

### Ejemplo Completo

```json
{
  "pregunta": "¿Cuál es la principal diferencia entre MapReduce y Spark?",
  "opciones": {
    "A": "MapReduce usa memoria, Spark usa disco",
    "B": "Spark procesa en memoria, MapReduce usa disco",
    "C": "No hay diferencia, son lo mismo"
  },
  "respuestaCorrecta": "B"
}
```

### Reglas Importantes

1. **Pregunta**: Debe ser clara y específica
2. **Opciones**: Exactamente 3 opciones (A, B, C)
3. **Respuesta Correcta**: Debe ser A, B o C
4. **Caracteres Especiales**: Pueden incluir: ¿ ¡ € © ® ™ etc.

---

## Personalización de Estilos

### Cambiar Color del Botón Corregir

En `css/styles.css`:

```css
#submit-btn {
  background-color: #004eff;  /* Cambiar este color */
  color: white;
}

#submit-btn:hover {
  background-color: #0039cc;  /* Color al pasar el mouse */
}
```

### Cambiar Color de la Caja de Instrucciones

```css
.instructions-box {
  background-color: #f0f8ff;  /* Color de fondo */
  border-left: 4px solid #004eff;  /* Color del borde */
}
```

### Hacer Preguntas Más Grandes

```css
.question-text {
  font-size: 1.2em;  /* Aumentar tamaño */
  line-height: 1.8;  /* Aumentar espaciado entre líneas */
}
```

---

## Troubleshooting - Solución de Problemas

### La autoevaluación no aparece

**Causas posibles:**
- El `data-module-id` no está en la etiqueta `<body>`
- El include de `autoevaluacion.html` no está presente
- El script `autoevaluacion.js` no se cargó

**Solución:**
```html
<body data-module-id="modulo2_tema1">  <!-- ✅ Debe estar -->
  ...
  <div data-include="/partials/autoevaluacion.html"></div>  <!-- ✅ Debe estar -->
  ...
  <script src="/js/autoevaluacion.js"></script>  <!-- ✅ Debe estar -->
</body>
```

### Las preguntas no cargan

**Causa:** El `data-module-id` no coincide con la clave en `questions-data.json`

**Solución:**
- Verifica que `questions-data.json` tiene la entrada con ese ID
- El ID debe ser exacto: `modulo2_tema1` (con guiones bajos, sin espacios)

### El botón Corregir no funciona

**Causa:** No todas las preguntas están respondidas

**Solución:**
El sistema te mostrará un alert pidiéndote que respondas todas las preguntas.

### Los estilos no se aplican

**Causa:** El archivo CSS no se cargó o hay conflicto

**Solución:**
- Recarga la página (Ctrl+Shift+R para forzar recarga)
- Verifica en DevTools que `styles.css` se cargó sin errores

---

## JavaScript API - Para Desarrolladores Avanzados

### Crear instancia manual

```javascript
const quiz = new AutoevaluacionQuiz('modulo2_tema1');
```

### Con contenedor personalizado

```javascript
const quiz = new AutoevaluacionQuiz('modulo2_tema1', '#mi-contenedor');
```

### Acceder a propiedades

```javascript
quiz.questions       // Array de preguntas cargadas
quiz.userAnswers     // Object con respuestas del usuario
quiz.moduleId        // ID del módulo
```

### Llamar métodos

```javascript
quiz.renderQuiz()      // Dibujar preguntas
quiz.checkAnswers()    // Validar y mostrar resultados
quiz.resetQuiz()       // Limpiar respuestas
```

---

## Eventos Personalizados

### Escuchar cuando se cargan preguntas

```javascript
document.addEventListener('DOMContentLoaded', () => {
  console.log('Quiz cargado y listo');
});
```

### Escuchar cambios en respuestas

```javascript
document.addEventListener('change', (e) => {
  if (e.target.type === 'radio') {
    console.log('Respuesta cambiada');
  }
});
```

---

## Exportar Resultados (Extensión Futura)

Para guardar resultados en localStorage:

```javascript
// Guardar resultado
localStorage.setItem('quiz_resultado', JSON.stringify({
  modulo: 'modulo2_tema1',
  correctas: 4,
  total: 5,
  porcentaje: 80,
  fecha: new Date()
}));

// Recuperar resultado
const resultado = JSON.parse(localStorage.getItem('quiz_resultado'));
console.log(resultado);
```

---

## Estadísticas por Tema

| Tema | Preguntas | Estado |
|------|-----------|--------|
| Módulo 2, Tema 1 | 5 | ✅ Completo |
| Módulo 2, Tema 2 | 5 | ✅ Completo |
| Módulo 2, Tema 3 | 5 | ✅ Completo |
| Módulo 2, Tema 4 | 5 | ✅ Completo |
| Módulo 3, Tema 1 | 5 | ✅ Completo |
| Módulo 3, Tema 2 | 5 | ✅ Completo |
| Módulo 3, Tema 3 | 5 | ✅ Completo |
| **TOTAL** | **35** | **✅ COMPLETO** |

---

## Checklist Antes de Publicar

- [ ] `data-module-id` correctamente configurado
- [ ] Include de autoevaluacion.html presente
- [ ] Script autoevaluacion.js cargado
- [ ] Preguntas existen en questions-data.json
- [ ] Respuestas correctas están definidas
- [ ] Probado en navegadores principales
- [ ] Diseño responsivo verificado
- [ ] Mensajes de error probados

---

## Contacto y Soporte

Para problemas o dudas:

1. Consulta `ESPECIFICACION_TECNICA.md` para detalles técnicos
2. Consulta `GUIA_USUARIO_AUTOEVALUACION.md` para guía de usuario
3. Revisa `AUTOEVALUACION_README.md` para documentación general

---

**Última actualización:** 12 de Marzo de 2026
**Versión:** 1.0


