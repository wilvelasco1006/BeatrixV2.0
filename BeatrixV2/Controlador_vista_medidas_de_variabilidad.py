from Medidas_de_variabilidad import Medidas_de_variabilidad
from Vista_medidas_de_variabilidad import Vista_medidas_de_variabilidad
from Diagrama_de_caja import Diagrama_de_caja
from Diagrama_de_caja_para_txt import Diagrama_de_caja_para_txt


class Controlador_vista_medidas_de_variabilidad:
    #atributos
    un_cuadro_de_frecuencia=None
    un_cuadro_de_variabilidad= Medidas_de_variabilidad()#variable para crear un objeto medidas de variabilidad para rellenar y luego acceder a sus atributos
    una_vista_medidas_de_variabilidad= Vista_medidas_de_variabilidad()# permite mostrar las medidas de variabilidad junto con el teorema de chevyshev
    un_diagrama_de_caja= Diagrama_de_caja()# objeto que me permite mostrar el diagrama de caja 
    diagrama_de_caja_para_txt= Diagrama_de_caja_para_txt()
    #metodos
    #metodo constructor
    def __init__(self):
        pass
    
    def importar_cuadro_de_frecuencias(self):
        from Controlador_vista_cuadro_de_frecuencias_intervalos import Controlador_vista_cuadro_de_frecuencias_intervalos
        self.un_cuadro_de_frecuencia=Controlador_vista_cuadro_de_frecuencias_intervalos()
    
    #Metodo que me permite calcular el rango de los datos
    def calcular_el_rango(self,todos_los_datos, cuartil_1, cuartil_3,cuartil_2, grafico_seleccionado, nombre_archivo_final):
        rango= (max(todos_los_datos) - min(todos_los_datos))
        
        self.un_cuadro_de_variabilidad.set_nombre_archivo_final(nombre_archivo_final)# proceso para almacenar el nombre del archivo .txt en el que se almacenan todo los resultados del análisis
        
        self.un_cuadro_de_variabilidad.set_grafico_seleccionado(grafico_seleccionado)# proceso para almacenar el número de la operación a realizar ingresado por el usuario
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_todos_los_datos(todos_los_datos)#proceso para guardar la lista de datos con las que se va a trabajar
        
        self.un_cuadro_de_variabilidad.set_rango(rango)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_el_rango_intercuartico(todos_los_datos, cuartil_1, cuartil_3,cuartil_2)
        
    #metrodo que me permite calcular el rango intercuartico
    def calcular_el_rango_intercuartico(self, todos_los_datos,cuartil_1,cuartil_3,cuartil_2):
        
        rango_inter_cuartico= round(cuartil_3 - cuartil_1, 3)#proceso para callcular cual es el rango intercuartico
        
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
        while True:
            
            try:#try catch para que el programa no se detenga en el caso en que se ingresen datos en lugar de números 
                
                tipo_de_varianza = int(input("¿Qué tipo de varianza desea que se emplee? 1. Poblacional  2. Muestral \n")) #input para que el usuario defina el tipo de varianza que prefiera el usuario
                
                
                if tipo_de_varianza>=1 and tipo_de_varianza <=2: # condicional para verificar que el dato ingresado se encuentre dentro del rango 1-2   S
                    break
                else:
                    print("Por favor, ingrese 1 para Poblacional o 2 para Muestral.")
                    
                    
            except ValueError:# mensaje de error para cuand ose ingrese una letra en lugar de un número
                print("Entrada no válida. Por favor, ingrese un número (1 o 2).")
                
        

        desicion_varianza=False
        
        #condicional para definirt tipo de varianza se empleará
        if (tipo_de_varianza==1): #condicional para convetir el tipo de varianza seleccionada de un numero a un valor booleano 
            
            desicion_varianza=True #1=poblacional
            with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# proceso para guardar que la varianza escogida fue la poblacional
                f.write("tipo de varianza escogida: varianza poblacional \n")
                    
        else:
            desicion_varianza=False #2=muestral
            with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# # proceso para guardar que la varianza escogida fue la muestral
                f.write("tipo de varianza escogida: varianza muestral \n")
            
        #condicional para definir si la varianza será muestral o poblacional
        if(desicion_varianza==True):
            varianza= round(sum_cuadra_desvi_resp_media/len(todos_los_datos),2) # proceso para calcular la varianza poblacional
            
        else:
            varianza= round(sum_cuadra_desvi_resp_media/(len(todos_los_datos )- 1),2) # proceso pra calcular la varianza muestral
            
        
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
        
        
        while True:# try catch para que el programa no deje de ejecutarse en el caso de que se ingrese texto en lugar de números     
            try:
                num_menor_rango= float(input("Por favor ingrese el numero menor que desee que se analice con el teorema de chevyshev: "))#numero menor para definir un rango y calcular el porcentaje de datos que se encuentran en ese reango
                
            
                if(num_menor_rango==self.un_cuadro_de_variabilidad.get_media_muestral()):# condicional para que no lance error en el caso de que en el número menor se ingrese el mismo valor de la media muestral o poblacional
                    print("el número menor no puede ser igual que la media muestral")
                
                else:
                    break
            
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")# mensaje de error para el caso de que se ingrese texto en lugar de números
        
        with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# proceso para innsertar el numero menor escogido para definir un rango con el teorema de chevyshev en el archivo .txt
                    f.write("numero menor escogido para definir un rango con el teorema de chevyshev: "+ str(num_menor_rango) +"\n")
            
        while True:
            try:# try catch para que el programa no deje de ejecutarse en el caso de que se ingrese texto en lugar de números 
                
                num_mayor_rango= float(input("Por favor ingrese el numero mayor que desee que se analice con el teorema de chevyshev: "))#numero mayor para definir un rango y calcular el porcentaje de datos que se encuentran en ese reango
                
                if(num_mayor_rango==self.un_cuadro_de_variabilidad.get_media_muestral()):# condicional para que no lance error en el caso de que en el número menor se ingrese el mismo valor de la media muestral o poblacional
                    print("el número mayor no puede ser igual que la media muestral")
                
                else:
                    break
                    
                
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")# menjsae de error para el caso de que se ingrese texto en lugar de números
        
        with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# proceso para innsertar el numero mayor escogido para definir un rango con el teorema de chevyshev en el archivo .txt
                    f.write("numero mayor escogido para definir un rango con el teorema de chevyshev: "+ str(num_mayor_rango) +"\n")
        
        
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_num_menor_rango(num_menor_rango)
        self.un_cuadro_de_variabilidad.set_num_mayor_rango(num_mayor_rango)
        
        #llamado al siguiente metodo para continuar con el programa
        self.calcular_puntos_z_interno(desviacion_estandar, num_menor_rango, num_mayor_rango, cuartil_1, cuartil_3,cuartil_2)
        
    
    #metodo para calcular puntos z que se usa solo para los datos que se van a evaluar en el teorema de chevyshev
    def calcular_puntos_z_interno(self, desviacion_estandar, num_menor_rango, num_mayor_rango, cuartil_1, cuartil_3,cuartil_2):
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()#Se obtiene la lista todos los datos tras usar el metodo get para pedirsela al objeto un)cuadro_de_varibilidad
        
        #proceso para saber la cantidad de desviaciones estandar entre el numero mayor y menor de la media muestral o poblacional
               
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
        while True:
            try:#try catch para que el programa no deje de ejecutarse en el caso
                
                desea_puntos_z=int(input("\n¿Desea conocer a cuantas desviaciones estandar de la media muestral se encuentra algún numero en específico?  1.Si  2.No \n"))
                if(desea_puntos_z==1 or desea_puntos_z==2):
                    break
                 
            except ValueError:  
                print("Entrada no válida. Por favor, ingrese un número entre 1  y 2.")# mensaje de error para el caso de que se ingrese texto en lugar de números
        
        with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# proceso para insertar la pregunta sobre si se desea conocer la distancia en desviaciones estandar de un número enel archivo .txt
                    f.write("\n¿Desea conocer a cuantas desviaciones estandar de la media muestral se encuentra algún numero en específico?  1.Si  2.No \n")
                    
        
        if(desea_puntos_z==1):
            
            while True:
                try:
                    #En el caso de que el usuario si desee conocer la cantidad de vaiaciones estandar a la que se encuentra un número lo podrá ingresar a cotinuación 
                    numero= float(input("Por favor ingrese el numero el cual desee conocer a cuantas desviaciones estandar se encuentra de la media_muestral:  "))
                    break
                except ValueError:

                    print("Por favor ingrese un número")# mensaje de error para el caso de que se ingrese texto en lugar de números
            
            resultado_desicion= round((numero - media_muestral)/ desviacion_estandar,2) #proceso par calcular la cantidad de desviaciones estandar del número ingresado
            if (resultado_desicion<0):
                resultado_desicion*=-1
                
            with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# # metodo para almacenar el numero que el cliente eligió para conocer su distancia con la media muestral en desviaciones estandar en el archivo .txt
                    f.write("el número elegido para conocer su distancia con la media muestral o poblacional en desviaciones estandar es  "+ str(resultado_desicion) +"\n")
        
        #En el caso en que no se quiera saber los puntos z de otro dato en especifico saldrá un mensaje de no se ingresó ningún numero
        else:
            numero= "No se ingresó ningún numero"
            resultado_desicion= "No se ingresó ningún numero"
            
            with open(self.un_cuadro_de_variabilidad.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:# metodo para almacenar el mensaje de que no se eligió ningún numero para conocer su distancia con la media muestral en desviaciones estandar en el archivo .txt
                    f.write("No se ingresó ningún numero \n")
        
            
        #uso del objeto un_cuadro_de_variabilidad para guardar datos en los atributos del mismo
        self.un_cuadro_de_variabilidad.set_numero_puntos_z(numero)    
        self.un_cuadro_de_variabilidad.set_puntos_z(resultado_desicion)
        
        #llamado al siguiente metodo para continuar con el programa
        self.definir_media_y_desviaciones_estandar(desea_puntos_z,desviacion_estandar, cuartil_1, cuartil_3,cuartil_2)
    
    def definir_media_y_desviaciones_estandar(self,desea_puntos_z,desviacion_estandar, cuartil_1, cuartil_3,cuartil_2):
        tabla=[[]]
        media_muestral= self.un_cuadro_de_variabilidad.get_media_muestral()

        for i in range (3, 0, -1 ):
            tabla[0].append(str(round(media_muestral - (desviacion_estandar*i) , 1))) # proceso para almacenar los valores menores a la media muestral que se pondrán en la parte inferior del teorema de chevyshev  
        
        for i in range(4):
            tabla[0].append(str(round(media_muestral + (desviacion_estandar*i), 1)))  # proceso para almacenar los valores mayores a la media muestral que se pondrán en la parte inferior del teorema de chevyshev  
            
        self.un_cuadro_de_variabilidad.set_media_y_desviaciones_estandar(tabla)    
            
        self.preparar_para_mostrar_diagrama_de_caja(desea_puntos_z,tabla, cuartil_1, cuartil_3,cuartil_2)
        
    def preparar_para_mostrar_diagrama_de_caja(self,desea_puntos_z,tabla, cuartil_1, cuartil_3,cuartil_2):
        
        rango_intercuartico=self.un_cuadro_de_variabilidad.get_rango_intercuartico()
        
        limite_inferior=round((cuartil_1- rango_intercuartico) , 1)#proceso para calcular el límite inferior de los datos para el diagrama de caja
        
        limite_superior= round((cuartil_3 + rango_intercuartico) , 1)#proceso para calcular el límite superior de los datos para el diagrama de caja
        
        cuartil_1_redondeado=round(cuartil_1 , 1)
        
        lista=[[limite_inferior,cuartil_1_redondeado,cuartil_2,cuartil_3,limite_superior]]# lista que contendrá los valores de la parte de abajo del diagrama de caja
        
        
        self.llamado_para_mostrar_los_datos(desea_puntos_z,tabla,lista,limite_superior)
        
        
    #metodo que me permitirá almacenar los datos atípicos   
    def determinar_las_observaciones_atipicas(self, limite_superior):
        
        observ_atipicas = []

        for dato in self.un_cuadro_de_variabilidad.get_todos_los_datos():
            if dato > limite_superior and dato not in observ_atipicas:
                observ_atipicas.append(dato)
                
        return observ_atipicas
    
    #metodo para enviarle los datos organizados a la vista para que los muestre allá
    def llamado_para_mostrar_los_datos(self,desea_puntos_z,tabla,lista,limite_superior):
        #obteniendo los datos ordenados en una sola variable para mostrarla posteriormente
        medidas_de_variabilidad= self.un_cuadro_de_variabilidad.mostrar_los_datos_de_las_medidas_de_variabilidad(desea_puntos_z)
        
        #variable que contiene el número de la operación elegida por el usuario
        grafico_seleccionado=self.un_cuadro_de_variabilidad.get_grafico_seleccionado()
        
        nombre_archivo_final= self.un_cuadro_de_variabilidad.get_nombre_archivo_final()
        
        if(grafico_seleccionado==7 or grafico_seleccionado==9):  # condicional para que se ejecute en el caso de que la opción elegida haya sido el 7 o el 9 (diagrama de caja o todas las tablas)
             
            observ_atipicas= self.determinar_las_observaciones_atipicas(limite_superior)
            self.un_diagrama_de_caja.dibujar(lista, observ_atipicas)# llamado a la clase que construirá el diagrama de caja
            
            self.diagrama_de_caja_para_txt.dibujar(lista, observ_atipicas, nombre_archivo_final)
            
            if(grafico_seleccionado==7):# condicional que me permite hacer que el programa se ejecute de nuevo para que mantenga abierto
                self.importar_cuadro_de_frecuencias()
                self.un_cuadro_de_frecuencia.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)
        
        
        if(grafico_seleccionado==8 or grafico_seleccionado==9):# condicional para que se ejecute en el caso de que la opción elegida haya sido el 8 o el 9 (medidas de variabilidad y teorema de chevyshev o todas las tablas)
            
            self.una_vista_medidas_de_variabilidad.mostrar_las_medidas_de_variabilidad(medidas_de_variabilidad,tabla,nombre_archivo_final)# llamado a la clase que imprimirá los resultados de las medidas de variabilidad y el teorema de chevyshev

            if(grafico_seleccionado==8):# condicional que me permite hacer que el programa se ejecute de nuevo para que mantenga abierto
                self.importar_cuadro_de_frecuencias()
                self.un_cuadro_de_frecuencia.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)
        
        