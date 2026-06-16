# Uso de Inteligencia Artificial en el proyecto

## 1. Finalidad del uso de IA

Durante el desarrollo de este proyecto se ha utilizado Inteligencia Artificial como herramienta de apoyo para acelerar tareas de redaccion, revision, generacion de ejemplos, estructuracion de contenidos y mejora tecnica de la web docente.

La IA no se ha usado como sustituto de la autoria ni de la validacion final. Su papel ha sido el de asistente tecnico y editorial: proponer, ordenar, revisar y generar borradores que posteriormente han sido ajustados al contexto del proyecto.

## 2. Tipos de tareas asistidas por IA

### 2.1 Redaccion y mejora de contenidos docentes

La IA se ha utilizado para ampliar y homogeneizar lecciones del curso, especialmente en paginas de recursos, ejercicios propuestos y explicaciones tecnicas.

Ejemplos:

- Ampliacion de paginas de "Recursos y lecturas" en los temas de `modulo2` y `modulo3`.
- Reorganizacion de contenidos en secciones como descripcion, documentacion oficial, ruta de lectura y aplicacion al ejercicio.
- Mejora de explicaciones sobre Kafka, Spark Structured Streaming, MLlib, GraphX, monitorizacion y arquitecturas Lambda/Kappa.

Ejemplo concreto:

```text
Archivo: modulo3/Tema3/M3T3L4.html
Uso de IA: ampliacion de recursos sobre Kafka, contratos de datos, Schema Registry y relacion con el laboratorio avanzado.
Revision humana: comprobacion de coherencia con el tema "Procesamiento de streams con Spark".
```

### 2.2 Diseno de ejercicios practicos

La IA se ha utilizado para proponer ejercicios mas completos y realistas, manteniendo relacion directa con los contenidos del temario.

Ejemplo:

```text
Archivo: modulo3/Tema3/M3T3L5.html
Uso de IA: diseno de un ejercicio avanzado de integracion Kafka + Spark Structured Streaming.
Resultado: practica con productor Kafka, consumidor Spark, validacion, cuarentena, metricas, alertas, checkpoints y topic de eventos enriquecidos.
```

En este caso, la IA ayudo a estructurar:

- el enunciado del ejercicio;
- la arquitectura del pipeline;
- los pasos de ejecucion con Docker Compose;
- la separacion entre topic de entrada `orders` y topic de salida `orders_enriched`;
- las ampliaciones avanzadas propuestas para el alumnado.

### 2.3 Generacion de codigo de apoyo para laboratorios

La IA se ha utilizado para crear o revisar scripts y ficheros de laboratorio orientados a reproducibilidad.

Ejemplo:

```text
Carpeta: modulo3/Tema3/kafka_spark_advanced_lab/
Uso de IA: generacion del laboratorio avanzado de Kafka + Spark.
Ficheros creados:
- docker-compose.yml
- Dockerfile
- requirements.txt
- app/producer_orders.py
- app/streaming_pipeline.py
- app/validate_outputs.py
- README.md
```

El laboratorio permite ejecutar un flujo completo:

1. Un productor Python genera eventos JSON de pedidos.
2. Kafka recibe los eventos en el topic `orders`.
3. Spark Structured Streaming consume el topic.
4. Spark valida eventos, calcula metricas y genera alertas.
5. Los resultados se escriben en Parquet.
6. Los eventos enriquecidos se publican en `orders_enriched`.

La validacion tecnica incluyo revision de sintaxis Python mediante:

```bash
python3 -m py_compile producer_orders.py streaming_pipeline.py validate_outputs.py
```

### 2.4 Revision y mejora de HTML/CSS

La IA se ha utilizado para diagnosticar y corregir problemas de interfaz en la web.

Ejemplo:

```text
Archivo: css/styles.css
Problema: el menu desplegable de la cabecera se abria, pero el texto del submenu no era visible hasta pasar el raton por encima.
Uso de IA: analisis de reglas CSS y propuesta de correccion.
Resultado: ajuste de color, fondo, z-index, sombra y estado hover/focus del submenu.
```

El cambio permitio que los elementos del menu fueran visibles desde el primer despliegue, mejorando usabilidad y accesibilidad.

### 2.5 Adaptacion de documentacion tecnica

