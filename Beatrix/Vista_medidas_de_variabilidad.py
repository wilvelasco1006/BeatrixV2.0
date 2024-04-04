from Teorema_chevyshev import accion_8

class Vista_medidas_de_variabilidad:
    #atributos
    un_teorema_de_chevyshev=accion_8()
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    def mostrar_las_medidas_de_variabilidad(self,medidas_de_variabilidad,tabla):
        print("\n"+medidas_de_variabilidad)
        
        self.mostrar_el_diagrama_de_chevyshev(tabla)
        
    def mostrar_el_diagrama_de_chevyshev(self,tabla):
        print(tabla)
        self.un_teorema_de_chevyshev.dibujar(tabla)