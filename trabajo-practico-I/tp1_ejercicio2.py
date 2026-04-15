#Materia: Algoritmos y Estructuras de Datos II
#Alumno: Brian Sabil
#TP1 | Ejercicio 2
#Fecha de entrega: 15/04/2026

#color+area+descripcion
#1_Creamos la clase base que se llama Figura, Pide un color y el area por defecto es 0
class Figura:
    def __init__(self, color):
        self.color = color #Guardamos el color que nos pasen

    def area(self):
        #Aca por ahora debolvemos 0 porque es una figura general
        return 0

    def describir(self):
        #Este metodo muestra el color y el area. Aca se ve el polimorfismo
        print("figura de color " + self.color + " y el area es: " + str(self.area())) #como es un valor numerico, usamos el str para convertirlo en string



#Rectangulo
#2_Creamos las subclases Rectangulo y Circulo que heredan de Figura
class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color) #Le pasamos el color a la clase padre, para llamarlo usamos super()
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura #calculamos el area base X altura



#Circulo
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        #Usamos la formula del circulo (pi * r al cuadrado). Uso 3.14 para que sea simple
        return 3.14 * (self.radio ** 2)




#3_Hacemos la lista de las figuras
mis_figuras = [Rectangulo("Rojo", 10, 5), Circulo("Azul", 7),Rectangulo("Verde", 4, 2)]

#Recorremos la lista y llamamos al metodo describir de cada uno
print("figuras Calculadas")
for figu in mis_figuras:
    figu.describir() #Aca cada figura usa su propia formula de area y el color
