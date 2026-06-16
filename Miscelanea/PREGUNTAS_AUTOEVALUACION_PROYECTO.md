# Preguntas de autoevaluaci?n del proyecto

Modulo 1. Tema 1: Introducci?n a Big Data
1. ¿Cuáles son las 5 V del Big Data?
a) Volumen, veracidad, valor, variedad, velocidad
b) Volumen, valor, verdad, volatilidad, velocidad
c) Valor, vulnerabilidad, veracidad, verdad, volumen
Respuesta correcta: A
2. Elige la opción falsa:
a) Implementar tecnologías de Big Data puede requerir una inversión significativa.
b) Las empresas siempre recuperan rápidamente la inversión en infraestructuras de Big Data.
c) Los beneficios de las inversiones en Big Data pueden tardar en aparecer.
Respuesta correcta: B
3. ¿Cuáles son las mejores bases de datos para Big Data?
a) Bases de datos relacionales
b) Bases de datos NoSql
c) Bases de datos para datos estructurados
Respuesta correcta: B
4. Elige la opción falsa:
a) La gobernanza efectiva de datos implica establecer políticas que regulen tanto el acceso como la calidad de la información almacenada.
b) La falta de gobernanza adecuada puede llevar a problemas de seguridad y cumplimiento normativo, afectando la confianza en los análisis de datos.
c) Una vez establecida, la gobernanza de datos no requiere ajustes ni revisiones, ya que las políticas son universales e inmutables.
Respuesta correcta: C
5. Elije la opción correcta:
a) Machine Learning y Big data engloban todas las aplicaciones para Inteligencia Artificial
b) La Inteligencia Artificial siempre utiliza Big Data ya que se apoya en los datos para el aprendizaje
c) Mediante Machine Learning somos capaces de aprender patrones de los datos y utilizarlos en aplicaciones de Big Data
Respuesta correcta: C
6. Elije la opción falsa:
a) Hadoop es una plataforma de software libre para el almacenamiento y procesamiento de datos a gran escala.
b) Big Data Analytics no tiene nada que ver con Inteligencia Artificial, se apoya solo en Machine Learning y Big Data.
c) Los orígenes del big data se remontan a los años 60 y 70.
Respuesta correcta: B
7. Elije la opción correcta:
a) La interacción entre Big Data y Machine Learning permite la automatización de procesos analíticos complejos.
b) La Inteligencia Artificial no requiere grandes volúmenes de datos para mejorar su capacidad predictiva.
c) Big Data se utiliza principalmente para reemplazar la necesidad de modelos de Machine Learning en análisis avanzados.
Respuesta correcta: A
8. Elije la opción falsa:
a) Una de las grandes ventajas del Big Data es que existen muchos profesionales cualificados para ello.
b) Los elevados costos del Big Data pueden llevar a que las empresas no inviertan en esta tecnología.
c) Se han tenido que crear nuevas infraestructuras robustas para gestionar la cantidad masiva de datos.
Respuesta correcta: A
9. Elije la opción correcta:
a) La Inteligencia Artificial necesita que los datos estén preprocesados manualmente antes de poder utilizarlos.
b) Los algoritmos de Machine Learning pueden mejorar sus predicciones a medida que procesan más datos provenientes de Big Data.
c) Big Data y Machine Learning son independientes y no se benefician mutuamente.
Respuesta correcta: B
10. Elije la opción correcta:
a) En el sector financiero, Big Data se utiliza principalmente para optimizar campañas de marketing y detección de fraude.
b) En el ámbito de la salud, Big Data ayuda a prevenir enfermedades con antelación.
c) El uso de Big Data en el transporte se limita únicamente a la creación de planes electorales.
Respuesta correcta: A

