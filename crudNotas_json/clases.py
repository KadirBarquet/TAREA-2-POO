from abc import ABC, abstractmethod 

class Carrera:
    def __init__(self, nombre):
        self.__id = id(self)
        self.nombre = nombre

class Facultad:
    def __init__(self, nombre):
        self.__id = id(self)
        self.nombre = nombre
        self.carreras = [] #composicion

    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

class Asignatura:
    def __init__(self, nombre):
        self.__id = id(self)
        self.nombre = nombre

class Persona(ABC):
    def __init__(self, nombre, apellido):
        self.__id = id(self)
        self.nombre = nombre
        self.apellido = apellido

    @property
    def id(self):
        return self.__id 
    
    @abstractmethod
    def mostrar(self):
        pass

class Profesor(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido) 

    def mostrar(self):
        print()
    
class Alumno(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido) 

    def mostrar(self):
        print()

class Semestre:
    def __init__(self, descripcion, paralelo, seccion, fecha_inicio, fecha_fin):
        self.__id = id(self)
        self.descripcion = descripcion
        self.paralelo = paralelo
        self.seccion = seccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Notas:
    def __init__(self, facultad, carrera, asignatura, profesor, alumno, semestre, nota1, nota2, examen1, parcial1, nota3, nota4, examen2, parcial2, nota_final, estado):
        self.__id = id(self)
        self.facultad = facultad
        self.carrera = carrera
        self.asignatura = asignatura
        self.profesor = profesor
        self.alumno = alumno
        self.semestre = semestre
        self.nota1 = nota1
        self.nota2 = nota2
        self.examen1 = examen1
        self.parcial1 = 0
        self.nota3 = nota3
        self.nota4 = nota4
        self.examen2 = examen2
        self.parcial2 = 0
        self.nota_final = 0
        self.estado = estado

    @property
    def id(self):
        return self.__id 
    
    def calcular_notas(self):
        # Funciones dentro de función para calcular los parciales
        def calcular_parcial1():
            return self.nota1 + self.nota2 + self.examen1

        def calcular_parcial2():
            return self.nota3 + self.nota4 + self.examen2

        self.parcial1 = calcular_parcial1()
        self.parcial2 = calcular_parcial2()
        self.nota_final = self.parcial1 + self.parcial2 
        self.determinar_estado = lambda: self.nota_final >= 70 #lambda para determinar estado 
        self.estado = self.determinar_estado()
    
    


