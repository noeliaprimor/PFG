# Registro de cambios asistidos por IA

Este documento recoge cambios relevantes del proyecto en los que se ha utilizado IA como apoyo tecnico, editorial o de revision.

La IA se ha usado como herramienta de asistencia. La seleccion final, revision y validacion de los cambios corresponde a la persona autora del proyecto.

## Plantilla utilizada

```text
Fecha:
Archivo o carpeta:
Objetivo del cambio:
Tipo de asistencia IA:
Revision realizada:
Resultado:
```

## Cambios registrados

### 1. Adaptacion del ejercicio Kafka + Spark Streaming actualizado

```text
Fecha: 2026-05-08
Archivo o carpeta: modulo3/Tema2/M3T2L5.html
Objetivo del cambio: incorporar en la pagina el contenido del ejercicio actualizado de Kafka + Spark Streaming.
Tipo de asistencia IA: transformacion de documentacion Markdown a HTML didactico y estructuracion del ejercicio.
Revision realizada: comprobacion de secciones, enlaces internos y coherencia con los ficheros ya incluidos en el proyecto.
Resultado: pagina con enunciado, ficheros disponibles, ejecucion paso a paso, validacion, ejercicios de mejora, problemas frecuentes y entrega.
```

### 2. Correccion del Dockerfile para evitar error con Java

```text
Fecha: 2026-05-11
Archivo o carpeta: modulo3/Tema2/Dockerfile, modulo3/Tema2/crear_laboratorio.sh, modulo3/Tema2/KAFKA_SPARK_STREAMING_EXAMPLE_ACTUALIZADO.md, modulo3/Tema2/M3T2L5.html
Objetivo del cambio: resolver el error de Docker durante la instalacion de openjdk-17-jre-headless.
Tipo de asistencia IA: diagnostico tecnico y propuesta de correccion en imagen base Docker.
Revision realizada: comprobacion de referencias a la imagen base y actualizacion de la guia de problemas frecuentes.
Resultado: uso de FROM python:3.11-slim-bookworm para fijar la variante de Debian y evitar fallos por paquetes no disponibles.
```

### 3. Creacion de ejercicio avanzado Kafka + Spark Structured Streaming

```text
Fecha: 2026-05-11
Archivo o carpeta: modulo3/Tema3/M3T3L5.html
Objetivo del cambio: convertir el ejercicio final del tema en una practica avanzada con Kafka real como fuente y Spark Structured Streaming como consumidor.
Tipo de asistencia IA: diseno pedagogico del ejercicio, redaccion HTML y estructuracion de comandos.
Revision realizada: comprobacion del flujo del ejercicio, navegacion de la pagina y coherencia con el tema "Procesamiento de streams con Spark".
Resultado: pagina con arquitectura, ficheros de laboratorio, ejecucion guiada, validacion, ampliaciones avanzadas y entrega.
```

### 4. Generacion del laboratorio avanzado Kafka + Spark

```text
Fecha: 2026-05-11
Archivo o carpeta: modulo3/Tema3/kafka_spark_advanced_lab/
Objetivo del cambio: crear un laboratorio autocontenido para ejecutar un pipeline completo Kafka + Spark.
Tipo de asistencia IA: generacion de ficheros Docker, scripts Python, README y comandos de ejecucion.
Revision realizada: validacion de sintaxis Python con py_compile y comprobacion de rutas enlazadas desde M3T3L5.html.
Resultado: laboratorio con productor de pedidos, consumidor Spark, validacion, cuarentena, metricas, alertas, salida Parquet y topic orders_enriched.
```

### 5. Aclaracion de la creacion de topics Kafka

```text
Fecha: 2026-05-13
Archivo o carpeta: modulo3/Tema3/M3T3L5.html
Objetivo del cambio: aclarar por que se ejecutaban dos comandos kafka-topics.sh.
Tipo de asistencia IA: explicacion tecnica y edicion HTML.
Revision realizada: comprobacion del bloque modificado.
Resultado: comandos separados para crear el topic de entrada orders y el topic de salida orders_enriched, con una explicacion previa para cada uno.
```

