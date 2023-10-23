import json 
from datetime import *
from clases import *

class notasCRUD:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def consultar_notas(self):
        return self.notas

    def guardar_json(self, archivo):
        dato = []
        obtener_estado = lambda nota: "Aprobado" if nota.estado else "Reprobado" #lambda para obtener estado

        for nota in self.notas:
            dato.append({
                "id": nota.id,
                "facultad": nota.facultad.nombre,
                "carrera": nota.carrera.nombre,
                "asignatura": nota.asignatura.nombre,
                "profesor": f"{nota.profesor.nombre} {nota.profesor.apellido}",
                "alumno": f"{nota.alumno.nombre} {nota.alumno.apellido}",
                "semestre": nota.semestre.descripcion,
                "paralelo": nota.semestre.paralelo,
                "seccion": nota.semestre.seccion,
                "fechaInicio": nota.semestre.fecha_inicio.strftime("%d/%m/%y"),
                "fechaFin": nota.semestre.fecha_fin.strftime("%d/%m/%y"),
                "nota1": nota.nota1,
                "nota2": nota.nota2,
                "examen1": nota.examen1,
                "parcial1": nota.parcial1,
                "nota3": nota.nota3,
                "nota4": nota.nota4,
                "examen2": nota.examen2,
                "parcial2": nota.parcial2,
                "nota_final": nota.nota_final,
                "estado": obtener_estado(nota)
            })

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(dato, file, indent=4, ensure_ascii=False)

    def cargar_json(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as file:
            dato = json.load(file)

        for item in dato:
            facultad = Facultad(item["facultad"])
            carrera = Carrera(item["carrera"])
            asignatura = Asignatura(item["asignatura"])

            split_name = lambda full_name: full_name.split(" ")  # lambda para dividir nombres
            nombre_profesor, apellido_profesor = split_name(item["profesor"])
            profesor = Profesor(nombre_profesor, apellido_profesor)
            nombre_alumno, apellido_alumno = split_name(item["alumno"])
            alumno = Alumno(nombre_alumno, apellido_alumno)

            semestre = Semestre(item["semestre"], "", "", "", "", "")
            nota1 = item["nota1"]
            nota2 = item["nota2"]
            examen1 = item["examen1"]
            parcial1 = item["parcial1"]
            nota3 = item["nota3"]
            nota4 = item["nota4"]
            examen2 = item["examen2"]
            parcial2 = item["parcial2"]
            nota_final = item["nota_final"]
            estado = item["estado"] == "Aprobado"

            nota = Notas(
                facultad,
                carrera,
                asignatura,
                profesor,
                alumno,
                semestre,
                nota1,
                nota2,
                examen1,
                parcial1,
                nota3,
                nota4,
                examen2,
                parcial2,
                nota_final,
                estado
            )
            self.agregar_nota(nota)

if __name__ == "__main__":
    notas_crud = notasCRUD()

    while True:
        print("Menú de Opciones:")
        print("1. Ingresar nueva nota")
        print("2. Consultar notas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            facultad_nombre = input("Facultad: ")
            carrera_nombre = input("Carrera: ")
            asignatura_nombre = input("Asignatura: ")
            profesor_nombre = input("Nombre del profesor: ")
            profesor_apellido = input("Apellido del profesor: ")
            alumno_nombre = input("Nombre del alumno: ")
            alumno_apellido = input("Apellido del alumno: ")
            semestre_descripcion = input("Descripción del semestre: ")
            semestre_paralelo = input("Paralelo: ")
            semestre_seccion = input("Sección: ")

            fecha_inicio_str = input("Fecha de inicio (dd/mm/yyyy): ")
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y").date()

            fecha_fin_str = input("Fecha de fin (dd/mm/yyyy): ")
            fecha_fin = datetime.strptime(fecha_fin_str, "%d/%m/%Y").date()

            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            examen1 = float(input("Examen 1: "))
            nota3 = float(input("Nota 3: "))
            nota4 = float(input("Nota 4: "))
            examen2 = float(input("Examen 2: "))

            facultad = Facultad(facultad_nombre)
            carrera = Carrera(carrera_nombre)
            asignatura = Asignatura(asignatura_nombre)
            profesor = Profesor(profesor_nombre, profesor_apellido)
            alumno = Alumno(alumno_nombre, alumno_apellido)
            semestre = Semestre(semestre_descripcion, semestre_paralelo, semestre_seccion, fecha_inicio, fecha_fin)

            nueva_nota = Notas(facultad, carrera, asignatura, profesor, alumno, semestre, nota1, nota2, examen1, 0, nota3, nota4, examen2, 0, 0, False)

            nueva_nota.calcular_notas()
            notas_crud.agregar_nota(nueva_nota)
            notas_crud.guardar_json('notas.json')  # Cargar archivo json
            print("Nota ingresada correctamente.")
        elif opcion == "2":
            notas = notas_crud.consultar_notas()
            for nota in notas:
                print(f"ID: {nota.id}")
                print(f"Facultad: {nota.facultad.nombre}")
                print(f"Carrera: {nota.carrera.nombre}")
                print(f"Asignatura: {nota.asignatura.nombre}")
                print(f"Profesor: {nota.profesor.nombre} {nota.profesor.apellido}")
                print(f"Alumno: {nota.alumno.nombre} {nota.alumno.apellido}")
                print(f"Semestre: {nota.semestre.descripcion}")
                print(f"Paralelo: {nota.semestre.paralelo}")
                print(f"Sección: {nota.semestre.seccion}")
                print(f"Fecha de Inicio: {nota.semestre.fecha_inicio.strftime('%d/%m/%y')}")
                print(f"Fecha de Fin: {nota.semestre.fecha_fin.strftime('%d/%m/%y')}")
                print(f"Nota1: {nota.nota1:.2f}")
                print(f"Nota2: {nota.nota2:.2f}")
                print(f"Examen1: {nota.examen1:.2f}")
                print(f"Parcial1: {nota.parcial1:.2f}")
                print(f"Nota3: {nota.nota3:.2f}")
                print(f"Nota4: {nota.nota4:.2f}")
                print(f"Examen2: {nota.examen2:.2f}")
                print(f"Parcial2: {nota.parcial2:.2f}")
                print(f"Nota Final: {nota.nota_final:.2f}")
                print(f"Estado: {'Aprobado' if nota.estado else 'Reprobado'}")
                print("\n")
        elif opcion == "3":
            print("Adios!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")







