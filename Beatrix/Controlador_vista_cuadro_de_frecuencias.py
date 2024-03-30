from Cuadro_de_frecuencias import Cuadro_de_frecuencias_datos_individuales as cuadro_de_frecuencias

class Controlador_vista_cuadro_de_frecuencias:
    #Atributos
    un_cuadro_de_frecuencias= cuadro_de_frecuencias()
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    def ingresar_y_almacenar_todos_los_datos(self):
        continuar= 1
        todos_los_datos= list()
        
        while(continuar== 1):
            dato=input("Por favor ingrese los datos que desee analizar:  ")
            todos_los_datos.append(dato)
            continuar= int(input("Desea agregar otro dato? 1.Si  2.No\n\n"))
            
        print( todos_los_datos)