### 6. Ampliacion de paginas de Recursos y lecturas

```text
Fecha: 2026-05-13
Archivo o carpeta: modulo2/Tema1/M2T1L8.html, modulo2/Tema2/M2T2L11.html, modulo2/Tema3/M2T3L6.html, modulo2/Tema4/M2T4L4.html, modulo3/Tema1/M3T1L5.html, modulo3/Tema3/M3T3L4.html
Objetivo del cambio: completar las lecciones de recursos y lecturas con contenido especifico de cada tema.
Tipo de asistencia IA: redaccion tecnica, seleccion de categorias de recursos y homogeneizacion de estructura HTML.
Revision realizada: identificacion de la leccion correspondiente en cada tema, comprobacion de titulos, indices y secciones.
Resultado: paginas ampliadas con descripcion, contenido, rutas recomendadas y relacion con los ejercicios del tema.
```

### 7. Refuerzo de recursos para Spark Streaming y Kafka

```text
Fecha: 2026-05-13
Archivo o carpeta: modulo3/Tema3/M3T3L4.html
Objetivo del cambio: relacionar los recursos de lectura con el laboratorio avanzado de Kafka + Spark.
Tipo de asistencia IA: ampliacion editorial y conexion entre teoria y practica.
Revision realizada: comprobacion de enlaces a documentacion de Spark, Kafka, Schema Registry y JSON Schema.
Resultado: nueva seccion sobre Kafka, contratos de datos y operacion del pipeline, junto con una relacion explicita con kafka_spark_advanced_lab.
```

### 8. Mejora del menu desplegable de la cabecera

```text
Fecha: 2026-05-13
Archivo o carpeta: css/styles.css
Objetivo del cambio: corregir el problema por el que el submenu del menu superior se abria pero el texto no era visible hasta pasar el raton por encima.
Tipo de asistencia IA: diagnostico CSS y ajuste visual.
Revision realizada: lectura de partials/header.html y de las reglas CSS asociadas a .navbar, .submenu y .nav_menu.
Resultado: submenu con fondo, color de texto, z-index, borde, sombra y estados hover/focus definidos de forma explicita.
```

### 9. Analisis de ficheros candidatos a limpieza

```text
Fecha: 2026-05-13
Archivo o carpeta: raiz del proyecto
Objetivo del cambio: identificar ficheros y carpetas que podrian eliminarse al finalizar el proyecto.
Tipo de asistencia IA: analisis de referencias internas y clasificacion de candidatos.
Revision realizada: busqueda de referencias en HTML, CSS, JS, Markdown y estructura de carpetas.
Resultado: lista de candidatos agrupados por confianza: node_modules, .idea, imagenes no referenciadas, notebooks no enlazados y documentacion auxiliar.
```

### 10. Documentacion del uso de IA en el proyecto

```text
Fecha: 2026-05-13
Archivo o carpeta: USO_IA.md
Objetivo del cambio: documentar como se ha utilizado la IA a lo largo del proyecto con ejemplos concretos.
Tipo de asistencia IA: redaccion documental y organizacion de evidencias.
Revision realizada: comprobacion de que los ejemplos corresponden a cambios reales del proyecto.
Resultado: documento con finalidad, tareas asistidas, ejemplos, validacion humana, limites, beneficios, riesgos y trazabilidad recomendada.
```

### 11. Creacion del registro de cambios asistidos por IA

```text
Fecha: 2026-05-13
Archivo o carpeta: REGISTRO_USO_IA.md
Objetivo del cambio: crear un registro trazable de intervenciones asistidas por IA usando una plantilla uniforme.
Tipo de asistencia IA: redaccion estructurada y recopilacion de cambios relevantes.
Revision realizada: verificacion de formato, fechas, archivos y resultados descritos.
Resultado: documento de registro con entradas concretas sobre contenido, ejercicios, laboratorios, CSS, limpieza y documentacion.
```

