# Resumen de ejercicios del proyecto

## 1. Alcance

Este documento resume el sistema de ejercicios localizado en el proyecto PFG, incluyendo:

- Autoevaluaciones por tema.
- Ejercicios practicos propuestos en las lecciones finales de cada tema.
- Notebooks, datasets, laboratorios y documentos relacionados.
- Objetivos formativos y tecnologias necesarias.

La revision se basa en el estado actual del repositorio, especialmente en `js/questions-data.json`, `data/structure.json`, las lecciones de ejercicio de `modulo2` y `modulo3`, y el marco de uso de IA descrito en `USO_IA_EN_PROYECTO.md`.

## 2. Sistema de autoevaluacion

El proyecto incorpora un sistema de autoevaluacion reutilizable para los modulos 2 y 3. Cada tema usa un identificador `data-module-id` en el HTML, que se cruza con las preguntas definidas en `js/questions-data.json`.

### Componentes principales

| Archivo | Funcion |
| --- | --- |
| `js/questions-data.json` | Banco centralizado de preguntas por modulo y tema. |
| `js/autoevaluacion.js` | Logica de carga, renderizado, correccion, calculo de nota y reinicio. |
| `partials/autoevaluacion.html` | Fragmento HTML reutilizable del cuestionario. |
| `css/styles.css` | Estilos del bloque de autoevaluacion, preguntas, botones y resultados. |
| `test-autoevaluacion.html` | Pagina de prueba del sistema. |

### Cobertura actual

| ID | Tema | Preguntas |
| --- | --- | ---: |
| `modulo2_tema1` | Introduccion e instalacion de Apache Spark | 10 |
| `modulo2_tema2` | Procesamiento paralelo con Spark | 20 |
| `modulo2_tema3` | Librerias y componentes avanzados de Spark | 20 |
| `modulo2_tema4` | Configuracion, monitorizacion y optimizacion de Spark | 20 |
| `modulo3_tema1` | Procesamiento de streaming y arquitecturas Lambda/Kappa | 20 |
| `modulo3_tema2` | Adquisicion, Kafka, sinks y conectores | 24 |
| `modulo3_tema3` | Procesamiento de streams con Spark | 22 |

Total actual en `js/questions-data.json`: 136 preguntas.

Nota: algunos documentos historicos del proyecto indican 35 preguntas, pero esa cifra corresponde a una version anterior. La fuente vigente es `js/questions-data.json`.

### Objetivos de las autoevaluaciones

- Verificar la comprension conceptual al final de cada tema.
- Comprobar la capacidad de identificar componentes, APIs, configuraciones y patrones de Spark/Kafka.
- Reforzar vocabulario tecnico: RDD, DataFrame, SparkSession, Structured Streaming, checkpoint, watermark, Kafka topic, offset, sink, Parquet y Delta Lake.
- Dar retroalimentacion inmediata mediante puntuacion y mensaje de resultado.
- Facilitar mantenimiento docente mediante un banco de preguntas JSON.

## 3. Ejercicios practicos por tema

### Modulo 2. Procesamiento paralelo basado en Spark

| Tema | Archivo principal | Recursos asociados | Resumen del ejercicio | Objetivos | Tecnologias |
| --- | --- | --- | --- | --- | --- |
| Tema 1: Introduccion e instalacion de Apache Spark | `modulo2/Tema1/M2T1L9.html` | `modulo2/Tema1/docker-compose.yml`, `modulo2/Tema1/Ejercicio2-1.ipynb`, `modulo2/Tema1/heart.csv` | Practicas de escalado de workers, modificacion de recursos, analisis de logs y procesamiento de datos con PySpark. | Comprender ejecucion distribuida, impacto de recursos, uso de logs y comportamiento del cluster. | Apache Spark, PySpark, Docker Compose, CSV, terminal. |
| Tema 2: Procesamiento paralelo con Spark | `modulo2/Tema2/M2T2L12.html` | `modulo2/Tema2/Ejercicio1.ipynb`, `modulo2/Tema2/DatasetTema2.zip` | Caso practico sobre dataset retail: carga, limpieza, KPIs, joins, pivot, ventanas, promociones e interpretacion. | Aplicar transformaciones de DataFrames, funciones de ventana, joins especializados y analisis de negocio. | PySpark, Spark SQL/DataFrames, Jupyter Notebook, CSV, Parquet opcional, PyCharm. |
| Tema 3: Librerias y componentes avanzados de Spark | `modulo2/Tema3/M2T3L7.html` | `modulo2/Tema3/M2T3_productor.ipynb`, `modulo2/Tema3/M2T3_consumidor.ipynb` | Pipeline productor-consumidor con API CoinGecko para simular eventos de criptomonedas y procesarlos con Spark Structured Streaming. | Introducir streaming, ventanas temporales, alertas, agregaciones y persistencia de metricas. | CoinGecko API, Python, PySpark, Structured Streaming, Jupyter Notebook, Parquet. |
| Tema 4: Monitorizacion, despliegue y operacion | `modulo2/Tema4/M2T4L5.html` | Lecciones de configuracion y recursos del tema | Ejecucion de una aplicacion Spark en local/cluster, captura de metricas y propuesta de mejoras de configuracion. | Comparar tiempos, ajustar `spark.executor.memory` y `spark.executor.cores`, observar impacto y documentar mejoras. | Apache Spark, Spark UI, Prometheus, Grafana, Docker/cluster, configuracion Spark. |

