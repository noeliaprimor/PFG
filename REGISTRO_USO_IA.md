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
Fecha: 2026-05-13 (estimada)
Archivo o carpeta: contenidos teoricos del PFG relacionados con Apache Spark y documentacion tecnica
Objetivo del cambio: obtener una explicacion tecnica sobre SparkContext, SparkSession, ciclo de vida de aplicaciones Spark y configuracion avanzada en Docker.
Tipo de asistencia IA: explicacion tecnica, redaccion academica y generacion de contenido docente mediante ChatGPT web.
Revision realizada: adaptacion del contenido al enfoque docente y tecnico del proyecto.
Resultado: documentacion teorica y tecnica sobre Apache Spark y arquitectura distribuida.
```

### 13. Consulta en ChatGPT web sobre micro-batches en Spark Streaming

```text
Fecha: 2026-05-13 (estimada)
Archivo o carpeta: material grafico y contenidos visuales del modulo de Spark Streaming
Objetivo del cambio: crear diagramas e infografias explicativas sobre el modelo de micro-batches de Spark Streaming.
Tipo de asistencia IA: generacion de imagenes tecnicas y apoyo visual docente mediante ChatGPT web.
Revision realizada: seleccion y validacion visual de los diagramas generados.
Resultado: recursos graficos para explicar procesamiento en micro-batches, arquitectura Spark Streaming, batch interval, executors y DAG.
```

### 14. Consulta en ChatGPT web sobre Spark Streaming, Kafka y YARN

```text
Fecha: 2026-05-13 (estimada)
Archivo o carpeta: documentacion visual del ecosistema Big Data y arquitectura distribuida
Objetivo del cambio: generar una imagen explicativa sobre la integracion entre Spark Streaming, Kafka y YARN.
Tipo de asistencia IA: generacion de contenido grafico tecnico mediante ChatGPT web.
Revision realizada: revision conceptual y adaptacion al diseno del proyecto.
Resultado: material visual sobre Kafka Cluster, Spark Streaming, YARN, micro-batches, executors, sinks y procesamiento paralelo.
```

### 15. Consulta en ChatGPT web sobre contenido HTML y modulos docentes

```text
Fecha: 2026-05-13 (estimada)
Archivo o carpeta: modulos HTML, temas docentes y lecciones del proyecto web
Objetivo del cambio: generar y mejorar contenidos docentes, temas, modulos y explicaciones tecnicas relacionadas con Big Data y Apache Spark.
Tipo de asistencia IA: generacion de contenido educativo y estructuracion academica mediante ChatGPT web.
Revision realizada: edicion, validacion tecnica y adaptacion pedagogica.
Resultado: contenidos docentes para el entorno web educativo sobre Big Data, Spark, Streaming y arquitectura distribuida.
```

### 16. Consulta en ChatGPT web sobre Docker y despliegue Big Data

```text
Fecha: 2026-05-13 (estimada)
Archivo o carpeta: docker-compose.yml, configuracion de servicios Spark e infraestructura local de pruebas
Objetivo del cambio: obtener explicaciones y configuracion de entornos Spark en Docker y Docker Compose.
Tipo de asistencia IA: soporte tecnico y documentacion de infraestructura mediante ChatGPT web.
Revision realizada: ajuste y validacion de la configuracion usada en el proyecto.
Resultado: documentacion tecnica e infraestructura Docker del entorno Big Data, incluyendo Spark Master, Spark Workers y uso de spark://spark-master:7077.
```

## Interacciones adicionales con GitHub Copilot

Las siguientes entradas proceden de un resumen aportado manualmente por la autora del proyecto sobre interacciones mantenidas con GitHub Copilot o con una ventana de chat identificada como Copilot. No han sido importadas automaticamente desde la herramienta.

### 17. Generacion del modulo 3 a partir de structure.json

```text
Fecha: no disponible
Archivo o carpeta: data/structure.json, modulo2/, modulo3/
Objetivo del cambio: generar contenido del modulo 3 usando la estructura definida en structure.json y tomando el modulo 2 como plantilla.
Tipo de asistencia IA: solicitud de generacion de contenido docente y estructuracion de modulos mediante GitHub Copilot.
Revision realizada: la herramienta solicito anadir los ficheros al working set antes de modificar.
Resultado: no se incorporaron cambios directos en esa primera interaccion; quedo pendiente proporcionar los archivos necesarios.
```

### 18. Propuesta de correccion de la pagina raiz del modulo 3

```text
Fecha: no disponible
Archivo o carpeta: modulo3/modulo3.html
Objetivo del cambio: corregir la pagina raiz del modulo 3 y estructurar enlaces hacia los temas.
Tipo de asistencia IA: propuesta de pasos de refactorizacion HTML mediante GitHub Copilot.
Revision realizada: revision de la propuesta antes de aplicar cambios.
Resultado: se propuso unificar etiqueta html, titulo, rutas, main, enlaces a Tema1 y Tema2, placeholder para Tema3 y limpieza de duplicados de footer/scripts.
```

### 19. Menu desplegable por hover en header

```text
Fecha: no disponible
Archivo o carpeta: partials/header.html
Objetivo del cambio: hacer que el submenu de Modulo 2 apareciera al posar el raton sin necesidad de hacer click.
Tipo de asistencia IA: propuesta de mejora HTML/CSS/JS mediante GitHub Copilot.
Revision realizada: revision de accesibilidad y comportamiento esperado del menu.
Resultado: se propuso soporte CSS con hover, mantenimiento de aria-expanded y navegacion por teclado.
```

### 20. Diseno de estilos de tablas para modulos 2 y 3

```text
Fecha: no disponible
Archivo o carpeta: css/tables.css, modulo2/, modulo3/
Objetivo del cambio: mejorar el estilo visual de las tablas del proyecto.
Tipo de asistencia IA: propuesta de diseno CSS y normalizacion visual mediante GitHub Copilot.
Revision realizada: revision del alcance y de las paginas con tablas.
Resultado: se propuso crear tables.css con bordes suaves, sombreado, filas alternas, cabecera sticky, diseno responsive y clases reutilizables.
```

### 21. Aplicacion de estilos de tablas a HTML existentes

```text
Fecha: no disponible
Archivo o carpeta: css/tables.css, multiples HTML en modulo2/ y modulo3/
Objetivo del cambio: aplicar los estilos de tablas a todos los ficheros HTML bajo modulo2 y modulo3.
Tipo de asistencia IA: propuesta de cambios masivos en HTML/CSS mediante GitHub Copilot.
Revision realizada: revision de la propuesta de incluir tables.css y ajustar clases de tablas.
Resultado: se propuso enlazar tables.css en los HTML y aplicar clases table/table-bordered donde procediera.
```

### 22. Contenido sobre creacion de proyecto Spark en PyCharm

```text
Fecha: no disponible
Archivo o carpeta: modulo3/Tema1/M3T1L5.html
Objetivo del cambio: generar una seccion didactica sobre creacion de un proyecto Spark en PyCharm.
Tipo de asistencia IA: generacion de contenido docente mediante GitHub Copilot.
Revision realizada: revision de adecuacion al tema y al formato HTML.
Resultado: se propuso insertar explicacion, prerequisitos, pasos de creacion, estructura de proyecto y ejemplo main.py.
```

### 23. Personalizacion de contenido segun Ejercicio1.ipynb

```text
Fecha: no disponible
Archivo o carpeta: Ejercicio1.ipynb, modulo3/Tema1/M3T1L5.html
Objetivo del cambio: adaptar el contenido generado a lo que realmente hacia el notebook Ejercicio1.ipynb.
Tipo de asistencia IA: solicitud de revision contextual mediante GitHub Copilot.
Revision realizada: la herramienta indico que necesitaba el notebook o un resumen para personalizar con exactitud.
Resultado: se ofrecio una version provisional con marcadores pendientes de ajustar tras revisar el notebook.
```

### 24. Revision de autoevaluacion del Tema 2 del Modulo 2

```text
Fecha: no disponible
Archivo o carpeta: modulo2/Tema2/M2T2auto.html, js/questions-data.json
Objetivo del cambio: verificar que las preguntas de autoevaluacion cubrian todas las lecciones de modulo2/Tema2.
Tipo de asistencia IA: revision pedagogica y propuesta de reorganizacion mediante GitHub Copilot.
Revision realizada: se indico que sin acceso a questions-data.json no era posible verificar automaticamente el banco de preguntas.
Resultado: se propuso una autoevaluacion organizada por subtema y un checklist de correspondencia por leccion.
```

### 25. Revision de questions-data.json para modulo2_tema2

```text
Fecha: no disponible
Archivo o carpeta: js/questions-data.json, modulo2/Tema2/
Objetivo del cambio: comprobar si la seccion modulo2_tema2 incluia preguntas de todo el contenido del tema y no solo MapReduce.
Tipo de asistencia IA: solicitud de analisis de banco de preguntas mediante GitHub Copilot.
Revision realizada: la herramienta solicito anadir los ficheros al working set.
Resultado: no se incorporaron cambios directos en esa interaccion; quedo pendiente proporcionar el fichero.
```

### 26. Propuesta de actualizacion de autoevaluacion modulo2_tema2

```text
Fecha: no disponible
Archivo o carpeta: modulo2/Tema2/M2T2auto.html, js/questions-data.json
Objetivo del cambio: revisar y ampliar preguntas representativas para todo el Tema 2 del Modulo 2.
Tipo de asistencia IA: propuesta de cobertura tematica mediante GitHub Copilot.
Revision realizada: se indico que era necesario disponer de questions-data.json o de la seccion modulo2_tema2 para verificar con exactitud.
Resultado: se propuso actualizar la autoevaluacion con preguntas por subtema mientras se aportaba el fichero requerido.
```

### 27. Reconstruccion del uso de IA en conversaciones previas

```text
Fecha: no disponible
Archivo o carpeta: documentacion final del proyecto
Objetivo del cambio: reconstruir el uso de IA realizado en conversaciones anteriores y obtener un formato Markdown reutilizable.
Tipo de asistencia IA: resumen documental y estructuracion de evidencias mediante GitHub Copilot.
Revision realizada: revision manual del resumen generado y seleccion de consultas relevantes.
Resultado: se genero un resumen con bloques "Consulta IA N" sobre modulo3, header, tablas, PyCharm, autoevaluaciones y question-data.json.
```

### 28. Busqueda de evidencias de uso de Codex o Copilot

```text
Fecha: no disponible
Archivo o carpeta: repositorio del proyecto
Objetivo del cambio: identificar que uso de IA se habia dado al proyecto con Codex o Copilot.
Tipo de asistencia IA: orientacion de auditoria y trazabilidad mediante GitHub Copilot.
Revision realizada: se revisaron las limitaciones indicadas por la herramienta.
Resultado: se propusieron comandos y vias de busqueda en el repositorio, git log, metadatos de notebooks y configuracion de extensiones.
```

### 29. Consulta especifica sobre uso de GitHub Copilot

```text
Fecha: no disponible
Archivo o carpeta: repositorio del proyecto
Objetivo del cambio: determinar si existian evidencias explicitas de uso de GitHub Copilot.
Tipo de asistencia IA: orientacion de trazabilidad mediante GitHub Copilot.
Revision realizada: revision de la respuesta y de la necesidad de buscar evidencias locales.
Resultado: se indico que no habia menciones explicitas en el historial aportado y se sugirieron busquedas similares a las de Codex.
```

### 30. Enumeracion de cambios historicos del proyecto

```text
Fecha: no disponible
Archivo o carpeta: historial git del proyecto
Objetivo del cambio: enumerar cambios realizados desde la creacion del proyecto.
Tipo de asistencia IA: orientacion sobre uso de git y generacion de changelog mediante GitHub Copilot.
Revision realizada: se tuvo en cuenta que la herramienta no podia acceder directamente al repositorio ni al historial de commits.
Resultado: se propusieron comandos git para extraer logs y pasos para convertir la salida en un changelog Markdown.
```

### 31. Exportacion de contenido de chat en formato pregunta/respuesta

```text
Fecha: no disponible
Archivo o carpeta: documentacion final del uso de IA
Objetivo del cambio: exportar el contenido de una ventana de chat en formato "pregunta realizada por mi" y "respuesta de Copilot".
Tipo de asistencia IA: estructuracion y resumen de interacciones mediante GitHub Copilot.
Revision realizada: revision manual del documento generado por la autora.
Resultado: se genero el resumen de interacciones utilizado como base para estas entradas del registro.
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