### 12. Consulta en ChatGPT web sobre arquitectura y sesiones Spark

```text
Fecha: no disponible
Archivo o carpeta: contenidos teoricos del PFG relacionados con Apache Spark y documentacion tecnica
Objetivo del cambio: obtener una explicacion tecnica sobre SparkContext, SparkSession, ciclo de vida de aplicaciones Spark y configuracion avanzada en Docker.
Tipo de asistencia IA: explicacion tecnica, redaccion academica y generacion de contenido docente mediante ChatGPT web.
Revision realizada: adaptacion del contenido al enfoque docente y tecnico del proyecto.
Resultado: documentacion teorica y tecnica sobre Apache Spark y arquitectura distribuida.
```

### 13. Consulta en ChatGPT web sobre micro-batches en Spark Streaming

```text
Fecha: no disponible
Archivo o carpeta: material grafico y contenidos visuales del modulo de Spark Streaming
Objetivo del cambio: crear diagramas e infografias explicativas sobre el modelo de micro-batches de Spark Streaming.
Tipo de asistencia IA: generacion de imagenes tecnicas y apoyo visual docente mediante ChatGPT web.
Revision realizada: seleccion y validacion visual de los diagramas generados.
Resultado: recursos graficos para explicar procesamiento en micro-batches, arquitectura Spark Streaming, batch interval, executors y DAG.
```

### 14. Consulta en ChatGPT web sobre Spark Streaming, Kafka y YARN

```text
Fecha: no disponible
Archivo o carpeta: documentacion visual del ecosistema Big Data y arquitectura distribuida
Objetivo del cambio: generar una imagen explicativa sobre la integracion entre Spark Streaming, Kafka y YARN.
Tipo de asistencia IA: generacion de contenido grafico tecnico mediante ChatGPT web.
Revision realizada: revision conceptual y adaptacion al diseno del proyecto.
Resultado: material visual sobre Kafka Cluster, Spark Streaming, YARN, micro-batches, executors, sinks y procesamiento paralelo.
```

### 15. Consulta en ChatGPT web sobre contenido HTML y modulos docentes

```text
Fecha: no disponible
Archivo o carpeta: modulos HTML, temas docentes y lecciones del proyecto web
Objetivo del cambio: generar y mejorar contenidos docentes, temas, modulos y explicaciones tecnicas relacionadas con Big Data y Apache Spark.
Tipo de asistencia IA: generacion de contenido educativo y estructuracion academica mediante ChatGPT web.
Revision realizada: edicion, validacion tecnica y adaptacion pedagogica.
Resultado: contenidos docentes para el entorno web educativo sobre Big Data, Spark, Streaming y arquitectura distribuida.
```

### 16. Consulta en ChatGPT web sobre Docker y despliegue Big Data

```text
Fecha: no disponible
Archivo o carpeta: docker-compose.yml, configuracion de servicios Spark e infraestructura local de pruebas
Objetivo del cambio: obtener explicaciones y configuracion de entornos Spark en Docker y Docker Compose.
Tipo de asistencia IA: soporte tecnico y documentacion de infraestructura mediante ChatGPT web.
Revision realizada: ajuste y validacion de la configuracion usada en el proyecto.
Resultado: documentacion tecnica e infraestructura Docker del entorno Big Data, incluyendo Spark Master, Spark Workers y uso de spark://spark-master:7077.
```

## Observaciones finales

Este registro debe mantenerse actualizado si se realizan nuevos cambios con asistencia de IA.

Para cada nueva intervencion se recomienda:

- registrar la fecha;
- indicar archivos o carpetas afectados;
- explicar el objetivo del cambio;
- describir el tipo de ayuda proporcionada por IA;
- anotar que revision humana se realizo;
- resumir el resultado final.
