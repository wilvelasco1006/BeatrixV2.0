from  Controlador_vista_cuadro_de_frecuencias  import Controlador_vista_cuadro_de_frecuencias
from Controlador_vista_cuadro_de_frecuencias_intervalos import Controlador_vista_cuadro_de_frecuencias_intervalos

class Controlador_vista_seleccion_tipo_cuadro_de_frecuencias:
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    def redireccionamiento_segun_seleccion(self, opcion: int):
        controlador_cuadro_de_frecuencias_datos_individuales= Controlador_vista_cuadro_de_frecuencias()
        controlador_cuadro_de_frecuencias_intervalos= Controlador_vista_cuadro_de_frecuencias_intervalos()
        
        if opcion== 1:
            controlador_cuadro_de_frecuencias_datos_individuales()
        
        elif opcion == 2:
            controlador_cuadro_de_frecuencias_intervalos()
        
        else:
            print("Se ha introducido un numero distinto a 1 y 2 ")