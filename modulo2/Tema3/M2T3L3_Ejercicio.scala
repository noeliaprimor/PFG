import org.apache.spark.sql.SparkSession
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

object M2T3L3EjercicioCineGraphX {

  case class Nodo(tipo: String, nombre: String, anio: String)

  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder()
      .appName("M2T3L3 Cine GraphX")
      .master("local[*]")
      .getOrCreate()

    val verticesPath =
      if (args.length > 0) args(0) else "cine_vertices.csv"

    val aristasPath =
      if (args.length > 1) args(1) else "cine_aristas.csv"

    val verticesRaw = spark.read
      .option("header", "true")
      .csv(verticesPath)

    val aristasRaw = spark.read
      .option("header", "true")
      .csv(aristasPath)

    val vertices: RDD[(VertexId, Nodo)] = verticesRaw.rdd.map(row => {
      val id = row.getAs[String]("id").toLong
      val tipo = row.getAs[String]("tipo")
      val nombre = row.getAs[String]("nombre")
      val anio = Option(row.getAs[String]("anio")).getOrElse("")
      (id, Nodo(tipo, nombre, anio))
    })

    val aristas: RDD[Edge[String]] = aristasRaw.rdd.map(row => {
      val src = row.getAs[String]("src").toLong
      val dst = row.getAs[String]("dst").toLong
      val relacion = row.getAs[String]("relacion")
      Edge(src, dst, relacion)
    })

    val grafo = Graph(vertices, aristas)

    println("===== Relaciones del grafo =====")
    grafo.triplets.collect().foreach { t =>
      println(s"${t.srcAttr.nombre} --${t.attr}--> ${t.dstAttr.nombre}")
    }

    println()
    println("===== Grado de cada vertice =====")

    val grados = grafo.degrees

    grados.join(vertices)
      .sortBy { case (_, (grado, nodo)) => (-grado, nodo.nombre) }
      .collect()
      .foreach {
        case (_, (grado, nodo)) =>
          println(s"${nodo.nombre} (${nodo.tipo}) tiene grado $grado")
      }

    println()
    println("===== Peliculas con mas relaciones =====")

    grados.join(vertices)
      .filter { case (_, (_, nodo)) => nodo.tipo == "pelicula" }
      .sortBy { case (_, (grado, nodo)) => (-grado, nodo.nombre) }
      .take(5)
      .foreach {
        case (_, (grado, nodo)) =>
          println(s"${nodo.nombre} (${nodo.anio}) tiene $grado relaciones")
      }

    spark.stop()
  }
}
