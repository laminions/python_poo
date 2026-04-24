class persona:

    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(persona):
    pass

# metodo principal
def main():
## alumno
    alumno = Alumno()
    alumno.setNombre("heidy vanesa")
    alumno.setApellidos("acosta")
    alumno.setEdad(15)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas([ "Tecnología"])
    alumno.mostrarAlumno()
## profesor
def main():
    Profesor = Profesor()
    Profesor.setNombre("neztor")
    Profesor.setApellidos("paez")
    Profesor.setEdad(25)
    Profesor.setCurso("Bachillerato")
    Profesor.setAsignaturas([ "Tecnología", "matematica", "ingles"])
    Profesor.mostrarprofesor()

if __name__ == "__main__":
    main()