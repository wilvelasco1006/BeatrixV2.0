from Controlador_vista_seleccion_tipo_cuadro_de_frecuencias import Controlador_vista_seleccion_tipo_cuadro_de_frecuencias

class Vista_seleccion_tipo_cuadro_de_frecuencias:
    #Atributos
    
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass 
    
    def vista_seleccion_tipo_de_datos_a_ingresar(self):
        controlador= Controlador_vista_seleccion_tipo_cuadro_de_frecuencias()
        opcion= int(input("Bienvenido a la sección para crear una tabla de frecuencias\n\n"
                          "Por favor ingrese una opción:\n"
                          "1. Ingresar datos para analisis individual"
                          "\n2. Ingresar datos para analizarlos en intérvalos\n\n"))

        controlador.redireccionamiento_segun_seleccion(opcion)
        
        
