class persona:

    # metodo constructor de la clase 

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # metodo para mostrar la informacion de la persona
    def mostarpersonas(self):
        print("nombre: ", self.nombre)
        print("apellidos: ", self.apellidos)
        print("edad: ", self.edad)

class persona:

    # metodo constructor de la clase 

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # metodo para mostrar la informacion de la persona
    def mostarpersonas(self):
        print("nombre: ", self.nombre)
        print("apellidos: ", self.apellido)
        print("edad: ", self.edad)

def main():
    print("vamos a prender POO...")
    persona_1 = persona("lorenzo", "perez", 18)
    persona_1.mostarpersonas()

if __name__ == main():
    main()