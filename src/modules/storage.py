import os
import csv
from modules.models import Atencion

def guardar_en_csv(atenciones):
    """
    Guarda todas las atenciones registradas en un archivo CSV.
    Si la carpeta 'data' no existe, la crea automáticamente.
    """
    # Crear la carpeta 'src/data' si no existe
    os.makedirs("src/data", exist_ok=True)

    # Definir la ruta completa del archivo CSV
    ruta_archivo = "src/data/atenciones.csv"

    # Abrir el archivo y escribir los datos
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Encabezados del archivo
        writer.writerow(["nombre", "servicio", "responsable", "fecha", "resultado"])

        # Escribir cada registro de atención
        for a in atenciones:
            writer.writerow([a.nombre, a.servicio, a.responsable, a.fecha, a.resultado])

    print(f"\nReporte generado exitosamente en: {ruta_archivo}")


def leer_atenciones():
    """
    Lee las atenciones guardadas en el archivo CSV (si existe)
    y devuelve una lista de diccionarios.
    """
    ruta_archivo = "src/data/atenciones.csv"
    atenciones = []

    # Si el archivo no existe, devolver lista vacía
    if not os.path.exists(ruta_archivo):
        return atenciones

    # Leer los datos desde el CSV
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            # Convertir cada fila del CSV a un diccionario
            atenciones.append({
                "nombre": fila["nombre"],
                "servicio": fila["servicio"],
                "responsable": fila["responsable"],
                "fecha": fila["fecha"],
                "resultado": fila["resultado"]
            })

    return atenciones
