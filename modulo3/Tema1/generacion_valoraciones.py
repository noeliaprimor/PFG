import csv
import os
import random
import time

peliculas = [
    "Matrix",
    "Interstellar",
    "Inception",
    "Titanic",
    "Avatar",
    "Gladiator",
    "Forrest Gump",
    "Pulp Fiction",
    "El Padrino",
    "El Caballero Oscuro"
]

os.makedirs("entrada_valoraciones", exist_ok=True)

contador = 1

while True:

    fichero = f"entrada_valoraciones/valoraciones_{contador:03}.csv"

    with open(fichero, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["pelicula", "usuario", "valoracion"])

        for i in range(10):

            writer.writerow([
                random.choice(peliculas),
                f"u{random.randint(1,500)}",
                random.randint(1,5)
            ])

    print(f"Creado {fichero}")

    contador += 1

    time.sleep(5)