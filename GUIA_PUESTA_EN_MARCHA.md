# Guia de Puesta en Marcha

## 1. Requisitos
- Node.js instalado.
- Dependencias del proyecto instaladas (`node_modules`).

## 2. Instalacion
Si necesitas reinstalar dependencias:
```bash
npm install
```

## 3. Ejecucion en local
Opciones tipicas (segun configuracion webpack del proyecto):
```bash
npm run dev
```

o:
```bash
npm start
```

Si no existe ese script, revisa `package.json` en la seccion `scripts`.

## 4. Flujo de prueba rapido
1. Abrir un indice de tema, por ejemplo `modulo2/Tema1/index.html`.
2. Entrar a `Leccion 1`.
3. Abrir la pagina `M2T1auto.html`.
4. Responder preguntas y pulsar `Corregir`.

## 5. Verificaciones minimas
- El header y footer cargan correctamente.
- El bloque de autoevaluacion aparece en paginas `M*T*auto.html`.
- La calificacion se muestra y las respuestas fallidas se resaltan.

## 6. Incidencias comunes
- No aparecen preguntas:
  - Revisar `data-module-id` en la pagina auto.
  - Confirmar clave equivalente en `js/questions-data.json`.
  - Revisar consola por errores de carga de JSON.

- No se muestra el bloque de autoevaluacion:
  - Revisar `data-include="/partials/autoevaluacion.html"`.
  - Revisar carga de `js/include.js`.

- Estilos inconsistentes:
  - Forzar recarga del navegador (sin cache).
  - Confirmar cambios en `css/styles.css`.


