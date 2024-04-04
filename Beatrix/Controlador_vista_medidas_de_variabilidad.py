from Medidas_de_variabilidad import Medidas_de_variabilidad
from Vista_medidas_de_variabilidad import Vista_medidas_de_variabilidad

class Controlador_vista_medidas_de_variabilidad:
    #atributos
    un_cuadro_de_variabilidad= Medidas_de_variabilidad()
    una_vista_medidas_de_variabilidad= Vista_medidas_de_variabilidad()
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    def calcular_el_rango(self,todos_los_datos, cuartil_1, cuartil_3):
        rango= (max(todos_los_datos) - min(todos_los_datos))
        
        self.un_cuadro_de_variabilidad.set_todos_los_datos(todos_los_datos)
        self.un_cuadro_de_variabilidad.set_rango(rango)
        
        self.calcular_el_rango_intercuartico(todos_los_datos, cuartil_1, cuartil_3)
        
    def calcular_el_rango_intercuartico(self, todos_los_datos,cuartil_1,cuartil_3):
        rango_inter_cuartico= cuartil_3 - cuartil_1
        
        self.un_cuadro_de_variabilidad.set_rango_intercuartico(rango_inter_cuartico)
        
        self.calcular_la_media_muestral(todos_los_datos)
        
    
    def calcular_la_media_muestral(self, todos_los_datos):
        sumatoria=0
        for i in todos_los_datos:
            sumatoria+=i
        
        media_muestral= round(sumatoria/ len(todos_los_datos),2)
        
        self.un_cuadro_de_variabilidad.set_media_muestral(media_muestral)
        
        self.determinar_el_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(todos_los_datos,media_muestral)
    
    
    def determinar_el_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(self,todos_los_datos, media_muestral):
        cuadrado_desvi_estand_resp_media=list()

        
        for i in range(len(todos_los_datos)):
            cuadrado_desvi_estand_resp_media.append(round((todos_los_datos[i] - media_muestral)**2,2))
            
        self.un_cuadro_de_variabilidad.set_cuadrado_de_la_desviación_respecto_a_la_medida(cuadrado_desvi_estand_resp_media)
        
        self.calcular_la_suma_del_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(todos_los_datos,  cuadrado_desvi_estand_resp_media)    
    
    
    def calcular_la_suma_del_cuadrado_de_la_desviacion_estandar_respecto_a_la_media(self, todos_los_datos, cuadrado_desvi_estand_resp_media):
        sumatoria=0
        
        for i in cuadrado_desvi_estand_resp_media:
            sumatoria+=i
        
        sumatoria_redondeada=round(sumatoria,2)
        self.un_cuadro_de_variabilidad.set_suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida(sumatoria_redondeada)
        
        self.calcular_la_varianza(todos_los_datos,sumatoria_redondeada)
    
    def calcular_la_varianza(self, todos_los_datos, sum_cuadra_desvi_resp_media):
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
            
            
        self.un_cuadro_de_variabilidad.set_varianza(varianza)
        self.un_cuadro_de_variabilidad.set_poblacion_o_muestra(desicion_varianza)
        
        self.calcular_desviacion_estandar(varianza, desicion_varianza)
        
        
    def calcular_desviacion_estandar(self, varianza, desicion_varianza):
        desviacion_estandar= round(varianza ** 0.5,2) #sacar la raiz cuadrada de la varianza
        
        self.un_cuadro_de_variabilidad.set_desviacion_estandar(desviacion_estandar)
        self.definir_el_numero_menor_del_rango(desviacion_estandar)
        
        
    def definir_el_numero_menor_del_rango(self, desviacion_estandar):
        num_menor_rango= float(input("Por favor ingrese el numero menor que desee que se analice con el teorema de chevyshev: "))
        
        num_mayor_rango= float(input("Por favor ingrese el numero mayor que desee que se analice con el teorema de chevyshev: "))
        
        self.un_cuadro_de_variabilidad.set_num_menor_rango(num_menor_rango)
        
        self.un_cuadro_de_variabilidad.set_num_mayor_rango(num_mayor_rango)
        
        self.calcular_puntos_z_interno(desviacion_estandar, num_menor_rango, num_mayor_rango)
        
        
    def calcular_puntos_z_interno(self, desviacion_estandar, num_menor_rango, num_mayor_rango):
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()
        #me dice a cuantas desviaciones estandar se encuentra un numero de la media muestra
        desviacion_num_menor= round((num_menor_rango -media_muestral)/ desviacion_estandar,4)
        desviacion_num_mayor= round((num_mayor_rango - media_muestral)/ desviacion_estandar,4)

        self.calcular_el_porcentaje_segun_el_teorema_de_chevyshev(desviacion_estandar, desviacion_num_menor, desviacion_num_mayor)
    
    def calcular_el_porcentaje_segun_el_teorema_de_chevyshev(self, desviacion_estandar, desviaciones_num_menor, desviaciones_num_mayor):
        if(desviaciones_num_mayor == desviaciones_num_menor):
            porcentaje= (1-(1/(desviaciones_num_menor*2)))
            porcentaje_real=round(porcentaje*100 , 2)
        
        else:
           
            if(desviaciones_num_menor<0):
                desviaciones_num_menor*=-1
            
            if(desviaciones_num_mayor<0):
                desviaciones_num_mayor*=-1
                
            k1= round(1- (1/desviaciones_num_menor**2) , 4)
            
            k2= round(1- (1/desviaciones_num_mayor**2) , 4)
            
            if(k1>k2):
                residuo_resta=k1-k2
                porcentaje_parcial=round(k1-(residuo_resta)/2 , 2)
            
            else:

                residuo_resta=k2-k1
                porcentaje_parcial=k2-(residuo_resta)/2
            porcentaje_real= round((porcentaje_parcial)*100 )
            
        self.un_cuadro_de_variabilidad.set_porcentaje_chevyshev(porcentaje_real)
        
        self.puntos_z_requeridos(desviacion_estandar)
    
    
    def puntos_z_requeridos(self, desviacion_estandar):
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()
        
        desea_puntos_z=int(input("\n¿Desea conocer a cuantas desviaciones estandar de la media muestras se encuentra algún numero en específico?  1.Si  2.No \n"))
        while(desea_puntos_z<1 or desea_puntos_z>2):
            desea_puntos_z=int(input("por favor elija una de las 2 opciones:  1.Si  2.No \n"))
        
        if(desea_puntos_z==1):
            numero= float(input("Por favor ingrese el numero el cual desee conocer a cuantas desviaciones estandar se encuentra de la media_muestral:  "))
            resultado_desicion= round((numero - media_muestral)/ desviacion_estandar,2)
            if (resultado_desicion<0):
                resultado_desicion*=-1
            
        else:
            numero= "No se ingresó ningún numero"
            resultado_desicion= "No se ingresó ningún numero"
            
            
        self.un_cuadro_de_variabilidad.set_numero_puntos_z(numero)    
        self.un_cuadro_de_variabilidad.set_puntos_z(resultado_desicion)
        
        self.llamado_para_mostrar_los_datos(desea_puntos_z)
        
    
    def llamado_para_mostrar_los_datos(self,desea_puntos_z):
        medidas_de_variabilidad= self.un_cuadro_de_variabilidad.mostrar_los_datos_de_las_medidas_de_variabilidad(desea_puntos_z)
        
        self.una_vista_medidas_de_variabilidad.mostrar_las_medidas_de_variabilidad(medidas_de_variabilidad)
            