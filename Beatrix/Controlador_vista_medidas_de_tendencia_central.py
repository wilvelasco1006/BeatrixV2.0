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
    def calcular_la_media(self,todos_los_datos,frecuencia_de_apari,desicion,datos_para_evaluar):
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
        
        self.calcular_la_mediana(todos_los_datos,desicion,datos_para_evaluar,frecuencia_de_apari)
        
            
    def calcular_la_mediana(self,todos_los_datos,desicion,datos_para_evaluar,frecuencia_de_apari):
        
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
        
        self.calcular_la_moda(todos_los_datos,frecuencia_de_apari,datos_para_evaluar,desicion)
        
    
    def calcular_la_moda(self,todos_los_datos, frecuencia_de_apari,datos_a_evaluar,desicion):
        posicion_moda=0
        dato_mas_repetido=max(frecuencia_de_apari)
        nombre_correspondiente=""
        
        for i in range(len(frecuencia_de_apari)):
            if (dato_mas_repetido== frecuencia_de_apari[i]):
                posicion_moda=i

        nombre_correspondiente+= str(datos_a_evaluar[posicion_moda])
        
        moda= "La moda es "+nombre_correspondiente+" con "+str(dato_mas_repetido)+" repeticiones"
        
        self.unas_medidias_de_tendencia.set_moda(moda)
        
        self.calcular_el_cuartil_1(todos_los_datos,desicion)
          
    def calcular_el_cuartil_1(self,todos_los_datos,desicion):
        i=(0.25 * len(todos_los_datos))
        i_redondeado= round(i)
        cuartil_1= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
        
        self.unas_medidias_de_tendencia.set_cuartil_1(cuartil_1)
 
        self.calcular_el_cuartil_2(todos_los_datos,desicion)
        
        
    def calcular_el_cuartil_2(self,todos_los_datos,desicion):
        i=(0.5 * len(todos_los_datos))
        i_redondeado= round(i)
        cuartil_2= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
        
        self.unas_medidias_de_tendencia.set_cuartil_2(cuartil_2)

        self.calcular_el_cuartil_3(todos_los_datos,desicion)
        
        
    def calcular_el_cuartil_3(self,todos_los_datos,desicion):
        i=(0.75 * len(todos_los_datos))
        i_redondeado= round(i)
        cuartil_3= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
        
        self.unas_medidias_de_tendencia.set_cuartil_3(cuartil_3)

        self.calcular_el_cuartil_4(todos_los_datos,desicion)
        
        
    def calcular_el_cuartil_4(self,todos_los_datos,desicion):
        cuartil_4=max(todos_los_datos)

        self.unas_medidias_de_tendencia.set_cuartil_4(cuartil_4)