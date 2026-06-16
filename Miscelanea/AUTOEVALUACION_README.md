# Sistema de Autoevaluación - Módulos 2 y 3

## Descripción General

Se ha implementado un sistema de autoevaluación completo y reutilizable para los módulos 2 y 3, con una página de autoevaluación después de cada tema.

## Archivos Creados

### 1. **js/questions-data.json**
   - Archivo JSON centralizado con todas las preguntas de autoevaluación
   - Organizado por identificadores de módulo y tema
   - Cada pregunta contiene:
     - `pregunta`: Enunciado de la pregunta
     - `opciones`: Opciones A, B, C
     - `respuestaCorrecta`: Letra de la respuesta correcta

### 2. **js/autoevaluacion.js**
   - Script JavaScript reutilizable que carga dinámicamente las preguntas
   - Funcionalidades principales:
     - Carga de preguntas desde JSON
     - Renderizado dinámico del formulario
     - Validación de respuestas
     - Cálculo de calificación
     - Reinicio del cuestionario

### 3. **partials/autoevaluacion.html**
   - Componente HTML parcial reutilizable
   - Incluye:
     - Instrucciones del cuestionario
     - Contenedor para preguntas
     - Botones de Corregir y Restablecer
     - Sección de resultados

### 4. **css/styles.css** (actualizado)
   - Nuevos estilos CSS para:
     - Caja de instrucciones
     - Preguntas y opciones
     - Botones interactivos
     - Resultados
     - Diseño responsivo para móviles

## Módulos Actualizados

### Módulo 2 - Procesamiento Paralelo en memoria: Apache Spark

#### Tema 1: Introducción e instalación de Apache Spark
- **Archivo**: `/modulo2/Tema1/index.html`
- **Data-module-id**: `modulo2_tema1`
- **5 preguntas sobre**: HDFS, NameNode, replicación

#### Tema 2: Procesamiento paralelo con Spark (APIs y técnicas)
- **Archivo**: `/modulo2/Tema2/index.html`
- **Data-module-id**: `modulo2_tema2`
- **5 preguntas sobre**: MapReduce, Combiner, Shuffle

#### Tema 3: Librerías y componentes de Spark
- **Archivo**: `/modulo2/Tema3/index.html`
- **Data-module-id**: `modulo2_tema3`
- **5 preguntas sobre**: Spark vs MapReduce, RDD, transformaciones

#### Tema 4: Monitorización, despliegue y operación
- **Archivo**: `/modulo2/Tema4/index.html`
- **Data-module-id**: `modulo2_tema4`
- **5 preguntas sobre**: Procesamiento distribuido, localidad de datos

### Módulo 3 - Gestión de datos en tiempo real

#### Tema 1: Arquitecturas Lambda y Kappa
- **Archivo**: `/modulo3/Tema1/index.html`
- **Data-module-id**: `modulo3_tema1`
- **5 preguntas sobre**: Kafka, Topics, Productores

#### Tema 2: Kafka y sistemas de mensajería
- **Archivo**: `/modulo3/Tema2/index.html`
- **Data-module-id**: `modulo3_tema2`
- **5 preguntas sobre**: Structured Streaming, Output Mode

#### Tema 3: Procesamiento de streams con Spark
- **Archivo**: `/modulo3/Tema3/index.html`
- **Data-module-id**: `modulo3_tema3`
- **5 preguntas sobre**: Medallion Architecture, Delta Lake, Checkpoint

## Cómo Funciona

### Para los Usuarios

1. Al final de cada tema (Módulo 2 y 3), aparece una sección de **AUTOEVALUACIÓN**
2. El usuario lee las instrucciones
3. Responde todas las preguntas seleccionando una opción (A, B o C)
4. Presiona el botón **Corregir**
5. Ve su calificación y un mensaje de retroalimentación
6. Puede presionar **Restablecer** para intentarlo de nuevo

### Para Desarrolladores

#### Para añadir una nueva pregunta:

1. Abrir `js/questions-data.json`
2. Buscar el identificador del tema (ej: `modulo2_tema1`)
3. Añadir un nuevo objeto en el array `preguntas`:

```json
{
  "pregunta": "¿Tu pregunta aquí?",
  "opciones": {
    "A": "Opción A",
    "B": "Opción B",
    "C": "Opción C"
  },
  "respuestaCorrecta": "A"
}
```

#### Para crear autoevaluación en una nueva lección:

Si en el futuro deseas agregar autoevaluación a una lección individual (no solo a temas):

1. Añadir preguntas en `questions-data.json` con ID `modulo2_tema1_leccion1`
2. En el HTML de la lección, añadir:
```html
<body data-module-id="modulo2_tema1_leccion1">
  <!-- contenido -->
  <div data-include="/partials/autoevaluacion.html"></div>
  <script src="/js/autoevaluacion.js"></script>
</body>
```

## Características

✅ **Reutilizable**: Mismo código funciona para todos los temas
✅ **Dinámico**: Las preguntas se cargan desde JSON
✅ **Responsivo**: Se adapta a móviles y tablets
✅ **Accesible**: Interfaz clara y fácil de usar
✅ **Extensible**: Fácil de añadir más preguntas
✅ **Sin dependencias externas**: Solo JavaScript vanilla

## Pasos de Instalación

No requiere instalación adicional. El sistema funciona con:
- Los archivos creados
- Los estilos CSS añadidos
- El script de include existente (`include.js`)

## Validación

Todos los archivos han sido validados:
- ✅ JSON válido
- ✅ JavaScript sin errores
- ✅ HTML bien formado
- ✅ CSS correctamente estructurado

## Soporte y Mantenimiento

Para actualizar el contenido de las preguntas, solo necesitas modificar `questions-data.json`. El resto del sistema se mantiene constante.

Para cambiar estilos, edita la sección `/* ========== ESTILOS PARA AUTOEVALUACIÓN ========== */` en `styles.css`.

