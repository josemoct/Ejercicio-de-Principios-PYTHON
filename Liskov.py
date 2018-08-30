class Animal(object):
        def __init__(self,nombre):
                self.nombre=nombre

        def descripcion():
                pass

class Perro(Animal):
        def __init__(self,nombre,raza):
                super(Perro,self).__init__(nombre)
                self.raza=raza
                
        def descripcion(self):
                print'Perro:',self.nombre,'\nRaza:',self.raza
                print'El perro camina con 4 patas"'


perro=Perro("Wachu","Doberman")
perro.descripcion()