Modulo 2. Tema 1: Introducci?n e instalaci?n de Apache Spark
1. ¿Cuál es la ventaja principal de Spark frente a enfoques batch tradicionales?
a) Procesamiento en memoria para acelerar tareas iterativas
b) Obligar siempre a usar SQL
c) Eliminar la necesidad de clúster
Respuesta correcta: A
2. ¿Qué componente actúa como coordinador principal en una aplicación Spark?
a) Executor
b) Worker
c) Driver
Respuesta correcta: C
3. ¿Qué describen mejor los executors en Spark?
a) Procesos que ejecutan tareas y almacenan datos en caché
b) Interfaces web para monitorización
c) Gestores de paquetes del sistema operativo
Respuesta correcta: A
4. ¿Qué gestores de clúster aparecen en el tema?
a) Docker Swarm, Nomad y Mesos únicamente
b) YARN, Standalone y Kubernetes
c) Solo Kubernetes
Respuesta correcta: B
5. ¿Qué propiedad caracteriza a un RDD?
a) Tabla relacional persistente en disco local
b) Conjunto distribuido, inmutable y tolerante a fallos
c) Estructura mutable sin linaje
Respuesta correcta: B
6. En spark.read.csv('datos.csv', header=True), ¿qué hace header=True?
a) Indica que la primera fila contiene nombres de columnas
b) Activa el modo streaming
c) Guarda automáticamente en Parquet
Respuesta correcta: A
7. ¿Qué entorno interactivo se usa para trabajar con Spark en Python?
a) PL/SQL
b) PowerShell
c) PySpark
Respuesta correcta: C
8. ¿Qué comando se usa habitualmente para lanzar una aplicación Spark empaquetada?
a) spark-install
b) spark-submit
c) spark-cluster-init
Respuesta correcta: B
9. Si ejecutas rdd = sc.parallelize([1,2,3,4]), ¿qué estás creando?
a) Un RDD distribuido a partir de una colección local
b) Un DataFrame SQL con esquema fijo
c) Un topic de Kafka
Respuesta correcta: A
10. ¿Cuál es un criterio importante para validar una instalación de Spark?
a) Tener únicamente Java instalado
b) No usar variables de entorno
c) Poder ejecutar ejemplos y ver la aplicación en la UI de Spark
Respuesta correcta: C

Modulo 2. Tema 2: Procesamiento paralelo con Spark (APIs y t?cnicas)
1. ¿Cuál es uno de los principales entornos de ejecución de Apache Spark?
a) Docker Engine
b) Standalone
c) MySQL Server
Respuesta correcta: B
2. ¿Qué componente coordina la ejecución de una aplicación Spark?
a) Executor
b) Worker
c) Driver
Respuesta correcta: C
3. ¿Qué comando se utiliza para ejecutar una aplicación Spark desde consola?
a) spark-run
b) spark-exec
c) spark-submit
Respuesta correcta: C
4. ¿Cuál es el punto de entrada principal en aplicaciones Spark modernas?
a) SparkContext
b) SparkSession
c) SQLContext
Respuesta correcta: B
5. ¿Qué componente es responsable de la ejecución de tareas en nodos de trabajo?
a) Executor
b) Driver
c) Scheduler
Respuesta correcta: A
6. ¿En qué lenguaje se puede inicializar Spark además de Python?
a) Scala
b) HTML
c) SQL puro
Respuesta correcta: A
7. ¿Qué método se usa para crear o recuperar una SparkSession?
a) createSession()
b) startSession()
c) getOrCreate()
Respuesta correcta: C
8. ¿Qué formato de datos es más eficiente para almacenamiento en Spark?
a) CSV
b) Parquet
c) TXT
Respuesta correcta: B
9. ¿Cuál es la estructura de datos de más bajo nivel en Spark?
a) DataFrame
b) Dataset
c) RDD
Respuesta correcta: C
10. ¿Qué API proporciona optimización automática mediante Catalyst?
a) RDD
b) DataFrame
c) HDFS
Respuesta correcta: B
11. ¿Qué característica define a los RDD?
a) Inmutabilidad
b) Persistencia automática
c) Indexación relacional
Respuesta correcta: A
12. ¿Qué significa paralelizar una colección en Spark?
a) Guardar datos en memoria
b) Dividir los datos en particiones para procesarlos en paralelo
c) Ordenar datos automáticamente
Respuesta correcta: B
13. ¿Qué concepto permite distribuir datos en múltiples nodos?
a) Serialización
b) Indexación
c) Particionado
Respuesta correcta: C
14. ¿Cuál de las siguientes es una transformación sobre RDD?
a) map
b) collect
c) count
Respuesta correcta: A
15. ¿Cuál de las siguientes es una acción en Spark?
a) collect
b) map
c) filter
Respuesta correcta: A
16. ¿Qué optimización permite evitar movimientos de datos en joins pequeños?
a) Shuffle Join
b) Broadcast Join
c) Cartesian Join
Respuesta correcta: B
17. ¿Qué técnica mejora el rendimiento al reutilizar datos en memoria?
a) Sort
b) Filter
c) Cache
Respuesta correcta: C
18. ¿Qué API permite trabajar con datos estructurados en Spark?
a) RDD
b) Spark Core
c) DataFrame/Dataset
Respuesta correcta: C
19. ¿Qué función permite aplicar operaciones sobre ventanas en DataFrames?
a) groupBy
b) window
c) join
Respuesta correcta: B
20. ¿Cuál es una ventaja clave de los DataFrames frente a los RDD?
a) Optimización automática del plan de ejecución
b) Mayor control manual del código
c) Menor uso de memoria siempre
Respuesta correcta: A

