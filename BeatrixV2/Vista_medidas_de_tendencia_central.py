
class Vista_medidas_de_tendencia_central:
    #Atributos
    
    #metodos
    #meotodo constructor
    def __init__(self):
        pass
    
    def mostrar_las_medidas_de_tendencia(self,datos,nombre_archivo_final):
        print("\n"+datos)
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:# proceso para guardar las medidas de tendencia central en el archivo .txt que almacena los resultados
            f.write( "\n\nMedidas de tendencia central\n\n"+datos + '\n')