contactos = {
    "Ana López": "0991234567",
    "Carlos Pérez": "0987654321"
}

def mostrar_menu():
    print("\n--- GESTOR DE CONTACTOS ---")
    print("1. Mostrar todos los contactos")
    print("2. Agregar o actualizar un contacto")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

def mostrar_contactos():
    """Recorre la colección y muestra la información de forma clara."""
    if not contactos:
        print("\nLa lista de contactos está vacía.")
    else:
        print("\n=== LISTA DE CONTACTOS ===")
        for nombre, telefono in contactos.items():
            print(f"- Nombre: {nombre} | Teléfono: {telefono}")

def agregar_contacto():
    """Permite insertar nuevos datos a la colección."""
    nombre = input("\nIngrese el nombre del contacto: ").strip()
    telefono = input("Ingrese el número telefónico: ").strip()
    
    contactos[nombre] = telefono
    print(f"✅ Contacto '{nombre}' guardado exitosamente.")

def buscar_contacto():
    """Operación adicional: Búsqueda en la colección."""
    nombre = input("\nIngrese el nombre a buscar: ").strip()
    if nombre in contactos:
        print(f"🔍 Encontrado: {nombre} -> Teléfono: {contactos[nombre]}")
    else:
        print(f"❌ El contacto '{nombre}' no se encuentra registrado.")

def eliminar_contacto():
    """Operación adicional: Eliminación de datos."""
    nombre = input("\nIngrese el nombre del contacto a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print(f"🗑️ Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"❌ No se encontró el contacto '{nombre}'.")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            mostrar_contactos()
        elif opcion == "2":
            agregar_contacto()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("\n¡Gracias por usar el Gestor de Contactos! Hasta luego.")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if _name_ == "_main_":
    ejecutar()