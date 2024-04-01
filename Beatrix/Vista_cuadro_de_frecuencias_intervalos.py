
class Vista_cuadro_de_frecuencias_intervalos:
    #Atributos

    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    def mostrar_la_tabla_de_frecuencias(self, tabla, desicion):
        if (desicion==True):
            print ("| Intervalos |    F    |   Fr   |   FrA  |   F%   |   F%A   |   F°  |")
            
        else:
            print ("|   Intervalos   |   F   |   Fr   |    FrA  |   F%   |    F%A  |   F°  |")
        
        print(tabla)
        
        
    
            