La IA se ha usado para transformar guias tecnicas en contenido didactico integrado en paginas HTML.

Ejemplo:

```text
Archivo fuente: modulo3/Tema2/KAFKA_SPARK_STREAMING_EXAMPLE_ACTUALIZADO.md
Archivo destino: modulo3/Tema2/M3T2L5.html
Uso de IA: conversion del contenido Markdown en una leccion HTML estructurada.
Resultado: pagina con enunciado, ficheros disponibles, ejecucion paso a paso, validacion, mejoras y entrega.
```

Durante esta adaptacion se tuvo en cuenta que los ficheros del laboratorio ya estaban incluidos en el proyecto, por lo que no era necesario indicar al alumnado que los generase desde cero.

### 2.6 Deteccion de ficheros candidatos a limpieza

La IA se ha utilizado para analizar el arbol del proyecto y enumerar posibles ficheros no usados.

Ejemplo:

```text
Tarea: identificar ficheros no referenciados o regenerables.
Resultado: clasificacion en candidatos de alta confianza, imagenes no referenciadas, notebooks no enlazados y documentacion auxiliar.
```

Esta tarea no implico borrado automatico. La IA solo propuso una lista de candidatos para revision humana.

## 3. Ejemplos de interaccion con IA

### Ejemplo 1: aclaracion de un bloque de comandos

Consulta:

```text
Porque esto se ejecuta dos veces:
docker compose exec kafka ... --topic orders
docker compose exec kafka ... --topic orders_enriched
```

Uso de IA:

La IA explico que no era una repeticion, sino la creacion de dos topics distintos:

- `orders`: topic de entrada para eventos del productor.
- `orders_enriched`: topic de salida para eventos procesados por Spark.

Resultado:

Se modifico `M3T3L5.html` para separar ambos bloques y anadir una explicacion antes de cada comando.

### Ejemplo 2: resolucion de error Docker

Problema:

```text
failed to solve: apt-get install openjdk-17-jre-headless ... exit code: 100
```

Uso de IA:

La IA identifico que la imagen base `python:3.11-slim` podia apuntar a una variante de Debian en la que el paquete no estuviera disponible.

Solucion aplicada:

```dockerfile
FROM python:3.11-slim-bookworm
```

Archivos actualizados:

- `modulo3/Tema2/Dockerfile`
- `modulo3/Tema2/crear_laboratorio.sh`
- `modulo3/Tema2/KAFKA_SPARK_STREAMING_EXAMPLE_ACTUALIZADO.md`
- `modulo3/Tema2/M3T2L5.html`

### Ejemplo 3: mejora de recursos y lecturas

Tarea:

```text
Cada carpeta de Tema* de modulo2 y modulo3 tiene una leccion "Recursos y lecturas".
Anadir contenido relativo al tema.
```

Uso de IA:

La IA reviso los indices de los temas, identifico las paginas de recursos y amplio su contenido con enlaces y explicaciones adaptadas a cada tema.

Archivos modificados:

- `modulo2/Tema1/M2T1L8.html`
- `modulo2/Tema2/M2T2L11.html`
- `modulo2/Tema3/M2T3L6.html`
- `modulo2/Tema4/M2T4L4.html`
- `modulo3/Tema1/M3T1L5.html`
- `modulo3/Tema3/M3T3L4.html`

## 4. Consultas realizadas en ChatGPT web

Ademas de las interacciones realizadas en este entorno de desarrollo, se realizaron consultas en ChatGPT web relacionadas con el proyecto. Estas consultas no han sido importadas de forma automatica desde una cuenta externa; han sido reconstruidas manualmente por la autora a partir de su historial personal.

Las consultas principales fueron:

### 4.1 Arquitectura y creacion de sesiones en Apache Spark

```text
Fecha aproximada: no disponible
Herramienta: ChatGPT web
Titulo o tema de la conversacion: Arquitectura y creacion de sesiones en Apache Spark
Consulta o necesidad planteada: explicacion tecnica detallada sobre SparkContext, SparkSession, ciclo de vida de aplicaciones Spark y configuracion avanzada en Docker.
Tipo de asistencia IA: explicacion tecnica, redaccion academica y generacion de contenido docente.
Revision humana realizada: adaptacion del contenido al enfoque docente y tecnico del proyecto.
Resultado incorporado al proyecto: documentacion teorica y tecnica sobre Apache Spark y arquitectura distribuida.
Nivel de confianza: alto
```

