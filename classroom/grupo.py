

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self.grado = "Grado 12"

    def listadoAsignaturas(self, **kwargs):
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):
        if(self.listadoAlumnos is None):
            self.listadoAlumnos = []
        if(lista is None):
            lista = [alumno]
        else:
            lista.append(alumno)

        self.listadoAlumnos = self.listadoAlumnos + lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    '''@ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre'''

    def __str__(self):
        cadena = "Grupo de estudiantes: "+self._grupo
        return cadena