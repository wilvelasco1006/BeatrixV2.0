from Teorema_chevyshev import accion_8

from Teorema_chevyshev_para_txt import Teorema_chevyshev_para_txt

class Vista_medidas_de_variabilidad:
    #atributos
    un_teorema_de_chevyshev=accion_8()
    un_teorema_de_chevyshev_para_txt= Teorema_chevyshev_para_txt()
    
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    def mostrar_las_medidas_de_variabilidad(self,medidas_de_variabilidad,tabla,nombre_archivo_final):
        print("\n"+medidas_de_variabilidad)
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write  ("\n"+medidas_de_variabilidad+"\n")  
        
        self.un_teorema_de_chevyshev.dibujar(tabla)
        
        self.un_teorema_de_chevyshev_para_txt.dibujar(tabla,nombre_archivo_final)
        
        