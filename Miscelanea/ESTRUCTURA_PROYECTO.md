# Estructura del Proyecto

## 1. Arbol simplificado
```text
PFG/
  index.html
  css/
  js/
  img/
  partials/
  modulo1/
  modulo2/
  modulo3/
  scripts/
```

## 2. Carpetas clave
### `css/`
- `styles.css`: estilos globales del sitio.
- Incluye estilos de navegacion, lecciones y autoevaluacion.

### `js/`
- `script.js`: logica comun de interfaz y carga de header/footer.
- `include.js`: carga de bloques `data-include`.
- `autoevaluacion.js`: render de preguntas y correccion.
- `questions-data.json`: banco de preguntas por tema.

### `partials/`
- `header.html`: cabecera reutilizable.
- `footer.html`: pie reutilizable.
- `autoevaluacion.html`: plantilla del cuestionario.

### `modulo2/` y `modulo3/`
- Cada tema tiene `index.html`.
- Cada tema contiene lecciones `M*T*L*.html`.
- Cada tema contiene autoevaluacion `M*T*auto.html`.

## 3. Convenciones de nombres
- Lecciones: `M2T2L1.html`.
- Autoevaluacion de tema: `M2T2auto.html`.
- Identificador de tema para preguntas: `modulo2_tema2`.

## 4. Relacion entre paginas y preguntas
- Cada pagina auto define `data-module-id` en `<body>`.
- Ese id se usa como clave en `js/questions-data.json`.
- Si la clave existe, se renderizan preguntas del tema.

## 5. Donde editar cada cosa
- Cambiar textos de contenido: lecciones HTML de cada tema.
- Cambiar estilo visual: `css/styles.css`.
- Cambiar preguntas: `js/questions-data.json`.
- Cambiar logica de correccion: `js/autoevaluacion.js`.

## 6. Buenas practicas de mantenimiento
- Mantener rutas absolutas consistentes (`/modulo2/...`).
- Probar navegacion entre `Leccion 1`, `Volver al modulo` y `Siguiente`.
- Verificar que cada `data-module-id` tenga preguntas en JSON.
- Evitar duplicar codigo de autoevaluacion en cada pagina.


