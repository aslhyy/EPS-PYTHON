from modules.models import Atencion, GestorAtenciones
from modules.storage import guardar_en_csv, leer_atenciones
from modules.utils import validar_fecha, limpiar_pantalla

def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n=== SISTEMA DE REGISTRO DE ATENCIÓN EPS ===")
    print("1. Registrar nueva atención")
    print("2. Ver atenciones registradas")
    print("3. Generar reporte CSV")
    print("4. Salir")

def registrar_atencion(gestor):
    """
    Permite ingresar los datos de una nueva atención.
    Valida la fecha y maneja excepciones por entradas vacías.
    """
    try:
        print("\n--- Registrar Nueva Atención ---")
        nombre = input("Nombre del beneficiario: ").strip()
        servicio = input("Servicio solicitado: ").strip()
        responsable = input("Responsable: ").strip()
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        resultado = input("Resultado de la atención: ").strip()

        # Validación básica
        if not all([nombre, servicio, responsable, fecha, resultado]):
            print("Todos los campos son obligatorios.")
            return

        # Validar formato de fecha
        if not validar_fecha(fecha):
            print("Fecha inválida. Use el formato YYYY-MM-DD.")
            return

        # Crear objeto y agregar al gestor
        nueva_atencion = Atencion(nombre, servicio, responsable, fecha, resultado)
        gestor.agregar_atencion(nueva_atencion)
        print("Atención registrada exitosamente.")

    except Exception as e:
        print(f"Error al registrar la atención: {e}")

def mostrar_atenciones(gestor):
    """
    Muestra todas las atenciones registradas en memoria.
    """
    atenciones = gestor.listar_atenciones()
    if not atenciones:
        print("\nNo hay atenciones registradas aún.")
        return

    print("\n--- LISTADO DE ATENCIONES ---")
    for i, atencion in enumerate(atenciones, start=1):
        print(f"{i}. {atencion.nombre} | {atencion.servicio} | "
              f"{atencion.responsable} | {atencion.fecha} | {atencion.resultado}")

def generar_reporte_csv(gestor):
    """
    Genera el archivo CSV con todas las atenciones registradas.
    """
    try:
        guardar_en_csv(gestor.listar_atenciones())
        print("Reporte CSV generado exitosamente en data/atenciones.csv")
    except Exception as e:
        print(f"Error al generar el reporte: {e}")

def main():
    """
    Función principal del programa.
    Controla el flujo general y el menú interactivo.
    """
    limpiar_pantalla()
    print("Bienvenida/o al Sistema de Registro de Atención EPS")

    # Cargar datos previos si existen
    gestor = GestorAtenciones()
    datos_guardados = leer_atenciones()
    for d in datos_guardados:
        gestor.agregar_atencion(Atencion(**d))

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()

        if opcion == "1":
            registrar_atencion(gestor)
        elif opcion == "2":
            mostrar_atenciones(gestor)
        elif opcion == "3":
            generar_reporte_csv(gestor)
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Punto de entrada
if __name__ == "__main__":
    main()
