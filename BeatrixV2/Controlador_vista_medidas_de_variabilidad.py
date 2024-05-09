from Medidas_de_variabilidad import Medidas_de_variabilidad
from Vista_medidas_de_variabilidad import Vista_medidas_de_variabilidad
from Diagrama_de_caja import accion_9
class Controlador_vista_medidas_de_variabilidad:
    #atributos
    un_cuadro_de_variabilidad= Medidas_de_variabilidad()
    una_vista_medidas_de_variabilidad= Vista_medidas_de_variabilidad()
    un_diagrama_de_caja= accion_9()
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    #Metodo que me permite calcular el rango de los datos
    def calcular_el_rango(self,todos_los_datos, cuartil_1, cuartil_3,cuartil_2):
        rango= (max(todos_los_datos) - min(todos_los_datos))
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_todos_los_datos(todos_los_datos)
        self.un_cuadro_de_variabilidad.set_rango(rango)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_el_rango_intercuartico(todos_los_datos, cuartil_1, cuartil_3,cuartil_2)
        
    #metrodo que me permite calcular el rango intercuartico
    def calcular_el_rango_intercuartico(self, todos_los_datos,cuartil_1,cuartil_3,cuartil_2):
        rango_inter_cuartico= cuartil_3 - cuartil_1
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_rango_intercuartico(rango_inter_cuartico)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_la_media_muestral(todos_los_datos, cuartil_1, cuartil_3,cuartil_2)
        
    
    #metodo para calcular la media muestral
    def calcular_la_media_muestral(self, todos_los_datos, cuartil_1, cuartil_3,cuartil_2):
        sumatoria=0
        for i in todos_los_datos:
            sumatoria+=i
        
        #division de la sumatoria de el contenido de todos los datos ingresados con el tamaño del contenedor
        media_muestral= round(sumatoria/ len(todos_los_datos),2)
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_media_muestral(media_muestral)
        
        #llamado al siguiente metodo para continuar con el programa
        self.determinar_el_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(todos_los_datos,media_muestral, cuartil_1, cuartil_3,cuartil_2)
    
    
    #metodo que me permite determinar_el_cuadrado_de_la_desviacion_estandar_respecto_a_la_media
    def determinar_el_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(self,todos_los_datos, media_muestral, cuartil_1, cuartil_3,cuartil_2):
        cuadrado_desvi_estand_resp_media=list()

        #ciclo para sacar el_cuadrado_de_la_desviacion_estandar_respecto_a_la_media restando cada dato con la media muestral y luego elevandolos al cuadrado
        for i in range(len(todos_los_datos)):
            cuadrado_desvi_estand_resp_media.append(round((todos_los_datos[i] - media_muestral)**2,2))# los **2 significan elevar al cuadrado

        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_cuadrado_de_la_desviación_respecto_a_la_medida(cuadrado_desvi_estand_resp_media)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_la_suma_del_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(todos_los_datos,  cuadrado_desvi_estand_resp_media, cuartil_1, cuartil_3,cuartil_2)    
    
    
    #metodo para hacer la sumatoria total del_cuadrado_de_la_desviacion_estandar_respecto_a_la_media
    def calcular_la_suma_del_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(self, todos_los_datos, cuadrado_desvi_estand_resp_media, cuartil_1, cuartil_3,cuartil_2):
        sumatoria=0
        
        #ciclo para hacer la sumatoria consecutiva
        for i in cuadrado_desvi_estand_resp_media:
            sumatoria+=i
        
        sumatoria_redondeada=round(sumatoria,2)
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida(sumatoria_redondeada)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_la_varianza(todos_los_datos,sumatoria_redondeada, cuartil_1, cuartil_3,cuartil_2)
    
    
    #metodo para calcular la varianza, tanto poblacional como muestral
    def calcular_la_varianza(self, todos_los_datos, sum_cuadra_desvi_resp_media, cuartil_1, cuartil_3,cuartil_2):
        tipo_de_varianza=int(input("¿Que tipo de varianza desea que se emplee? 1.Poblacional  2.Muestral \n"))
        desicion_varianza=False
        
        #condicional para definirt tipo de varianza se empleará
        if (tipo_de_varianza==1):
            desicion_varianza=True
        
        else:
            desicion_varianza=False 
        
            
        #condicional para definir si la varianza será muestral o poblacional
        if(desicion_varianza==True):
            varianza= round(sum_cuadra_desvi_resp_media/len(todos_los_datos),2)
            
        else:
            varianza= round(sum_cuadra_desvi_resp_media/(len(todos_los_datos )- 1),2)
            
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_varianza(varianza)
        self.un_cuadro_de_variabilidad.set_poblacion_o_muestra(desicion_varianza)
        
         #llamado al siguiente metodo para continuar con el programa
        self.calcular_desviacion_estandar(varianza, desicion_varianza, cuartil_1, cuartil_3,cuartil_2)
        
    
    #metodo para calcular la desviacion estandar
    def calcular_desviacion_estandar(self, varianza, desicion_varianza, cuartil_1, cuartil_3,cuartil_2):
        desviacion_estandar= round(varianza ** 0.5,2) #sacar la raiz cuadrada de la varianza
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_desviacion_estandar(desviacion_estandar)
        
        #llamado al siguiente metodo para continuar con el programa
        self.definir_el_numero_menor_del_rango(desviacion_estandar, cuartil_1, cuartil_3,cuartil_2)
        
        
    #metodo para definir tanto el numero menor como el numero mayor del rango que se va a evaluar con el teorema de shevychev
    def definir_el_numero_menor_del_rango(self, desviacion_estandar, cuartil_1, cuartil_3,cuartil_2):
        num_menor_rango= float(input("Por favor ingrese el numero menor que desee que se analice con el teorema de chevyshev: "))
        
        num_mayor_rango= float(input("Por favor ingrese el numero mayor que desee que se analice con el teorema de chevyshev: "))
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_num_menor_rango(num_menor_rango)
        self.un_cuadro_de_variabilidad.set_num_mayor_rango(num_mayor_rango)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_puntos_z_interno(desviacion_estandar, num_menor_rango, num_mayor_rango, cuartil_1, cuartil_3,cuartil_2)
        
    
    #metodo para calcular puntos z que se usa solo para los datos que se van a evaluar en el teorema de chevyshev
    def calcular_puntos_z_interno(self, desviacion_estandar, num_menor_rango, num_mayor_rango, cuartil_1, cuartil_3,cuartil_2):
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()#Se obtiene la lista todos los datos tras usar el metodo get para pedirsela al objeto un)cuadro_de_varibilidad
        
        #me dice a cuantas desviaciones estandar se encuentra un numero de la media muestra
        desviacion_num_menor= round((num_menor_rango -media_muestral)/ desviacion_estandar,4)
        desviacion_num_mayor= round((num_mayor_rango - media_muestral)/ desviacion_estandar,4)

         #llamado al siguiente metodo para continuar con el programa
        self.calcular_el_porcentaje_segun_el_teorema_de_chevyshev(desviacion_estandar, desviacion_num_menor, desviacion_num_mayor, cuartil_1, cuartil_3,cuartil_2)
    
    
    #Metodo para calcular el porcentaje que abarca el rango determinado por el rango introducido anteriormente
    def calcular_el_porcentaje_segun_el_teorema_de_chevyshev(self, desviacion_estandar, desviaciones_num_menor, desviaciones_num_mayor, cuartil_1, cuartil_3,cuartil_2):
        
         #si la desviacion de los dos numeros es igual aprovecho para acortar un poco el codigo usando los datos de solo una variable
        if desviaciones_num_mayor == desviaciones_num_menor:
            porcentaje = (1 - (1 / (desviaciones_num_menor * 2)))
            porcentaje_real = round(porcentaje * 100, 2)
        else:
            # Asegura valores positivos para las desviaciones
            desviaciones_num_menor = abs(desviaciones_num_menor)
            desviaciones_num_mayor = abs(desviaciones_num_mayor)
        
            # Cálculo de k para las desviaciones simétricas de ambos datos
            k1 = abs(round(1 - (1 / desviaciones_num_menor ** 2), 4))
            k2 = abs(round(1 - (1 / desviaciones_num_mayor ** 2), 4))
            # Determina el k más grande y el más pequeño
            max_k = max(k1, k2)
            min_k = min(k1, k2)
        
            min_k=min_k
            max_k=max_k
            # Calcula el porcentaje parcial según Chevyshev
            porcentaje_parcial = max_k - ((max_k - min_k))
            porcentaje_real = round((porcentaje_parcial) * 100)

        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_porcentaje_chevyshev(porcentaje_real)
        
        #llamado al siguiente metodo para continuar con el programa
        self.puntos_z_requeridos(desviacion_estandar, cuartil_1, cuartil_3,cuartil_2)
    
    #metodo para calcular cuantas desviaciones estandar de la media muestral se encuantra algun dato que desee conocer el usuario
    def puntos_z_requeridos(self, desviacion_estandar, cuartil_1, cuartil_3,cuartil_2):
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()
        
        #pregunta para saber si desea saber los puntos z de un dato extra o no
        desea_puntos_z=int(input("\n¿Desea conocer a cuantas desviaciones estandar de la media muestral se encuentra algún numero en específico?  1.Si  2.No \n"))
        while(desea_puntos_z<1 or desea_puntos_z>2):
            desea_puntos_z=int(input("por favor elija una de las 2 opciones:  1.Si  2.No \n"))
        
        if(desea_puntos_z==1):
            numero= float(input("Por favor ingrese el numero el cual desee conocer a cuantas desviaciones estandar se encuentra de la media_muestral:  "))
            resultado_desicion= round((numero - media_muestral)/ desviacion_estandar,2)
            if (resultado_desicion<0):
                resultado_desicion*=-1
        
        #En el caso en que no se quiera saber los puntos z de otro dato en especifico saldrá un mensaje de no se ingresó ningún numero
        else:
            numero= "No se ingresó ningún numero"
            resultado_desicion= "No se ingresó ningún numero"
            
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_numero_puntos_z(numero)    
        self.un_cuadro_de_variabilidad.set_puntos_z(resultado_desicion)
        
        #llamado al siguiente metodo para continuar con el programa
        self.definir_media_y_desviaciones_estandar(desea_puntos_z,desviacion_estandar, cuartil_1, cuartil_3,cuartil_2)
    
    def definir_media_y_desviaciones_estandar(self,desea_puntos_z,desviacion_estandar, cuartil_1, cuartil_3,cuartil_2):
        tabla=[[]]
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()

        for i in range (3, 0, -1 ):
            tabla[0].append(str(round(media_muestral - (desviacion_estandar*i) , 1)))    
        
        for i in range(4):
            tabla[0].append(str(round(media_muestral + (desviacion_estandar*i), 1)))  
            
        self.un_cuadro_de_variabilidad.set_media_y_desviaciones_estandar(tabla)    
            
        self.preparar_para_mostrar_diagrama_de_caja(desea_puntos_z,tabla, cuartil_1, cuartil_3,cuartil_2)
        
    def preparar_para_mostrar_diagrama_de_caja(self,desea_puntos_z,tabla, cuartil_1, cuartil_3,cuartil_2):
        todos_los_datos= self.un_cuadro_de_variabilidad.get_todos_los_datos()
        rango_intercuartico=self.un_cuadro_de_variabilidad.get_rango_intercuartico()
        limite_inferior=round((cuartil_1- rango_intercuartico) , 1)
        limite_superior= round((cuartil_3 + rango_intercuartico) , 1)
        
        cuartil_1_redondeado=round(cuartil_1 , 1)
        
        lista=[[limite_inferior,cuartil_1_redondeado,cuartil_2,cuartil_3,limite_superior]]
        
        
        self.llamado_para_mostrar_los_datos(desea_puntos_z,tabla,lista)
        
    #metodo para enviarle los datos organizados a la vista para que los muestre allá
    def llamado_para_mostrar_los_datos(self,desea_puntos_z,tabla,lista):
        #obteniendo los datos ordenados en una sola variable
        medidas_de_variabilidad= self.un_cuadro_de_variabilidad.mostrar_los_datos_de_las_medidas_de_variabilidad(desea_puntos_z)
        
        #llamada a la vista
        self.una_vista_medidas_de_variabilidad.mostrar_las_medidas_de_variabilidad(medidas_de_variabilidad,tabla)
        self.un_diagrama_de_caja.dibujar(lista)
        