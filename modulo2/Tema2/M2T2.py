
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
    .appName("Retail_Sales_Analysis")
    .getOrCreate()
)

spark

sales_path = "DatasetTema2/sales.csv"
product_path = "DatasetTema2/product_hierarchy.csv"
stores_path = "DatasetTema2/store_cities.csv"




# ## 3. Carga de los ficheros CSV

sales_df = spark.read.csv(sales_path, header=True, inferSchema=True)
product_df = spark.read.csv(product_path, header=True, inferSchema=True)
stores_df = spark.read.csv(stores_path, header=True, inferSchema=True)

print("\n3. Carga de CSV: se comprueba el esquema inferido de ventas para validar columnas y tipos iniciales.")
sales_df.printSchema()

print("\n3. Carga de CSV: se comprueba el esquema de la dimensión de productos.")
product_df.printSchema()

print("\n3. Carga de CSV: se comprueba el esquema de la dimensión de tiendas y ciudades.")
stores_df.printSchema()



# ## 4. Exploración inicial de los datos


print("\n4. Exploración inicial: primeras filas de ventas para revisar el contenido real del dataset.")
sales_df.show(5, truncate=False)

print("\n4. Exploración inicial: primeras filas de la jerarquía de productos.")
product_df.show(5, truncate=False)

print("\n4. Exploración inicial: primeras filas de tiendas y ciudades.")
stores_df.show(5, truncate=False)


# ## 5. Tipado y preparación de `sales.csv`
#
# Este bloque transforma `sales_df` para preparar los datos antes del análisis.
#

sales_df = (
    sales_df
    .withColumn("date", F.to_date("date"))
    .withColumn("sales", F.col("sales").cast("double"))
    .withColumn("revenue", F.col("revenue").cast("double"))
    .withColumn("stock", F.col("stock").cast("double"))
    .withColumn("price", F.col("price").cast("double"))
    .withColumn("promo_discount_2", F.col("promo_discount_2").cast("double"))
    .withColumn("year", F.year("date"))
    .withColumn("month", F.month("date"))
    .withColumn("weekofyear", F.weekofyear("date"))
    .withColumn("is_stockout", F.when(F.col("stock") <= 0, 1).otherwise(0))
    .withColumn("avg_ticket_est", F.when(F.col("sales") != 0, F.col("revenue") / F.col("sales")))
)

print("\n5. Tipado y preparación: esquema después de convertir fechas, métricas numéricas y crear columnas auxiliares.")
sales_df.printSchema()

print("\n5. Tipado y preparación: muestra de ventas ya preparadas para el análisis.")
sales_df.show(5, truncate=False)




# ## 6. Enriquecimiento con dimensiones de producto y tienda
#


retail_df = (
    sales_df
    .join(F.broadcast(product_df), "product_id", "left")
    .join(F.broadcast(stores_df), "store_id", "left")
)

print("\n6. Enriquecimiento: esquema del dataset tras unir ventas con producto y tienda.")
retail_df.printSchema()

print("\n6. Enriquecimiento: muestra del dataset final enriquecido con dimensiones.")
retail_df.show(5, truncate=False)


# ## 7. Comprobación de columnas tras el enriquecimiento


print("\n7. Comprobación: columnas disponibles después del enriquecimiento.")
print(retail_df.columns)


# ## 8. KPI inicial: ventas y facturación por tienda
# 



kpi_store = (
    retail_df
    .groupBy("store_id")
    .agg(
        F.sum("sales").alias("total_sales_qty"),
        F.sum("revenue").alias("total_revenue"),
        F.avg("price").alias("avg_price"),
        F.avg("stock").alias("avg_stock")
    )
    .orderBy(F.desc("total_revenue"))
)

print("\n8. KPI inicial: ventas, facturación, precio medio y stock medio por tienda, ordenado por facturación.")
kpi_store.show(20, truncate=False)




# ## 9. Análisis por ciudad, tipo y tamaño de tienda
# 



kpi_city_storetype = (
    retail_df
    .groupBy("city_id", "storetype_id", "store_size")
    .agg(
        F.sum("sales").alias("sales_qty"),
        F.sum("revenue").alias("revenue_total"),
        F.avg("price").alias("avg_price")
    )
    .orderBy(F.desc("revenue_total"))
)