Modulo 2. Tema 3: Librer?as y componentes de Spark
1. ¿Cuál es la principal función de Apache Spark SQL?
a) Permitir consultas estructuradas mediante SQL y DataFrames
b) Procesar grafos distribuidos
c) Gestionar el almacenamiento en HDFS
Respuesta correcta: A
2. ¿Qué componente de Spark se utiliza para procesamiento de grafos?
a) MLlib
b) GraphX
c) Spark Streaming
Respuesta correcta: B
3. ¿Cuál es la evolución moderna de Spark Streaming?
a) GraphFrames
b) Structured Streaming
c) Spark SQL
Respuesta correcta: B
4. ¿Qué biblioteca de Spark se utiliza para Machine Learning?
a) GraphX
b) Spark SQL
c) MLlib
Respuesta correcta: C
5. ¿Qué abstracción principal utiliza Spark SQL?
a) DataFrame
b) RDD
c) Graph
Respuesta correcta: A
6. ¿Qué permite Catalyst Optimizer en Spark SQL?
a) Ejecutar código en GPU
b) Optimizar consultas de forma automática
c) Gestionar nodos del cluster
Respuesta correcta: B
7. ¿Qué tipo de procesamiento realiza Spark Streaming?
a) Procesamiento batch puro
b) Procesamiento exclusivamente en memoria
c) Procesamiento en micro-batches
Respuesta correcta: C
8. ¿Cuál es una ventaja de Structured Streaming frente a Spark Streaming clásico?
a) Unifica batch y streaming mediante DataFrames
b) No necesita cluster
c) Solo trabaja con JSON
Respuesta correcta: A
9. ¿Qué tipo de datos procesa GraphX?
a) Grafos dirigidos y no dirigidos
b) Datos tabulares
c) Imágenes
Respuesta correcta: A
10. ¿Qué algoritmo es típico en GraphX?
a) K-means
b) Regresión lineal
c) PageRank
Respuesta correcta: C
11. ¿Qué formato permite consultar datos con SQL en Spark?
a) RDD plano
b) DataFrame
c) Socket
Respuesta correcta: B
12. ¿Qué función permite ejecutar consultas SQL en Spark?
a) spark.read()
b) spark.sql()
c) spark.stream()
Respuesta correcta: B
13. ¿Qué hace el siguiente código? spark.readStream.format("json").load("input/")
a) Lee datos batch desde JSON
b) Escribe datos en JSON
c) Lee datos en streaming desde archivos JSON
Respuesta correcta: C
14. ¿Qué hace el siguiente código? df.groupBy("coin").avg("price")
a) Agrupa y calcula la media
b) Filtra datos
c) Ordena datos
Respuesta correcta: A
15. ¿Qué permite MLlib?
a) Procesar streams
b) Entrenar modelos de Machine Learning distribuidos
c) Gestionar grafos
Respuesta correcta: B
16. ¿Qué tipo de aprendizaje soporta MLlib?
a) Solo supervisado
b) Solo aprendizaje profundo
c) Supervisado y no supervisado
Respuesta correcta: C
17. ¿Cuál es el modo de salida típico en Structured Streaming para agregaciones?
a) update
b) overwrite
c) append
Respuesta correcta: A
18. ¿Qué hace withWatermark en streaming?
a) Ordena datos
b) Elimina duplicados automáticamente
c) Gestiona datos tardíos
Respuesta correcta: C
19. ¿Qué representa una ventana en streaming?
a) Un archivo
b) Un intervalo de tiempo para agrupar datos
c) Una tabla en memoria
Respuesta correcta: B
20. ¿Qué librería usarías para combinar datos estructurados con consultas SQL y streaming?
a) Spark SQL + Structured Streaming
b) GraphX
c) MLlib
Respuesta correcta: A

