from Medidas_de_tendencia_central import Medidas_de_tendencia_central 
from Vista_medidas_de_tendencia_central import Vista_medidas_de_tendencia_central

class Controlador_vista_medidas_de_tendencia_central:
    #Atributos
    unas_medidias_de_tendencia= Medidas_de_tendencia_central()
    una_vista_de_medidas_de_tendencia= Vista_medidas_de_tendencia_central()
    
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    #Se debe agregar la entrada de un dato de tipo booleano tipo desicion para cambiar la forma de sacar el promedio se se ingresan datos string
    def calcular_la_media(self,todos_los_datos,frecuencia_de_apari,desicion):
        suma=0
        if (desicion==1):
            desicion=True
        else:
            desicion=False
        
        if(desicion==False): #False=datos de tipo String
            for i in frecuencia_de_apari:
                suma+=i
                promedio= (suma/len(frecuencia_de_apari))
        else:
            for i in todos_los_datos:
                suma+=i
            promedio= (suma/len(todos_los_datos))
        
        promedio_ajustado=round(promedio,2)
        
        self.unas_medidias_de_tendencia.set_media(promedio_ajustado)
        
        self.calcular_la_mediana(todos_los_datos,desicion)
        
            
    def calcular_la_mediana(self,todos_los_datos,desicion):
        
        if ((len(todos_los_datos) % 2) == 0):
            
            if(desicion==True):
                mitad_redondeada= round((len(todos_los_datos)) /2)
                mediana=(((todos_los_datos[mitad_redondeada-1]) + (todos_los_datos[mitad_redondeada])))
                mediana/=2
                
            else:
                mitad= ((len(todos_los_datos)) /2)
                mitad_redondeada=round(mitad)
                mediana= str(todos_los_datos[mitad_redondeada-1]) + " y " + str(todos_los_datos[mitad_redondeada])
        
        else:
            mitad= ((len(todos_los_datos)) /2)
            mitad_redondeada=(round(mitad))
            if (mitad>=mitad_redondeada):
                mitad_redondeada+=1
            mediana=(todos_los_datos[mitad_redondeada-1])
        
        self.unas_medidias_de_tendencia.set_mediana(mediana)
            
    