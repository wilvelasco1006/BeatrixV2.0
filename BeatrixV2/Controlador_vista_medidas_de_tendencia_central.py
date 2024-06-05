from Medidas_de_tendencia_central import Medidas_de_tendencia_central 
from Vista_medidas_de_tendencia_central import Vista_medidas_de_tendencia_central
from Controlador_vista_medidas_de_variabilidad import Controlador_vista_medidas_de_variabilidad
#from Vista_medidas_de_variabilidad import Vista_medidas_de_variabilidad

class Controlador_vista_medidas_de_tendencia_central:
    #Atributos
    unas_medidias_de_tendencia= Medidas_de_tendencia_central()#variable para crear un objeto medidas de tendencia central para rellenar y luego acceder a sus atributos
    una_vista_de_medidas_de_tendencia= Vista_medidas_de_tendencia_central()# objeto para mostrar las medidas de tendencia central
    unas_medidas_de_variabilidad= Controlador_vista_medidas_de_variabilidad()#variable para posteriormente tener un objeto de medidas de variabilidad para rellenar y luego acceder a sus atributos
    
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    #Se debe agregar la entrada de un dato de tipo booleano tipo desicion para cambiar la forma de sacar el promedio se se ingresan datos string
    def calcular_la_media(self,todos_los_datos,frecuencia_de_apari,datos_para_evaluar, grafico_seleccionado, nombre_archivo_final):
        
        self.unas_medidias_de_tendencia.set_nombre_archivo_final(nombre_archivo_final)# proceso para almacenar el nombre del archivo .txt en el que se almacenan todo los resultados del análisis
        
        self.unas_medidias_de_tendencia.set_grafico_seleccionado(grafico_seleccionado)# proceso para almacenar el número de la operación a realizar ingresado por el usuario
        
        suma=0
        
        for i in todos_los_datos: # ciclo para sumar todos los datos que se encuentran en la lista par evaluar
            suma+=i 
            
        promedio= (suma/len(todos_los_datos)) #proceso para calcular el promedio
        
        promedio_ajustado=round(promedio,2)#función para redondear el resultado del promedio a 2 decimales como máximo
        
        self.unas_medidias_de_tendencia.set_media(promedio_ajustado)
        
        self.calcular_la_mediana(todos_los_datos,datos_para_evaluar,frecuencia_de_apari)
        
            
    def calcular_la_mediana(self,todos_los_datos,datos_para_evaluar,frecuencia_de_apari):
        
        if ((len(todos_los_datos) % 2) == 0): #condicional para saber si la cantidad de elementos que contiene la lista a evaluar es par o impar
            
            #debido a que la cantidad de datos de la lista es par, se hará un promedio entre los 2 datos del medio
            mitad_redondeada= round((len(todos_los_datos)) /2)
            mediana=(((todos_los_datos[mitad_redondeada-1]) + (todos_los_datos[mitad_redondeada])))
            mediana/=2
            
        else:
            
            #debido a que la cantidad de datos de la lista es impar se elegirá ese valor  como mediana
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
            if (dato_mas_repetido== frecuencia_de_apari[i]): #proceso para definir el dato que más se repite en la lista de datos para evaluar
                posicion_moda=i

        nombre_correspondiente+= str(datos_a_evaluar[posicion_moda])
        
        moda= "La moda es "+nombre_correspondiente+" con "+str(dato_mas_repetido)+" repeticiones" # creación cadena de texto en donde se declara la moda junto con las repeticiones que justifican que sea la moda
        
        self.unas_medidias_de_tendencia.set_moda(moda)
        
        self.calcular_el_cuartil_1(todos_los_datos)
          
          
    def calcular_el_cuartil_1(self,todos_los_datos):
        
        i=(0.25 * len(todos_los_datos)) #proceso para definir el dato que se encuentra en la posición que representa el 25% de los datos
        i_redondeado= round(i)
        
        cuartil_1= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2 # proceso para sacar el promedio entre los 2 numeros que se encuentran en ese porcentaje
        self.unas_medidias_de_tendencia.set_cuartil_1(cuartil_1)
                   
        self.calcular_el_cuartil_2(todos_los_datos, cuartil_1)
        
        
    def calcular_el_cuartil_2(self,todos_los_datos,cuartil_1):

        i=(0.5 * len(todos_los_datos))#proceso para definir el dato que se encuentra en la posición que representa el 50% de los datos
        i_redondeado= round(i)
        
        cuartil_2= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2 # proceso para sacar el promedio entre los 2 numeros que se encuentran en ese porcentaje
        self.unas_medidias_de_tendencia.set_cuartil_2(cuartil_2)

        self.calcular_el_cuartil_3(todos_los_datos, cuartil_1,cuartil_2)
        
        
    def calcular_el_cuartil_3(self,todos_los_datos, cuartil_1,cuartil_2):

        i=(0.75 * len(todos_los_datos)) #proceso para definir el dato que se encuentra en la posición que representa el 75% de los datos
        i_redondeado= round(i)
        
        cuartil_3= (todos_los_datos[i_redondeado-1]+ todos_los_datos[i_redondeado])/2# proceso para sacar el promedio entre los 2 numeros que se encuentran en ese porcentaje
        self.unas_medidias_de_tendencia.set_cuartil_3(cuartil_3)
        
        self.calcular_el_cuartil_4(todos_los_datos, cuartil_1,cuartil_2,cuartil_3)
        
        
    def calcular_el_cuartil_4(self,todos_los_datos, cuartil_1,cuartil_2,cuartil_3):

        cuartil_4=max(todos_los_datos)#proceso para definir el dato que se encuentra en la posición que representa el 100% de los datos o el último dato de la lista
        self.unas_medidias_de_tendencia.set_cuartil_4(cuartil_4)

        self.llamado_para_mostrar_los_datos(todos_los_datos,cuartil_1,cuartil_3,cuartil_2)
        
        
    def llamado_para_mostrar_los_datos(self,todos_los_datos,cuartil_1,cuartil_3,cuartil_2):

        # variable que contiene una cadena de texto con las medidas de tendencia central acomodadas para mostrarlas
        datos= (self.unas_medidias_de_tendencia.acomodar_los_datos_para_mostrar()) 
        
        grafico_seleccionado= self.unas_medidias_de_tendencia.get_grafico_seleccionado() # variable que contiene el numero de la operación que ingresó el usario
        
        nombre_archivo_final=self.unas_medidias_de_tendencia.get_nombre_archivo_final()# variable que contendrá el nombre del archivo en el que se almacenaran los resultados del análisis proporcionado por el usuario
        
        
        if(grafico_seleccionado==2 or grafico_seleccionado ==12):# condicional para que se ejecute en el caso de que la opción elegida haya sido el 2 o el 12 (medidas de tendencia centarl o todas las tablas)
            
            self.una_vista_de_medidas_de_tendencia.mostrar_las_medidas_de_tendencia(datos,nombre_archivo_final) # metodo para mostrar las medidas de tendencia central
        
        
        if(grafico_seleccionado !=2):# condicional para que se ejecute en el caso de que la opción elegida haya sido cualquier número distinto al 2 (medidas de tendencia central)
            
            #variable para crear un objeto medidas de variabilidad para rellenar y luego acceder a sus atributos
            self.unas_medidas_de_variabilidad.calcular_el_rango(todos_los_datos,cuartil_1,cuartil_3,cuartil_2, grafico_seleccionado , nombre_archivo_final)
        