Modulo 2. Tema 4: Configuraci?n, monitorizaci?n y optimizaci?n de Spark
1. ¿Qué componente de Spark permite monitorizar la ejecución de jobs, stages y tareas en tiempo real?
a) SparkContext
b) MLlib
c) Spark UI
Respuesta correcta: C
2. ¿Qué información crítica se puede analizar en la pestaña 'Stages' de la Spark UI?
a) Tiempo de ejecución, shuffle y fallos de tareas
b) Solo configuración del cluster
c) Código fuente de la aplicación
Respuesta correcta: A
3. ¿Qué problema indica un alto tiempo en 'shuffle read' en la Spark UI?
a) Falta de memoria en el driver
b) Coste elevado en transferencia de datos entre nodos
c) Error de configuración del cluster
Respuesta correcta: B
4. ¿Qué parámetro controla el número de particiones en operaciones de shuffle en Spark SQL?
a) spark.executor.memory
b) spark.driver.cores
c) spark.sql.shuffle.partitions
Respuesta correcta: C
5. ¿Qué consecuencia tiene un valor demasiado alto de 'spark.sql.shuffle.partitions'?
a) Sobrecarga por exceso de tareas pequeñas
b) Falta de paralelismo
c) Pérdida de datos
Respuesta correcta: A
6. ¿Qué hace el siguiente código? spark = SparkSession.builder.config("spark.executor.memory", "4g").getOrCreate()
a) Define la memoria del driver
b) Configura la memoria disponible para cada executor
c) Limita el uso de disco
Respuesta correcta: B
7. ¿Cuál es una causa común del error 'OutOfMemoryError' en Spark?
a) Particiones demasiado grandes o mal dimensionadas
b) Uso de DataFrames
c) Uso de SQL
Respuesta correcta: A
8. ¿Qué técnica ayuda a reducir el consumo de memoria en Spark?
a) Usar persistencia en disco siempre
b) Reducir el número de executors
c) Aumentar el número de particiones
Respuesta correcta: C
9. ¿Qué mecanismo permite a Spark recuperarse ante fallos en streaming?
a) RDD caching
b) Shuffle
c) Checkpointing
Respuesta correcta: C
10. ¿Qué ocurre si no se configura correctamente el checkpoint en Structured Streaming?
a) Se pierde el estado y no hay recuperación ante fallos
b) Mejora el rendimiento
c) Se duplican los datos automáticamente
Respuesta correcta: A
11. ¿Qué protocolo se utiliza habitualmente para asegurar la comunicación en Spark?
a) HTTP sin cifrado
b) SSL/TLS
c) FTP
Respuesta correcta: B
12. ¿Qué sistema de autenticación es común en entornos Hadoop con Spark?
a) Kerberos
b) OAuth
c) JWT
Respuesta correcta: A
13. ¿Qué riesgo existe si Spark se despliega sin autenticación en un cluster?
a) Mejora del rendimiento
b) Fallo en el scheduler
c) Acceso no autorizado y ejecución de código malicioso
Respuesta correcta: C
14. ¿Qué modo de despliegue permite ejecutar Spark sin gestor de recursos externo?
a) YARN
b) Standalone
c) Kubernetes
Respuesta correcta: B
15. ¿Qué ventaja tiene desplegar Spark en Kubernetes?
a) Menor escalabilidad
b) Gestión automática de contenedores y escalado
c) Menor seguridad
Respuesta correcta: B
16. ¿Qué indica el error 'Task not serializable'?
a) Error de memoria
b) Fallo en el cluster
c) Se intenta enviar un objeto no serializable a los executors
Respuesta correcta: C
17. ¿Cómo se puede solucionar el error 'Task not serializable'?
a) Evitar referencias a objetos no serializables o usar funciones puras
b) Reduciendo memoria
c) Aumentando particiones
Respuesta correcta: A
18. ¿Qué ocurre si el 'driver' falla durante la ejecución?
a) Los executors continúan trabajando
b) Solo se pierde un stage
c) La aplicación completa falla
Respuesta correcta: C
19. ¿Qué herramienta externa se usa frecuentemente para monitorización avanzada de Spark?
a) Prometheus y Grafana
b) Excel
c) Word
Respuesta correcta: A
20. ¿Qué indica una alta latencia en procesamiento de micro-batches en streaming?
a) Procesamiento eficiente
b) El sistema no procesa datos al ritmo de llegada
c) Falta de datos
Respuesta correcta: B