La asistencia incluyo explicaciones sobre:

- `SparkContext`;
- `SparkSession`;
- DAG Scheduler;
- Task Scheduler;
- gestion de memoria;
- ciclo de vida de aplicaciones Spark;
- integracion con Docker Standalone;
- comparativas entre `SparkContext` y `SparkSession`;
- ejemplos de configuracion avanzada en PySpark.

### 4.2 Modelo de micro-batches en Spark Streaming

```text
Fecha aproximada: no disponible
Herramienta: ChatGPT web
Titulo o tema de la conversacion: Modelo de micro-batches en Spark Streaming
Consulta o necesidad planteada: creacion de diagramas e infografias explicativas sobre el modelo de micro-batches.
Tipo de asistencia IA: generacion de imagenes tecnicas y apoyo visual docente.
Revision humana realizada: seleccion y validacion visual de los diagramas generados.
Resultado incorporado al proyecto: recursos graficos para documentacion y contenidos docentes del PFG.
Nivel de confianza: alto
```

La asistencia se centro en representar visualmente:

- procesamiento en micro-batches;
- arquitectura de Spark Streaming;
- flujo continuo de datos;
- batch interval;
- executors;
- DAG;
- procesamiento distribuido.

### 4.3 Integracion Spark Streaming + Kafka + YARN

```text
Fecha aproximada: no disponible
Herramienta: ChatGPT web
Titulo o tema de la conversacion: Integracion Spark Streaming + Kafka + YARN
Consulta o necesidad planteada: generacion de una imagen explicativa sobre la integracion entre Spark Streaming, Kafka y YARN.
Tipo de asistencia IA: generacion de contenido grafico tecnico.
Revision humana realizada: revision conceptual y adaptacion al diseno del proyecto.
Resultado incorporado al proyecto: material visual para explicar integracion Big Data distribuida.
Nivel de confianza: alto
```

La respuesta de IA aporto una infografia sobre:

- Kafka Cluster;
- Spark Streaming;
- YARN;
- flujo de procesamiento distribuido;
- micro-batches;
- executors;
- sinks;
- procesamiento paralelo.

### 4.4 Contenido HTML y modulos docentes del proyecto

```text
Fecha aproximada: no disponible
Herramienta: ChatGPT web
Titulo o tema de la conversacion: Contenido HTML y modulos docentes del proyecto
Consulta o necesidad planteada: generacion y mejora de contenidos docentes, temas, modulos y explicaciones tecnicas relacionadas con Big Data y Apache Spark.
Tipo de asistencia IA: generacion de contenido educativo y estructuracion academica.
Revision humana realizada: edicion, validacion tecnica y adaptacion pedagogica.
Resultado incorporado al proyecto: contenidos docentes del entorno web educativo.
Nivel de confianza: medio
```

La asistencia ayudo a estructurar contenidos relacionados con:

- Big Data;
- Spark;
- Streaming;
- arquitectura distribuida;
- organizacion conceptual de temas;
- adaptacion de explicaciones a formato web/HTML.

### 4.5 Docker y despliegue de servicios Big Data

```text
Fecha aproximada: no disponible
Herramienta: ChatGPT web
Titulo o tema de la conversacion: Docker y despliegue de servicios Big Data
Consulta o necesidad planteada: explicaciones y configuracion de entornos Spark en Docker y Docker Compose.
Tipo de asistencia IA: soporte tecnico y documentacion de infraestructura.
Revision humana realizada: ajuste y validacion de la configuracion usada en el proyecto.
Resultado incorporado al proyecto: documentacion tecnica e infraestructura Docker del entorno Big Data.
Nivel de confianza: alto
```

La asistencia incluyo explicaciones sobre:

- Spark Master;
- Spark Workers;
- uso de `spark://spark-master:7077`;
- ejecucion distribuida en contenedores;
- recomendaciones de configuracion;
- errores comunes en entornos Docker.

### 4.6 Interacciones con GitHub Copilot

Tambien se han registrado interacciones con GitHub Copilot relacionadas con el desarrollo y documentacion del proyecto. Estas interacciones han sido aportadas manualmente por la autora y se han incorporado con detalle en `REGISTRO_USO_IA.md`.

