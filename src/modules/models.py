class Atencion:
    def __init__(self, nombre, servicio, responsable, fecha, resultado):
        self.nombre = nombre
        self.servicio = servicio
        self.responsable = responsable
        self.fecha = fecha
        self.resultado = resultado

class GestorAtenciones:
    def __init__(self):
        self.atenciones = []

    def agregar_atencion(self, atencion):
        self.atenciones.append(atencion)

    def listar_atenciones(self):
        return self.atenciones