Modulo 3. Tema 1: Arquitecturas Lambda y Kappa
1. ¿Cuál es la principal característica del procesamiento en tiempo real?
a) Procesar datos únicamente en lotes
b) Procesar y analizar datos a medida que se generan
c) Reducir el tamaño de los datos almacenados
Respuesta correcta: B
2. ¿Qué diferencia principal existe entre procesamiento batch y procesamiento streaming?
a) El streaming no utiliza memoria
b) El batch siempre es más rápido
c) El batch trabaja con datos históricos y el streaming con datos continuos
Respuesta correcta: C
3. ¿Qué tipo de aplicación requiere normalmente procesamiento en tiempo real?
a) Análisis de logs históricos una vez al mes
b) Monitorización de sensores IoT
c) Archivado de copias de seguridad
Respuesta correcta: B
4. ¿Cuál es uno de los principales retos del procesamiento en tiempo real?
a) Gestión de latencia y escalabilidad
b) Eliminación de bases de datos
c) Reducción de almacenamiento físico
Respuesta correcta: A
5. ¿Qué característica define a la arquitectura Lambda?
a) Uso exclusivo de procesamiento batch
b) Uso obligatorio de Kafka
c) Combinación de capas batch y streaming
Respuesta correcta: C
6. ¿Qué objetivo tiene la capa batch en arquitectura Lambda?
a) Procesar datos históricos completos con alta precisión
b) Procesar datos únicamente en memoria
c) Gestionar mensajes en cola
Respuesta correcta: A
7. ¿Qué función cumple la capa speed layer en arquitectura Lambda?
a) Guardar copias de seguridad
b) Reducir particiones
c) Procesar datos recientes con baja latencia
Respuesta correcta: C
8. ¿Cuál es una desventaja importante de la arquitectura Lambda?
a) No soporta procesamiento distribuido
b) Complejidad de mantenimiento por duplicar lógica
c) No permite escalabilidad
Respuesta correcta: B
9. ¿Qué simplificación propone la arquitectura Kappa frente a Lambda?
a) Usar una única capa basada en streaming
b) Eliminar el procesamiento streaming
c) Eliminar almacenamiento distribuido
Respuesta correcta: A
10. ¿Qué tecnología suele utilizarse como backbone en arquitecturas Kappa?
a) Excel
b) Kafka
c) FTP
Respuesta correcta: B
11. ¿Cuál es la principal función de Apache Kafka?
a) Entrenar modelos de Machine Learning
b) Procesar grafos
c) Actuar como sistema distribuido de mensajería y streaming
Respuesta correcta: C
12. ¿Qué elemento de Kafka almacena los mensajes?
a) RDD
b) Executor
c) Topic
Respuesta correcta: C
13. ¿Qué ventaja proporciona la partición de topics en Kafka?
a) Paralelismo y escalabilidad
b) Reducción del uso de memoria
c) Eliminación de consumidores
Respuesta correcta: A
14. ¿Qué ocurre si varios consumidores pertenecen al mismo consumer group en Kafka?
a) Todos leen exactamente los mismos mensajes
b) Los mensajes se distribuyen entre los consumidores
c) Kafka deja de funcionar
Respuesta correcta: B
15. ¿Qué hace el siguiente código en PySpark? spark.readStream.format("kafka").option("subscribe", "crypto").load()
a) Escribe mensajes en Kafka
b) Lee datos en streaming desde un topic Kafka
c) Crea un topic automáticamente
Respuesta correcta: B
16. ¿Qué modelo de procesamiento utiliza Spark Streaming clásico?
a) Micro-batches
b) Procesamiento continuo puro
c) Procesamiento exclusivamente batch
Respuesta correcta: A
17. ¿Qué ventaja principal ofrece Structured Streaming frente al Spark Streaming clásico?
a) Eliminación de SparkContext
b) Procesamiento únicamente batch
c) API unificada basada en DataFrames
Respuesta correcta: C
18. ¿Qué representa una ventana temporal en Spark Streaming?
a) Un intervalo de tiempo usado para agrupar eventos
b) Una tabla SQL
c) Un fichero de configuración
Respuesta correcta: A
19. ¿Qué problema resuelve withWatermark() en Structured Streaming?
a) Compresión de datos
b) Creación de topics Kafka
c) Gestión de eventos tardíos
Respuesta correcta: C
20. ¿Qué arquitectura sería más adecuada para un sistema moderno basado completamente en eventos y streaming?
a) Arquitectura monolítica
b) Arquitectura Kappa
c) Arquitectura cliente-servidor tradicional
Respuesta correcta: B

