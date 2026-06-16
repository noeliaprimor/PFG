# Documentacion del Proyecto PFG

## 1. Vision general
Este proyecto es una plataforma web educativa para contenidos de Big Data y Apache Spark.
El sitio esta organizado por modulos, temas y lecciones, e incluye autoevaluaciones por tema.

## 2. Objetivos del proyecto
- Publicar contenido docente estructurado por modulos.
- Ofrecer navegacion clara entre lecciones y temas.
- Incluir autoevaluacion para refuerzo del aprendizaje.
- Mantener una base de codigo simple (HTML, CSS, JS) facil de ampliar.

## 3. Alcance funcional
- Modulo 1, Modulo 2 y Modulo 3 con lecciones HTML.
- Indices por tema con lista de lecciones.
- Paginas de autoevaluacion por tema (formato `M*T*auto.html`).
- Motor de preguntas dinamico desde JSON.
- Estilos y navegacion unificados.

## 4. Arquitectura tecnica (resumen)
- Frontend estatico con HTML + CSS + JavaScript.
- Carga de fragmentos reutilizables desde `partials/`.
- Preguntas de autoevaluacion en `js/questions-data.json`.
- Logica de correccion en `js/autoevaluacion.js`.

## 5. Estructura principal
- `modulo1/`, `modulo2/`, `modulo3/`: contenido docente.
- `css/`: hojas de estilo.
- `js/`: scripts de interaccion, includes y autoevaluacion.
- `partials/`: cabecera, pie y bloque de autoevaluacion.
- `img/`: recursos graficos.

## 6. Flujo de autoevaluacion
1. El usuario abre una pagina de autoevaluacion del tema.
2. La pagina define `data-module-id`.
3. Se carga `partials/autoevaluacion.html`.
4. `js/autoevaluacion.js` lee preguntas del JSON segun `data-module-id`.
5. Se corrigen respuestas y se muestra calificacion.

## 7. Documentos recomendados
- `ESTRUCTURA_PROYECTO.md`: detalle de carpetas y flujo de archivos.
- `GUIA_PUESTA_EN_MARCHA.md`: ejecucion local y mantenimiento.
- `USO_IA_EN_PROYECTO.md`: uso, limites y trazabilidad de IA.

## 8. Estado actual
Proyecto operativo para uso docente con evaluacion interactiva en modulos 2 y 3.


