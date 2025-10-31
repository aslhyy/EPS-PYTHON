def mostrar_menu():
    print("\n=== SISTEMA DE REGISTRO DE ATENCIÓN EPS ===")
    print("1. Registrar nueva atención")
    print("2. Ver atenciones registradas")
    print("3. Generar reporte CSV")
    print("4. Salir")

def main():
    print("Bienvenida/o al Sistema de Registro de Atención EPS 🏥")
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        if opcion == "4":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Funcionalidad en desarrollo...")

if __name__ == "__main__":
    main()
