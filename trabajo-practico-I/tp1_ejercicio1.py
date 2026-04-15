#Materia: Algoritmos y Estructuras de Datos II
#Alumno: Brian Sabil
#TP1 | Ejercicio 1
#Fecha de entrega: 15/04/2026

#1_Definimos la clase base(creamos una clase Vehiculo con uin constructor donde pide marca, velocidad_max)
class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca #Guardamos la marca
        self.velocidad_max = velocidad_max #Guardamos la velocidad

    def describir(self):
        #aca debuelve un String el cual se imprimira en consola mostrando la marca del auto
        return "Este es un vehículo marca " + self.marca

#2_Creamos las Herencia la cual se le habran sido heredadas de Vehiculo(clase padre) y la cual usaran las clases hijas las cuales son Auto y Moto
class Auto(Vehiculo):
    def describir(self):
        #volvemos a poner un return para poder debolver un msj en consola mencionando el auto, marca, velocidad maxima
        return "Auto " + self.marca + ", alcanza los " + str(self.velocidad_max) + " km/h."

class Moto(Vehiculo):
    def describir(self):
      #aca es lo mismo que el auto pero en moto
        return "Moto " + self.marca + ", alcanza los " + str(self.velocidad_max) + " km/h."

#3_ Creamos una lista con los vewhiculos(objetos). donde aca asignamos Auto y Moto
mis_vehiculos = [Auto("Ford", 180), Moto("Honda", 120)]

# Recorremos la lista y mostramos la descripción (polimorfismo)
print("Lista de Vehiculos")
for vehi in mis_vehiculos:
    print(vehi.describir()) #aca llamamos a la funcion describir que es la que trabajaraen debolver el metodo string