### Modulo 3. Gestion de datos en tiempo real

| Tema | Archivo principal | Recursos asociados | Resumen del ejercicio | Objetivos | Tecnologias |
| --- | --- | --- | --- | --- | --- |
| Tema 1: Arquitecturas Lambda y Kappa | `modulo3/Tema1/M3T1L6.html` | `modulo3/Tema1/M3T1_productor.ipynb`, `modulo3/Tema1/M3T1_consumidor_kafka_basico.ipynb` | Evolucion del ejercicio CoinGecko para incluir Kafka como canal de eventos entre productor y consumidor. | Trabajar con offsets, claves Kafka, comparacion de timestamps, filtros, ventanas y escritura en Parquet. | Kafka, Python, PySpark, Structured Streaming, Jupyter Notebook, Parquet. |
| Tema 2: Kafka y sistemas de mensajeria | `modulo3/Tema2/M3T2L5.html` | `modulo3/Tema2/docker-compose.yml`, `modulo3/Tema2/Dockerfile`, `modulo3/Tema2/crear_laboratorio.sh`, `modulo3/Tema2/KAFKA_SPARK_STREAMING_EXAMPLE_ACTUALIZADO.md` | Laboratorio Kafka + Spark Structured Streaming con eventos tipo tweet en JSON, validacion, cuarentena, metricas y salidas Parquet. | Modernizar un ejemplo clasico con Kafka KRaft, Docker Compose y Structured Streaming; validar datos y medir microbatches. | Docker Compose, Kafka KRaft, Python, PySpark, spark-sql-kafka, JSON, Parquet. |
| Tema 3: Procesamiento de streams con Spark | `modulo3/Tema3/M3T3L5.html` | `modulo3/Tema3/kafka_spark_advanced_lab.zip`, `modulo3/Tema3/kafka_spark_advanced_lab/README.md`, `docker-compose.yml`, `Dockerfile`, `requirements.txt`, `app/producer_orders.py`, `app/streaming_pipeline.py`, `app/validate_outputs.py` | Laboratorio avanzado de pedidos ecommerce: eventos JSON, Kafka, validacion, enriquecimiento, metricas, alertas, Parquet y topic de salida `orders_enriched`. | Construir un pipeline reproducible con checkpoints, control de offsets, separacion de datos validos/cuarentena, alertas y escritura a multiples sinks. | Docker Compose, Kafka KRaft, Python, PySpark, Structured Streaming, spark-sql-kafka, Parquet, JSON, checkpoints. |

## 4. Documentos internos relacionados

| Documento | Relacion con los ejercicios |
| --- | --- |
| `USO_IA_EN_PROYECTO.md` | Define el marco academico y tecnico de uso de IA, incluyendo apoyo en preguntas de autoevaluacion y control humano. |
| `REGISTRO_USO_IA.md` | Registro de trazabilidad del uso de IA en el proyecto. |
| `AUTOEVALUACION_README.md` | Descripcion general del sistema de autoevaluacion. |
| `README_AUTOEVALUACION.md` | Resumen del sistema, temas cubiertos y documentacion de soporte. |
| `GUIA_USUARIO_AUTOEVALUACION.md` | Guia para estudiantes sobre uso del cuestionario. |
| `GUIA_RAPIDA_DESARROLLADORES.md` | Guia para modificar preguntas, estilos y logica. |
| `ESPECIFICACION_TECNICA.md` | Arquitectura, flujo de ejecucion, requisitos y mantenimiento del sistema. |
| `CHECKLIST_IMPLEMENTACION.md` | Lista de validacion funcional y tecnica. |
| `INDICE_DOCUMENTACION.md` | Indice general de documentacion del sistema. |
| `RESUMEN_EJECUTIVO.md` | Resumen ejecutivo y estado de implementacion. |
| `data/structure.json` | Estructura de modulos, temas y lecciones usada como mapa del temario. |