print("\n9. Análisis por ciudad, tipo y tamaño de tienda: compara ventas y facturación por segmentos de tienda.")
kpi_city_storetype.show(20, truncate=False)




# ## 10. Tabla dinámica (pivot) por tipo de promoción
#
#
# El objetivo es construir una tabla donde:
# - las filas sean las tiendas,
# - las columnas sean los tipos de promoción,
# - y el valor agregado sea la suma de `revenue`.
#
# Este patrón es útil para comparar el impacto económico de distintos tipos promocionales.
#




promo_type_1_values = [r[0] for r in retail_df.select("promo_type_1").distinct().orderBy("promo_type_1").collect() if r[0] is not None]
print("\n10. Tabla dinámica: tipos de promoción detectados que se usarán como columnas del pivot.")
print(promo_type_1_values[:20])





df_pivot_promo1 = (
    retail_df
    .groupBy("store_id")
    .pivot("promo_type_1", promo_type_1_values)
    .agg(F.sum("revenue"))
)

print("\n10. Tabla dinámica: facturación por tienda desglosada por tipo de promoción.")
df_pivot_promo1.show(20, truncate=False)



# ## 11. Top 3 productos por jerarquía principal
# 
# En lugar de utilizar una categoría genérica, aquí se aprovecha la jerarquía real de producto mediante `hierarchy1_id`.
# 
# El procedimiento consiste en:
# 1. agregar ventas por `hierarchy1_id` y `product_id`,
# 2. ordenar por facturación,
# 3. asignar un ranking con `row_number()`,
# 4. filtrar el Top 3 por grupo.
# 
# Este patrón es uno de los usos clásicos de las funciones de ventana.
# 

# In[21]:


df_prod_h1 = (
    retail_df
    .groupBy("hierarchy1_id", "product_id")
    .agg(
        F.sum("revenue").alias("revenue_total"),
        F.sum("sales").alias("sales_qty")
    )
)

w_h1 = Window.partitionBy("hierarchy1_id").orderBy(F.desc("revenue_total"))

df_top_h1 = (
    df_prod_h1
    .withColumn("rn", F.row_number().over(w_h1))
    .filter(F.col("rn") <= 3)
    .drop("rn")
    .orderBy("hierarchy1_id", F.desc("revenue_total"))
)

print("\n11. Top 3 productos por jerarquía principal: ranking de productos con mayor facturación dentro de cada hierarchy1_id.")
df_top_h1.show(50, truncate=False)



# ## 12. Top 3 productos por tienda
# 
# Este análisis cambia la perspectiva: ahora no interesa la jerarquía global, sino el rendimiento de producto dentro de cada tienda.
# 
# Este tipo de ranking puede ser útil para:
# - gestión del surtido,
# - optimización de inventario,
# - detección de productos estrella por ubicación.
# 

# In[22]:


df_prod_store = (
    retail_df
    .groupBy("store_id", "product_id")
    .agg(
        F.sum("revenue").alias("revenue_total"),
        F.sum("sales").alias("sales_qty")
    )
)

w_store = Window.partitionBy("store_id").orderBy(F.desc("revenue_total"))

df_top_store = (
    df_prod_store
    .withColumn("rn", F.row_number().over(w_store))
    .filter(F.col("rn") <= 3)
    .drop("rn")
)

print("\n12. Top 3 productos por tienda: productos con mayor facturación dentro de cada tienda.")
df_top_store.show(50, truncate=False)




# ## 13. Media móvil de 7 días por tienda y producto
# 
# Dado que el dataset tiene granularidad diaria, una ventana temporal móvil es muy adecuada.
# 
# En este caso se calcula la media de `revenue` en los últimos 7 días para cada combinación de:
# - `store_id`
# - `product_id`
# 
# Este tipo de métrica ayuda a suavizar fluctuaciones diarias y detectar tendencias recientes.
# 




w7d = (
    Window
    .partitionBy("store_id", "product_id")
    .orderBy(F.col("date").cast("timestamp").cast("long"))
    .rangeBetween(-7 * 24 * 3600, 0)
)

