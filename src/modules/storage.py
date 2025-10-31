import csv
def guardar_en_csv(lista_atenciones):
    with open("src/data/atenciones.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Servicio", "Responsable", "Fecha", "Resultado"])
        for a in lista_atenciones:
            writer.writerow([a.nombre, a.servicio, a.responsable, a.fecha, a.resultado])

def leer_atenciones():
    return []  # vacío por ahora