Los usos principales de GitHub Copilot fueron:

- propuesta de generacion del modulo 3 a partir de `structure.json` y del modulo 2 como plantilla;
- propuesta de correccion de `modulo3/modulo3.html`;
- mejora del comportamiento del menu desplegable en `partials/header.html`;
- diseno de estilos para tablas mediante `css/tables.css`;
- aplicacion de estilos de tablas en HTML bajo `modulo2` y `modulo3`;
- generacion de una seccion docente sobre proyectos Spark en PyCharm;
- revision conceptual de autoevaluaciones y cobertura de preguntas en `questions-data.json`;
- orientacion para reconstruir el uso de IA en conversaciones anteriores;
- orientacion para buscar evidencias de uso de Codex o Copilot en el repositorio;
- propuesta de comandos Git para reconstruir cambios historicos;
- exportacion de una ventana de chat en formato pregunta/respuesta.

Estas interacciones se consideran asistencia de apoyo. Algunas fueron propuestas o guias de actuacion y no necesariamente cambios aplicados directamente en el repositorio.

## 5. Control humano y validacion

Todas las propuestas generadas con IA han requerido revision humana antes de considerarse definitivas.

La validacion ha incluido:

- comprobar que los contenidos encajan con el tema correspondiente;
- revisar que los enlaces internos apuntan a rutas existentes;
- comprobar que los comandos son coherentes con los ficheros del laboratorio;
- verificar que no se eliminen cambios ajenos;
- validar sintaxis en scripts cuando era posible;
- mantener el estilo visual y editorial del proyecto.

## 6. Limites del uso de IA

La IA no ha sustituido:

- la decision final sobre que contenidos incluir;
- la responsabilidad academica del proyecto;
- la revision tecnica final;
- la validacion de resultados obtenidos al ejecutar laboratorios;
- la comprobacion manual de que la experiencia de usuario es adecuada.

Tambien se ha evitado borrar ficheros de forma automatica cuando la tarea era de limpieza. En esos casos, la IA ha enumerado candidatos y ha dejado la decision final a la persona responsable del proyecto.

## 7. Beneficios obtenidos

El uso de IA ha aportado valor principalmente en:

- acelerar la generacion de borradores tecnicos;
- homogeneizar la estructura de lecciones HTML;
- detectar inconsistencias de navegacion o explicacion;
- proponer ejercicios mas completos;
- transformar documentacion tecnica en material docente;
- ayudar a diagnosticar errores de configuracion;
- reducir trabajo repetitivo en cambios de formato.

## 8. Riesgos identificados y medidas de mitigacion

| Riesgo | Medida aplicada |
|---|---|
| Generacion de contenido tecnicamente plausible pero incorrecto | Revision humana y contraste con documentacion oficial |
| Instrucciones no adaptadas a los ficheros reales del proyecto | Lectura previa del arbol de archivos y de las paginas existentes |
| Cambios excesivos o no solicitados | Ediciones acotadas a los archivos relacionados con la tarea |
| Eliminacion accidental de ficheros utiles | No borrar sin confirmacion; solo listar candidatos |
| Inconsistencia visual entre paginas | Reutilizacion del patron HTML ya existente |

## 9. Trazabilidad recomendada

Para mantener transparencia, se recomienda registrar los cambios asistidos por IA con una plantilla como esta:

```text
Fecha:
Archivo o carpeta:
Objetivo del cambio:
Tipo de asistencia IA:
Revision realizada:
Resultado:
```

Ejemplo:

```text
Fecha: 2026-05-13
Archivo o carpeta: modulo3/Tema3/M3T3L5.html
Objetivo del cambio: aclarar la creacion de topics Kafka
Tipo de asistencia IA: explicacion tecnica y edicion HTML
Revision realizada: comprobacion del bloque modificado
Resultado: comandos separados para orders y orders_enriched
```

## 10. Conclusion

La IA se ha utilizado como apoyo tecnico y editorial a lo largo del proyecto, especialmente en tareas de estructuracion, documentacion, mejora de ejercicios y resolucion de incidencias.

El resultado final sigue dependiendo de la supervision humana: la IA propone y acelera, pero la seleccion, validacion y responsabilidad final corresponden a la persona autora del proyecto.