df_roll_7d = retail_df.withColumn("revenue_avg_7d", F.avg("revenue").over(w7d))

print("\n13. Media móvil de 7 días: suaviza la facturación diaria por tienda y producto para detectar tendencias recientes.")
df_roll_7d.select(
    "store_id", "product_id", "date", "revenue", "revenue_avg_7d"
).show(30, truncate=False)



# ## 14. Media móvil de 30 días
# 
# Una ventana más amplia permite observar tendencias menos sensibles al ruido diario.
# 
# Comparar la media móvil de 7 días con la de 30 días puede resultar útil para detectar:
# - aceleraciones,
# - desaceleraciones,
# - o comportamientos anómalos.
# 




w30d = (
    Window
    .partitionBy("store_id", "product_id")
    .orderBy(F.col("date").cast("timestamp").cast("long"))
    .rangeBetween(-30 * 24 * 3600, 0)
)

df_roll_30d = retail_df.withColumn("revenue_avg_30d", F.avg("revenue").over(w30d))

print("\n14. Media móvil de 30 días: permite observar tendencias más estables y menos sensibles al ruido diario.")
df_roll_30d.select(
    "store_id", "product_id", "date", "revenue", "revenue_avg_30d"
).show(30, truncate=False)




# ## 15. Análisis de roturas de stock
# 
# Una rotura de stock implica que al final del día el producto queda sin inventario disponible.
# Esto puede ser indicio de:
# - alta demanda,
# - mala planificación,
# - o problemas de reposición.
# 
# En este bloque se calcula:
# - el número de días con rotura de stock,
# - el número total de días observados,
# - y el ratio de rotura por combinación tienda-producto.
# 




stockout_kpi = (
    retail_df
    .groupBy("store_id", "product_id")
    .agg(
        F.sum("is_stockout").alias("days_stockout"),
        F.count("*").alias("days_total"),
        (F.sum("is_stockout") / F.count("*")).alias("stockout_ratio")
    )
    .orderBy(F.desc("stockout_ratio"))
)

print("\n15. Roturas de stock: días sin inventario y ratio de rotura por combinación tienda-producto.")
stockout_kpi.show(30, truncate=False)



# ## 16. Días con ventas y stock final nulo
# 
# Una situación especialmente interesante es aquella en la que hay ventas durante el día pero el stock final es cero o negativo.
# 
# Este patrón puede reflejar:
# - fuerte rotación,
# - agotamiento del inventario,
# - o necesidad de revisar el aprovisionamiento.
# 

# In[26]:


df_sales_stock_alert = retail_df.filter(
    (F.col("sales") > 0) & (F.col("stock") <= 0)
)

print("\n16. Alertas de venta con stock final nulo: casos con ventas positivas y stock agotado o negativo.")
df_sales_stock_alert.select(
    "store_id", "product_id", "date", "sales", "revenue", "stock"
).show(30, truncate=False)



# ## 17. Activos e inactivos mediante `left_semi` y `left_anti`
# 
# El dataset no dispone de `customer_id`, por lo que se adapta el patrón clásico de clientes activos/inactivos a pares `store_id` + `product_id`.
# 
# ### Idea del análisis
# 
# - Un par tienda-producto se considera **activo** si aparece en los últimos 30 días del dataset.
# - Se considera **inactivo** si no aparece en ese periodo.
# 
# Esto permite practicar dos joins muy relevantes en Spark:
# - `left_semi`: devuelve las filas del lado izquierdo que sí tienen coincidencia.
# - `left_anti`: devuelve las filas del lado izquierdo que no tienen coincidencia.
# 




max_date = retail_df.agg(F.max("date").alias("max_date")).collect()[0]["max_date"]

recent_df = retail_df.filter(F.col("date") >= F.date_sub(F.lit(max_date), 30))

store_product_pairs = retail_df.select("store_id", "product_id").distinct()
recent_pairs = recent_df.select("store_id", "product_id").distinct()

df_active_pairs = store_product_pairs.join(
    recent_pairs,
    ["store_id", "product_id"],
    "left_semi"
)

