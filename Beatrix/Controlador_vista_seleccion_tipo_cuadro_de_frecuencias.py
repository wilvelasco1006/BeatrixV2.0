from  Controlador_vista_cuadro_de_frecuencias  import Controlador_vista_cuadro_de_frecuencias
from Controlador_vista_cuadro_de_frecuencias_intervalos import Controlador_vista_cuadro_de_frecuencias_intervalos

class Controlador_vista_seleccion_tipo_cuadro_de_frecuencias:
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    def redireccionamiento_segun_seleccion(self, opcion: int):
        cuadro_de_frecuencia_dat_individuales= Controlador_vista_cuadro_de_frecuencias()
        cuadro_de_frecuencia_intervalos= Controlador_vista_cuadro_de_frecuencias_intervalos()
        
        if opcion== 1:
            cuadro_de_frecuencia_dat_individuales.ingresar_y_almacenar_todos_los_datos()
        
        elif opcion == 2:
            cuadro_de_frecuencia_intervalos.ingresar_y_almacenar_todos_los_datos()
        
        else:
            print("Se ha introducido un numero distinto a 1 y 2 ")