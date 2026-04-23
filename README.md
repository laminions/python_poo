# POO en python
introduccion o programacion orientada a Objetos (POO) en python

## ¿por que aprender POO?

- imagina que quieres creear un videojuego. tienen gerreros, magos, dragones... cada uno con sus  propios puntos de vida, ataques y habilidades. ¿como los organizo en codigo sin repetir todo una y la otra vez?

- la **programacion orientada a objetos (POO)** es la respuesta. en lugar de escribir instrucciones sueltas, modelas el mundo real con *objetos* que tienen caracteristicas y comportamientos. es la forma en que estan construidos la mayoria de los propramas profesionales del mundo.

![POO](img/POO.png)

## clase y objeto

- una clase es un tipo de dato cuyas variables se llaman objetos o instancias.

- la clase es la definicion del concepto del mundo real y los objetos o instancias son el propio "objeto" del mundo real.

- las clases estan compuestas por dos elementos:
     -  ***Atributos:** informacion que alamecena la clase.
     - ** Metodos:** operaciones que pueden realizarse con la clase.

## definicion de una clase de python

```python
class nombreclase:

    def__init__(self, variable1, variable2):
        self.atributo1 = valor1
        self.atributo2 = valor2

        def nombremetodo(self):
            bloquecodigo
```

- `class` :palabra reservada en python para defnir una clase.
- `nombreclase` : nombre de la clase que se quiere crear.
- `def` : palabra reserevada en python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene.
- `__init__`: palabra reservada en python para definir el metodo constructor de la clase. el metodo `__init__` es lo primero que se ejecuta cuando creas un objeto de una clase.
- `(self, variableX)`: parametro del constructor de la clase. el parametro `self` es obligatorio y despues tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.
- `self.AtributoX`: forma de utilizacion y ecceso a los atributos de la clase.
- `nombremetodo`: nombre del metodo de la clase.
-`self`: parametro del metodo. el parametro `self` es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.
- `bloquecodigo` : instrucciones que ejecutara el metodo.

** Al defenir una clase tenga en cuenta:**
- puedes definir tantos atributos como necesidades
- puedes definir tantos metodos como necesites 
- puedes definir tanto parametros en el constructor y en los metodos como necesites.

## ejemplo 1

- crear una clase que represente una persona.
- atributos: nombre, apellidos y edad.
- metodos: mostrar la informacion de la persona.

###  codigo

``` python
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

def main():
    print("vamos a prender POO...")
    persona_1 = persona("lorenzo", "perez", 18)
    persona_1.mostrarpersona

if __name__ == main():
    main()
```