Modulo 3. Tema 2: Kafka y sistemas de mensajer?a
1. ¿Qué describe mejor un evento en una arquitectura de datos en tiempo real?
a) Una consulta SQL ejecutada al final del día
b) Un fichero comprimido usado solo para backup
c) Una unidad de información que representa algo que ya ha ocurrido
Respuesta correcta: C
2. ¿Para qué sirve normalmente el campo event_id en un evento?
a) Para definir el número de brokers del clúster
b) Para identificar el evento y facilitar deduplicación
c) Para sustituir el checkpoint de Spark
Respuesta correcta: B
3. ¿Cuál es la diferencia entre tiempo de evento y tiempo de procesamiento?
a) El tiempo de evento indica cuándo ocurrió el hecho; el de procesamiento, cuándo Spark lo procesa
b) Son equivalentes en todos los sistemas de streaming
c) El tiempo de procesamiento siempre se genera en Kafka Connect
Respuesta correcta: A
4. ¿Qué patrón convierte cambios de una base de datos en eventos consumibles por otros sistemas?
a) CDC (Change Data Capture)
b) CSS
c) RAID
Respuesta correcta: A
5. ¿Qué ventaja aporta Kafka al situarse entre productores y consumidores?
a) Elimina la necesidad de definir esquemas
b) Desacopla ritmos de producción y consumo y permite retención/reprocesamiento
c) Convierte automáticamente todos los datos en tablas relacionales
Respuesta correcta: B
6. ¿Dónde garantiza Kafka el orden de los mensajes?
a) Dentro de todo el clúster sin importar la clave
b) Solo cuando el consumidor usa CSV
c) Dentro de una misma partición
Respuesta correcta: C
7. ¿Qué representa el offset en Kafka?
a) El tamaño máximo de un topic
b) La posición de un mensaje dentro de una partición
c) La contraseña del consumidor
Respuesta correcta: B
8. ¿Qué indica un consumer lag creciente?
a) Que los consumidores procesan más despacio de lo que llegan los eventos
b) Que el topic no tiene particiones
c) Que Spark ha borrado el esquema
Respuesta correcta: A
9. ¿Qué configuración de productor ayuda a evitar duplicados causados por reintentos?
a) retention.ms=0
b) cleanup.policy=delete
c) enable.idempotence=true
Respuesta correcta: C
10. ¿Qué hace la compactación de un topic Kafka?
a) Conserva el último valor conocido para cada clave
b) Ordena todos los mensajes por timestamp global
c) Convierte mensajes JSON en Parquet automáticamente
Respuesta correcta: A
11. ¿Para qué sirve checkpointLocation en Spark Structured Streaming?
a) Para definir el número de particiones de Kafka
b) Para instalar conectores JDBC
c) Para almacenar estado y offsets y poder recuperarse ante fallos
Respuesta correcta: C
12. ¿Qué contiene normalmente la columna value al leer desde Kafka con Spark?
a) El número total de brokers
b) El contenido del mensaje, normalmente en binario, que debe convertirse y parsearse
c) El directorio de checkpoint
Respuesta correcta: B
13. ¿Cuál es la función del Output Mode en Structured Streaming?
a) Configurar la autenticación SASL
b) Crear automáticamente una SparkSession
c) Definir cómo se escriben los resultados en el sink
Respuesta correcta: C
14. ¿Cuáles son los modos de salida principales en Structured Streaming?
a) Read, Parse y Delete
b) Append, Update y Complete
c) Leader, Follower y Controller
Respuesta correcta: B
15. ¿Qué controla un trigger en una consulta de streaming?
a) La frecuencia con la que se ejecutan los microbatches
b) El formato físico del log de Kafka
c) La clave primaria de una tabla JDBC
Respuesta correcta: A
16. ¿Qué problema ayuda a gestionar un watermark?
a) Cifrado de credenciales
b) Eventos tardíos y limpieza de estado en agregaciones temporales
c) Creación de topics compactados
Respuesta correcta: B
17. ¿Qué es un sink en Spark Structured Streaming?
a) El nodo que coordina particiones de Kafka
b) El esquema usado para inferir JSON automáticamente
c) El destino donde se escriben los resultados de una consulta continua
Respuesta correcta: C
18. ¿Por qué Parquet suele ser adecuado como sink analítico?
a) Porque es columnar, comprimible y eficiente para leer subconjuntos de columnas
b) Porque solo permite almacenar texto plano
c) Porque no necesita particiones ni metadatos
Respuesta correcta: A
19. Para escribir en Kafka desde Spark, ¿qué columna debe contener el DataFrame como mínimo?
a) checkpoint
b) broker_count
c) value
Respuesta correcta: C
20. ¿Para qué se usa foreachBatch?
a) Para borrar offsets antiguos de Kafka
b) Para aplicar lógica batch personalizada sobre cada microbatch
c) Para reemplazar el esquema de un topic
Respuesta correcta: B
21. ¿Qué significa que un sink sea idempotente?
a) Que repetir la misma escritura no deja el destino en un estado incorrecto
b) Que solo puede escribir una fila por segundo
c) Que no necesita autenticación
Respuesta correcta: A
22. En el ejercicio propuesto del tema, ¿qué genera el notebook productor?
a) Tablas Delta con datos históricos ya agregados
b) Usuarios y permisos de Kafka
c) Eventos JSON de pedidos en una carpeta de entrada
Respuesta correcta: C
23. En el ejercicio propuesto, ¿qué tarea realiza el notebook consumidor?
a) Lee eventos con Spark Structured Streaming, valida datos, calcula métricas y escribe sinks
b) Entrena un modelo de deep learning
c) Compila el sitio web estático
Respuesta correcta: A
24. ¿Qué riesgo aparece si se borra un checkpoint de una consulta de streaming sin estrategia clara?
a) Kafka elimina todos los brokers del clúster
b) Spark puede perder la referencia de offsets procesados y repetir o cambiar la posición de lectura
c) Parquet deja de ser un formato columnar
Respuesta correcta: B

