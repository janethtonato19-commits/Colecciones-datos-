estudiantes = {
    "Ana": 8.5,
    "Carlos": 9.0
}

# 2. Agregar un nuevo estudiante y su nota
print("--- AGREGAR NUEVO ESTUDIANTE ---")
nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota del estudiante: "))

estudiantes[nombre] = nota
print("Estudiante registrado con éxito.")

# 3. Mostrar todos los estudiantes registrados
print("\n--- LISTA DE ESTUDIANTES Y NOTAS ---")
for nombre, nota in estudiantes.items():
    print(nombre, ":", nota)

# 4. Operación adicional: Buscar la nota de un estudiante
print("\n--- BUSCAR NOTA DE ESTUDIANTE ---")
buscar = input("Ingrese el nombre del estudiante que desea buscar: ")

if buscar in estudiantes:
    print("La nota de", buscar, "es:", estudiantes[buscar])
else:
    print("El estudiante no se encuentra en el registro.")