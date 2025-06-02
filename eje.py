class Escuela:
    def __init__(self):
        # Inicializar las listas para almacenar alumnos y profesores
        self.alumnos = []
        self.profesores = []
        # Diccionario con cursos predefinidos (código: nombre)
        self.cursos = {
            'C001': 'Matemáticas',
            'C002': 'Ciencias',
            'C003': 'Historia',
            'C004': 'Literatura',
            'C005': 'Inglés'
        }
    
    def agregar_alumno(self):
        # Solicitar datos del alumno
        nombre = input("Ingrese el nombre del alumno: ")
        cedula = input("Ingrese la cédula del alumno: ")
        materia = input("Ingrese la materia: ")
        nota = float(input("Ingrese la nota: "))
        
        # Validar que la materia ingresada exista en cursos predefinidos
        if materia not in self.cursos.values():
            print("Error: La materia no existe.")
            return
        
        # Agregar el alumno a la lista de alumnos
        self.alumnos.append({'nombre': nombre, 'cedula': cedula, 'materia': materia, 'nota': nota})
        print("Alumno agregado exitosamente.")
    
    def consultar_alumnos(self):
        # Verificar si hay alumnos registrados
        if not self.alumnos:
            print("No hay alumnos registrados.")
            return
        
        # Mostrar la lista de alumnos con sus datos
        print("\nLista de Alumnos:")
        for alumno in self.alumnos:
            print(f"Nombre: {alumno['nombre']}, Cédula: {alumno['cedula']}, Materia: {alumno['materia']}, Nota: {alumno['nota']}")
    
    def agregar_profesor(self):
        # Solicitar datos del profesor
        nombre = input("Ingrese el nombre del profesor: ")
        cedula = input("Ingrese la cédula del profesor: ")
        curso = input("Ingrese el curso: ")
        
        # Validar que el curso exista en los cursos predefinidos por código
        if curso not in self.cursos.keys():
            print("Error: El curso no existe.")
            return
        
        # Agregar el profesor a la lista de profesores
        self.profesores.append({'nombre': nombre, 'cedula': cedula, 'curso': curso})
        print("Profesor agregado exitosamente.")
    
    def consultar_profesores(self):
        # Verificar si hay profesores registrados
        if not self.profesores:
            print("No hay profesores registrados.")
            return
        
        # Mostrar lista de profesores con sus datos
        print("\nLista de Profesores:")
        for profesor in self.profesores:
            print(f"Nombre: {profesor['nombre']}, Cédula: {profesor['cedula']}, Curso: {profesor['curso']}")
    
    def generar_reporte(self):
        # Verificar si hay alumnos para generar reporte
        if not self.alumnos:
            print("No hay alumnos registrados.")
            return
        
        # Calcular total de alumnos
        total_alumnos = len(self.alumnos)
        # Calcular promedio de notas
        promedio = sum(alumno['nota'] for alumno in self.alumnos) / total_alumnos
        # Contar alumnos aprobados (nota >= 70)
        aprobados = sum(1 for alumno in self.alumnos if alumno['nota'] >= 70)
        # Contar alumnos reprobados (nota < 60)
        reprobados = sum(1 for alumno in self.alumnos if alumno['nota'] < 60)
        # Contar alumnos aplazados (60 <= nota < 70)
        aplazados = sum(1 for alumno in self.alumnos if 60 <= alumno['nota'] < 70)
        # Contar alumnos con nota superior al promedio
        superiores_al_promedio = sum(1 for alumno in self.alumnos if alumno['nota'] > promedio)

        # Imprimir reporte con resultados
        print("\nReporte de Alumnos:")
        print(f"Total de Alumnos: {total_alumnos}")
        print(f"Promedio de Notas: {promedio:.2f}")
        print(f"Alumnos Aprobados: {aprobados}")
        print(f"Alumnos Reprobados: {reprobados}")
        print(f"Alumnos Aplazados: {aplazados}")
        print(f"Alumnos con Nota Superior al Promedio: {superiores_al_promedio}")

def main():
    escuela = Escuela()
    
    while True:
        # Mostrar menú principal
        print ("\nBIENVENIDO A LA ESCUELA REPUBLICA DE COREA")
        print("Menú Principal:")
        print("1. Agregar o Consultar Alumnos")
        print("2. Agregar o Consultar Profesores")
        print("3. Generar Reporte")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Submenú para alumnos
            print("a. Agregar Alumno")
            print("b. Consultar Alumnos")
            subopcion = input("Seleccione una subopción: ")
            if subopcion == 'a':
                escuela.agregar_alumno()  # Llamar función para agregar alumno
            elif subopcion == 'b':
                escuela.consultar_alumnos()  # Llamar función para mostrar alumnos
            else:
                print("Opción no válida.")
        
        elif opcion == '2':
            # Submenú para profesores
            print("a. Agregar Profesor")
            print("b. Consultar Profesores")
            subopcion = input("Seleccione una subopción: ")
            if subopcion == 'a':
                escuela.agregar_profesor()  # Agregar profesor
            elif subopcion == 'b':
                escuela.consultar_profesores()  # Consultar profesores
            else:
                print("Opción no válida.")
        
        elif opcion == '3':
            escuela.generar_reporte()  # Generar y mostrar reporte
        
        elif opcion == '4':
            print("Saliendo del programa.")  # Salir del programa
            break
        
        else:
            print("Opción no válida.")  # Opción inválida en menú principal

if __name__ == "__main__":
    main()  # Ejecutar función principal