Modulo 3. Tema 3: Procesamiento de streams con Spark
1. ¿Qué es un DStream en Spark Streaming clásico?
a) Una secuencia de RDDs generados a intervalos regulares
b) Una tabla Delta con transacciones ACID
c) Un broker Kafka embebido en Spark
Respuesta correcta: A
2. ¿Qué compromiso introduce el intervalo de micro-batch?
a) Define el número de topics Kafka
b) Elimina la necesidad de checkpoints
c) Equilibra latencia y sobrecarga de planificación
Respuesta correcta: C
3. ¿Cuál es la API recomendada para nuevos desarrollos de streaming en Spark?
a) DStreams obligatoriamente
b) Structured Streaming con DataFrames/Datasets
c) RDDs manuales sin SparkSession
Respuesta correcta: B
4. ¿Para qué se usa checkpointing en operaciones de streaming con estado?
a) Para recuperar estado y progreso tras fallos
b) Para comprimir mensajes JSON
c) Para crear automáticamente topics Kafka
Respuesta correcta: A
5. En la integración Spark-Kafka, ¿qué contiene normalmente la columna value?
a) El número de executors de Spark
b) El payload del mensaje en formato binario
c) La ruta del sink Parquet
Respuesta correcta: B
6. ¿Por qué conviene definir un esquema explícito al leer JSON en streaming?
a) Para desactivar todos los microbatches
b) Para impedir la escritura en Parquet
c) Para validar tipos y evitar inferencias costosas o inestables
Respuesta correcta: C
7. Si ya existe un checkpoint, ¿qué ocurre con startingOffsets?
a) Spark usa la posición guardada en el checkpoint
b) Spark ignora siempre el checkpoint
c) Kafka borra los offsets antiguos
Respuesta correcta: A
8. ¿Para qué sirve maxOffsetsPerTrigger al leer desde Kafka?
a) Para cambiar el formato de JSON a Avro
b) Para borrar particiones vacías
c) Para limitar la cantidad de datos leídos por trigger
Respuesta correcta: C
9. ¿Qué permite un watermark en agregaciones por tiempo de evento?
a) Autenticar productores Kafka
b) Gestionar eventos tardíos y limpiar estado de ventanas antiguas
c) Aumentar automáticamente el número de brokers
Respuesta correcta: B
10. ¿Cuándo es adecuado el modo de salida append en ventanas?
a) Cuando Spark puede emitir resultados finales, normalmente con watermark
b) Cuando se quiere reescribir todo el resultado en cada microbatch
c) Solo cuando no existe checkpoint
Respuesta correcta: A
11. ¿Qué controla un trigger en Structured Streaming?
a) La frecuencia de ejecución de microbatches
b) El nombre del topic de salida
c) El tipo de compresión de Parquet
Respuesta correcta: A
12. ¿Para qué se usa foreachBatch?
a) Para crear particiones Kafka desde Spark
b) Para aplicar lógica batch personalizada a cada microbatch
c) Para leer datos sin esquema
Respuesta correcta: B
13. ¿Qué precaución debe tomarse al usar foreachBatch en producción?
a) Eliminar siempre el checkpoint antes de arrancar
b) Usar únicamente salida por consola
c) Diseñar escrituras idempotentes ante reintentos
Respuesta correcta: C
14. En el caso de clickstream, ¿qué métrica se calcula típicamente por ventana?
a) Número de brokers instalados
b) Usuarios activos o URLs más visitadas
c) Tamaño del fichero CSS
Respuesta correcta: B
15. En el caso de detección de fraude simple, ¿qué patrón se busca?
a) Cambios en la hoja de estilos
b) Duplicación de notebooks
c) Picos de transacciones por tarjeta en ventanas cortas
Respuesta correcta: C
16. ¿Qué representa una capa Bronze en un pipeline de streaming?
a) Datos crudos o casi crudos conservados para trazabilidad
b) Solo métricas finales para dashboards
c) El fichero de configuración de Kafka
Respuesta correcta: A
17. ¿Qué representa una capa Silver en un pipeline Bronze-Silver?
a) Datos sin parsear y sin control de calidad
b) Un checkpoint corrupto
c) Datos limpios, validados, deduplicados o enriquecidos
Respuesta correcta: C
18. ¿Por qué Parquet es útil como sink analítico?
a) Porque es columnar, comprimible y eficiente para consultas posteriores
b) Porque solo admite datos sin esquema
c) Porque sustituye a Kafka como broker
Respuesta correcta: A
19. ¿Qué añade Delta Lake sobre Parquet en escenarios de streaming?
a) Una API para crear páginas HTML
b) Transacciones, log de cambios y mejor soporte para escrituras consistentes
c) Un algoritmo para eliminar SparkSession
Respuesta correcta: B
20. ¿Qué prueba ayuda a verificar la recuperación de un pipeline streaming?
a) Cambiar todos los timestamps a texto libre
b) Detener y reiniciar la consulta usando el mismo checkpoint
c) Eliminar todos los sinks antes de validar
Respuesta correcta: B
21. ¿Qué métrica conviene documentar en una consulta streaming?
a) Registros procesados por segundo y duración de microbatch
b) Número de etiquetas HTML del índice
c) Cantidad de colores usados en CSS
Respuesta correcta: A
22. ¿Qué riesgo existe al borrar un checkpoint sin estrategia clara?
a) Parquet deja de ser columnar
b) El navegador deja de cargar HTML
c) La consulta puede reprocesar datos o arrancar desde una posición distinta
Respuesta correcta: C
