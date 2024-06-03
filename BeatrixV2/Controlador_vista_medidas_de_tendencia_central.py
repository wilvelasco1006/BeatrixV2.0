from Medidas_de_tendencia_central import Medidas_de_tendencia_central 
from Vista_medidas_de_tendencia_central import Vista_medidas_de_tendencia_central
from Controlador_vista_medidas_de_variabilidad import Controlador_vista_medidas_de_variabilidad
#from Vista_medidas_de_variabilidad import Vista_medidas_de_variabilidad

class Controlador_vista_medidas_de_tendencia_central:
    #Atributos
    unas_medidias_de_tendencia= Medidas_de_tendencia_central()
    una_vista_de_medidas_de_tendencia= Vista_medidas_de_tendencia_central()
    unas_medidas_de_variabilidad= Controlador_vista_medidas_de_variabilidad()
    #una_vista_de_medidas_variabilidad=Vista_medidas_de_variabilidad()
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    #Se debe agregar la entrada de un dato de tipo booleano tipo desicion para cambiar la forma de sacar el promedio se se ingresan datos string
    def calcular_la_media(self,todos_los_datos,frecuencia_de_apari,datos_para_evaluar, grafico_seleccionado):
        
        self.unas_medidias_de_tendencia.set_grafico_seleccionado(grafico_seleccionado)
        suma=0
        
        for i in todos_los_datos:
            suma+=i
            
        promedio= (suma/len(todos_los_datos))
        
        promedio_ajustado=round(promedio,2)#estaba en ,2
        
        self.unas_medidias_de_tendencia.set_media(promedio_ajustado)
        
        self.calcular_la_mediana(todos_los_datos,datos_para_evaluar,frecuencia_de_apari)
        
            
    def calcular_la_mediana(self,todos_los_datos,datos_para_evaluar,frecuencia_de_apari):
        
        if ((len(todos_los_datos) % 2) == 0):
            
            mitad_redondeada= round((len(todos_los_datos)) /2)
            mediana=(((todos_los_datos[mitad_redondeada-1]) + (todos_los_datos[mitad_redondeada])))
            mediana/=2
            
        else:
            mitad= ((len(todos_los_datos)) /2)
            mitad_redondeada=(round(mitad))
            
            if (mitad>=mitad_redondeada):
                mitad_redondeada+=1
            mediana=(todos_los_datos[mitad_redondeada-1])
        
        self.unas_medidias_de_tendencia.set_mediana(mediana)
        
        self.calcular_la_moda(todos_los_datos,frecuencia_de_apari,datos_para_evaluar)
        
    
    def calcular_la_moda(self,todos_los_datos, frecuencia_de_apari,datos_a_evaluar):
        posicion_moda=0
        dato_mas_repetido=max(frecuencia_de_apari)
        nombre_correspondiente=""
        
        for i in range(len(frecuencia_de_apari)):
            if (dato_mas_repetido== frecuencia_de_apari[i]):
                posicion_moda=i

        nombre_correspondiente+= str(datos_a_evaluar[posicion_moda])
        
        moda= "La moda es "+nombre_correspondiente+" con "+str(dato_mas_repetido)+" repeticiones"
        
        self.unas_medidias_de_tendencia.set_moda(moda)
        
        self.calcular_el_cuartil_1(todos_los_datos)
          
          
    def calcular_el_cuartil_1(self,todos_los_datos):
        i=(0.25 * len(todos_los_datos))
        i_redondeado= round(i)
        cuartil_1= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
        self.unas_medidias_de_tendencia.set_cuartil_1(cuartil_1)
                   
        self.calcular_el_cuartil_2(todos_los_datos, cuartil_1)
        
        
    def calcular_el_cuartil_2(self,todos_los_datos,cuartil_1):

        i=(0.5 * len(todos_los_datos))
        i_redondeado= round(i)
        cuartil_2= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
        self.unas_medidias_de_tendencia.set_cuartil_2(cuartil_2)

        self.calcular_el_cuartil_3(todos_los_datos, cuartil_1,cuartil_2)
        
        
    def calcular_el_cuartil_3(self,todos_los_datos, cuartil_1,cuartil_2):

        i=(0.75 * len(todos_los_datos))
        i_redondeado= round(i)
        cuartil_3= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
        self.unas_medidias_de_tendencia.set_cuartil_3(cuartil_3)
        
        self.calcular_el_cuartil_4(todos_los_datos, cuartil_1,cuartil_2,cuartil_3)
        
        
    def calcular_el_cuartil_4(self,todos_los_datos, cuartil_1,cuartil_2,cuartil_3):

        cuartil_4=max(todos_los_datos)
        self.unas_medidias_de_tendencia.set_cuartil_4(cuartil_4)

        self.calcular_el_percentil_requerido(todos_los_datos,cuartil_1,cuartil_2,cuartil_3)

    def calcular_el_percentil_requerido(self, todos_los_datos,cuartil_1,cuartil_2,cuartil_3):
        peticion=int(input("Desea conocer la ubicación de algún dato con base a su porcentaje?: 1.Si  2.No\n: "))
        if(peticion==1):
            necesita_percentil=True
        else:
            necesita_percentil=False
        
        if(necesita_percentil==True):
            
            porcentaje= float(input("Por favor ingrese el porcentaje del dato a encontrar: "))
            while(porcentaje<1 or porcentaje>100):
                porcentaje= float(input("Por favor ingrese un numero entre el 1 y el 100: "))
            i=(porcentaje/100)*len(todos_los_datos)
            i_redondeado= round(i)
            percentil= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2
            if(porcentaje==100):
                percentil=max(todos_los_datos)
                
            elif (porcentaje==1):
                percentil=min(todos_los_datos)
                
        
        else:
            percentil="No se ingresó ningun percentil"
            
        self.unas_medidias_de_tendencia.set_resultado_percentil(percentil)
        
        self.llamado_para_mostrar_los_datos(todos_los_datos,cuartil_1,cuartil_3,cuartil_2)
        
        
    def llamado_para_mostrar_los_datos(self,todos_los_datos,cuartil_1,cuartil_3,cuartil_2):

        datos= (self.unas_medidias_de_tendencia.acomodar_los_datos_para_mostrar())
        if(self.unas_medidias_de_tendencia.get_grafico_seleccionado()==2 or self.unas_medidias_de_tendencia.get_grafico_seleccionado() ==12):
            self.una_vista_de_medidas_de_tendencia.mostrar_las_medidas_de_tendencia(datos)
        
        if(self.unas_medidias_de_tendencia.get_grafico_seleccionado() !=2):
        
            self.unas_medidas_de_variabilidad.calcular_el_rango(todos_los_datos,cuartil_1,cuartil_3,cuartil_2, self.unas_medidias_de_tendencia.get_grafico_seleccionado())
        