df_inactive_pairs = store_product_pairs.join(
    recent_pairs,
    ["store_id", "product_id"],
    "left_anti"
)

print("\n17. Activos e inactivos: pares tienda-producto presentes en los últimos 30 días del dataset.")
print("Pares tienda-producto activos:", df_active_pairs.count())

print("\n17. Activos e inactivos: pares tienda-producto que no aparecen en los últimos 30 días.")
print("Pares tienda-producto inactivos:", df_inactive_pairs.count())




# ## 18. Join por rango temporal con campañas simuladas
# 
# El dataset incluye información promocional a nivel de fila, pero para practicar un `range join` se construye una tabla auxiliar de campañas por periodos.
# 
# Una fila de ventas quedará asociada a una campaña si su fecha está comprendida entre:
# - la fecha de inicio,
# - y la fecha de fin del periodo.
# 
# Este tipo de join es útil en escenarios de:
# - campañas,
# - periodos de validez,
# - reglas activas,
# - ventanas temporales de negocio.
# 




promo_periods = spark.createDataFrame([
    ("campaign_1", "2017-01-01", "2017-06-30"),
    ("campaign_2", "2017-07-01", "2018-06-30"),
    ("campaign_3", "2018-07-01", "2019-12-31")
], ["campaign_id", "start_date", "end_date"])

promo_periods = (
    promo_periods
    .withColumn("start_date", F.to_date("start_date"))
    .withColumn("end_date", F.to_date("end_date"))
)

cond = (
    (retail_df["date"] >= promo_periods["start_date"]) &
    (retail_df["date"] < promo_periods["end_date"])
)

retail_campaign = retail_df.join(F.broadcast(promo_periods), cond, "left")

print("\n18. Join por rango temporal: ventas asociadas a una campaña simulada según la fecha de la venta.")
retail_campaign.select(
    "store_id", "product_id", "date", "revenue", "campaign_id"
).show(20, truncate=False)



# ## 19. KPIs finales
# 
# En este bloque se construyen varios indicadores finales que resumen el comportamiento del dataset desde distintas perspectivas:
# 
# - por jerarquía principal de producto,
# - por tamaño de tienda,
# - por combinación de promociones.
# 
# Este tipo de salidas puede utilizarse como base para las conclusiones  o como tablas auxiliares para gráficos.
# 




kpi_h1 = (
    retail_df
    .groupBy("hierarchy1_id")
    .agg(
        F.sum("sales").alias("sales_qty"),
        F.sum("revenue").alias("revenue_total")
    )
    .orderBy(F.desc("revenue_total"))
)

kpi_store_size = (
    retail_df
    .groupBy("store_size")
    .agg(
        F.sum("sales").alias("sales_qty"),
        F.sum("revenue").alias("revenue_total")
    )
    .orderBy(F.desc("revenue_total"))
)

kpi_promos = (
    retail_df
    .groupBy("promo_type_1", "promo_type_2")
    .agg(
        F.sum("sales").alias("sales_qty"),
        F.sum("revenue").alias("revenue_total")
    )
    .orderBy(F.desc("revenue_total"))
)

print("\n19. KPIs finales: ventas y facturación agregadas por jerarquía principal de producto.")
kpi_h1.show(20, truncate=False)

print("\n19. KPIs finales: ventas y facturación agregadas por tamaño de tienda.")
kpi_store_size.show(20, truncate=False)

print("\n19. KPIs finales: ventas y facturación agregadas por combinación de promociones.")
kpi_promos.show(20, truncate=False)



# ## 20. Guardado opcional en Parquet
# 
# En entornos reales es habitual persistir resultados intermedios o finales en formatos columnares como Parquet.
# 
# Frente a CSV, Parquet ofrece ventajas como:
# - compresión,
# - mejor rendimiento de lectura,
# - y preservación de tipos de datos.
# 




retail_df.write.mode("overwrite").parquet("out/retail_df")
df_pivot_promo1.write.mode("overwrite").parquet("out/df_pivot_promo1")
df_top_h1.write.mode("overwrite").parquet("out/df_top_h1")
stockout_kpi.write.mode("overwrite").parquet("out/stockout_kpi")





spark.stop()