## 5. Referencias externas usadas por las lecciones

Las lecciones de recursos y ejercicios hacen referencia, entre otras, a estas fuentes:

- Documentacion oficial de Apache Spark: guia general, RDD, Spark SQL, DataFrames/Datasets, Structured Streaming, integracion Kafka, monitorizacion, configuracion, tuning, seguridad y despliegue.
- Documentacion oficial de Apache Kafka: introduccion, productores, consumidores, topics, configuraciones y arquitectura.
- Docker Compose Documentation.
- Spark Packages y repositorios GitHub de Apache Spark y Apache Kafka.
- CoinGecko API, usada como fuente de datos para ejercicios de criptomonedas.
- Kaggle Retail Sales Data, usado en el ejercicio de ventas retail del modulo 2, tema 2.
- Prometheus, Grafana, Elastic y OpenTelemetry para monitorizacion y observabilidad.
- Confluent Kafka Connect y Schema Registry, Debezium, Apache Avro, Protocol Buffers y JSON Schema.
- Delta Lake para escenarios de streaming y mejora sobre Parquet.
- Libros y recursos de apoyo: Learning Spark, Designing Data-Intensive Applications, Streaming Systems y Graph Algorithms.

## 6. Tecnologias necesarias

### Para el sitio y la autoevaluacion

- HTML5 y CSS3.
- JavaScript vanilla con `fetch`, eventos DOM y `async/await`.
- JSON para el banco de preguntas.
- Servidor web local o remoto capaz de servir HTML, JS, CSS y JSON mediante HTTP GET.
- Navegador moderno.
- Webpack y `webpack-dev-server` si se usa el flujo definido en `package.json`.

### Para los ejercicios Spark

- Apache Spark.
- PySpark.
- Python.
- Jupyter Notebook.
- PyCharm u otro IDE equivalente.
- CSV, JSON y Parquet como formatos de datos.
- Spark UI para monitorizacion basica.
- Configuracion de recursos Spark: executors, cores, memoria, particiones, cache y checkpoints.

### Para los ejercicios de streaming y Kafka

- Apache Kafka.
- Kafka en modo KRaft en los laboratorios Docker.
- Spark Structured Streaming.
- Conector `spark-sql-kafka-0-10`.
- Docker y Docker Compose.
- Productores Python.
- Checkpoints para tolerancia a fallos y control de offsets.
- Topics Kafka de entrada y salida.
- Sinks Parquet y, como extension, Delta Lake.

### Para monitorizacion y operacion

- Spark UI.
- Prometheus.
- Grafana.
- Logs de contenedores o cluster.
- Posibles herramientas complementarias: Elastic y OpenTelemetry.

## 7. Criterios pedagogicos y de calidad

Los ejercicios siguen un patron progresivo:

1. Conceptos base de Spark y ejecucion distribuida.
2. Transformaciones batch y analisis con DataFrames.
3. Primer contacto con Structured Streaming.
4. Monitorizacion, despliegue y ajuste de recursos.
5. Introduccion de Kafka como sistema de mensajeria.
6. Laboratorios reproducibles con Docker Compose.
7. Pipelines avanzados con validacion, cuarentena, metricas, alertas, checkpoints y multiples sinks.

De acuerdo con `USO_IA_EN_PROYECTO.md`, las preguntas y ejercicios deben mantener correspondencia directa con las lecciones, una unica respuesta correcta en autoevaluaciones, distractores plausibles, validacion tecnica y revision humana final.

## 8. Mantenimiento recomendado

- Mantener sincronizados los `data-module-id` de los HTML con las claves de `js/questions-data.json`.
- Actualizar la cifra de preguntas en los documentos historicos si cambia el banco JSON.
- Revisar periodicamente notebooks, datasets y laboratorios Docker para confirmar que siguen ejecutando.
- Documentar cambios asistidos por IA en `REGISTRO_USO_IA.md`.
- Validar los enlaces externos en las lecciones de recursos.
- Probar `test-autoevaluacion.html` despues de modificar preguntas, partials o logica JavaScript.
