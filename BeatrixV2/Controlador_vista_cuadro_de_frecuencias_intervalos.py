from Cuadro_de_frecuencias_intervalos import Cuadro_de_frecuencias_intervalos as cuadro_de_frecuencias
from Controlador_vista_medidas_de_tendencia_central import Controlador_vista_medidas_de_tendencia_central
from Grafica_de_frecuencias import accion_1 
from Grafica_de_frecuencias_para_txt import Grafica_de_frecuencias_para_txt 
from Grafica_de_barras import Grafica_de_barras
from menu_opciones import menu
from Grafica_histograma import Grafica_histograma
from Grafica_de_pastel import Grafica_de_pastel
from Grafica_de_ojiva import Grafico_de_ojiva

class Controlador_vista_cuadro_de_frecuencias_intervalos():
    #Atributos
    un_cuadro_de_frecuencias= cuadro_de_frecuencias() #objeto para crear una tabla de frecuencias par a rellenar y luego acceder a sus atributos
    un_diagra_de_barras= Grafica_de_barras()# objeto para crear la gráfica de barras en la consola
    unas_medidas_de_tendencia= Controlador_vista_medidas_de_tendencia_central()# variable que me crea el objeto medidas de tendencia para luego llenar sus atributos y acceder a ellos
    una_grafica_de_frecuencias= accion_1() # objeto para crear una gráfica de barras
    grafico_frecuencia_para_txt= Grafica_de_frecuencias_para_txt() # objeto para crear la gráfica de barras en el documento .txt con los resultados
    una_grafica_histograma= Grafica_histograma() # objeto para crear un histograma
    menu_graficos= menu() #objeto que me permite crear la gráfica que contiene las opciones de las operaciones a elegir
    un_grafico_de_pastel= Grafica_de_pastel() # objeto que me permite crear un diagramma de pastel
    una_ojiva=Grafico_de_ojiva()# objeto que me permite crear una ojiva
    
    #Metodoss
    #Metodo constructor
    def __init__(self,):
        pass

    #Metodo para llenar una lista con todos los datos para analizar
    def ingresar_y_almacenar_todos_los_datos(self, nombre_archivo_final):
        self.un_cuadro_de_frecuencias.set_nombre_archivo_final(nombre_archivo_final)
        
        #listas para seccionar el contenido del archivo .csv que voy a analizar 
        datos_temperatura_interior=[]
        datos_humedad_interior=[]
        datos_temperatura_exterior=[]
        datos_humedad_exterior=[]
        datos_presion_relativa=[]
        datos_presion_absoluta=[]

        llenado=False
     
        while (llenado == False):
            
            #try catch para gestionar los errores que aparezcan al ingresar erroneamente la dirección raíz del archivo y que no deje de correr el programa 
            try:
                print('\u2501'*120) #codigo ASCI o UNICODE para generar una linea continua de 120 caracteres de largo
                
                #variable que contiene la dirección raíz del archivo .csv a evaluar o leer
                archivo_csv= input("Por favor ingrese la raiz del archivo .csv a evaluar, asegurese de que los datos se encuentren seaparados por comas ',' Ej: \nD://Programacion//repositorios//BeatrixV2//base de datos para pruebas meteorologica//datos1.csv\n\n")
                
                #metodo open que me permite abrir un archivo o crearlo si no exito, y que lo mantiene abierto a través de la f que luego uso para escribir o modificar su contenido
                with open(nombre_archivo_final, 'a', encoding='utf-8') as f:# el encoding= utf-8 me permite el ingreso de carácteres que no llegan a ser especiales, pero no hacen parte de los estandares
                    f.write("dirección ingresada: "+ archivo_csv + '\n')
                
               # abrir el archivo csv
                with open(archivo_csv, mode='r') as archivo: # metodo open para abrir el documento de terminación.csv el mode r se refiere a read o solo lectura
                    
                    # Leer los datos del archivo CSV fila por fila

                    # Convertir los datos de humedad de String a int
                    
                    for indice, linea in enumerate(archivo):
                        # Saltar la primera fila (índice 0)
                        if indice == 0:
                            continue
        
                        # Eliminar caracteres de nueva línea y separar por comas
                        fila = linea.strip().split(',')
        
                        if fila[3] != '':
                            datos_temperatura_interior.append(float(fila[3])) # Convertir los datos de temperatura exterior y presión de String a float
        
                        if fila[4] != '':    
                            datos_humedad_interior.append(int(fila[4]))   # Convertir los datos de humedad interior y humedad interior de String a int
        
                        if fila[5] != '--.-' and fila[5] != '':
                            datos_temperatura_exterior.append(float(fila[5]))
        
                        if fila[6] != '--' and fila[6] != '': #condición para no guardar el dato en el caso en que haya un caracter o dato que no sea un número o texto que no pueda ser convertido a número
                            datos_humedad_exterior.append(int(fila[6]))    
        
                        if fila[7] != '':
                            datos_presion_relativa.append(float(fila[7]))
        
                        if fila[8] != '':
                            datos_presion_absoluta.append(float(fila[8]))
                        
                    llenado=True
                        
            except FileNotFoundError: # mensaje para el caso en que no se encuentre la dirección raíz del archivo .csv
                print("\n El archivo no fue encontrado o la dirección del directorio es incorrecta.")
                

        #Guardar las listas que se acaban de llenar con los datos del archivo .csv en los atributos respectivos del objeto cuadro_de_frecuencias
        self.un_cuadro_de_frecuencias.set_datos_temperatura_interior(datos_temperatura_interior)
        self.un_cuadro_de_frecuencias.set_datos_humedad_interior(datos_humedad_interior)
        self.un_cuadro_de_frecuencias.set_datos_temperatura_exterior(datos_temperatura_exterior)
        self.un_cuadro_de_frecuencias.set_datos_humedad_exterior(datos_humedad_exterior)
        self.un_cuadro_de_frecuencias.set_datos_presion_relativa(datos_presion_relativa)
        self.un_cuadro_de_frecuencias.set_datos_presion_absoluta(datos_presion_absoluta)
         
        #aparicion de menu para seleccionar el grafico o contenido que desee ver 
        
        
        grafico_seleccionado=self.menu_graficos.dibujar(nombre_archivo_final) #variable que contiene el número de la opción elegida por el usuario
        
        self.un_cuadro_de_frecuencias.set_grafico_seleccionado(grafico_seleccionado)#guardar el gráfico seleccionado en su atributo correspondiente en el objeto cuadro de frecuencias
        
        #metodo para guardar o escribir en el archivo .txt que va a almacenar los resultados la opción de operación elegida
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write("grafico seleccionado: "+ str(grafico_seleccionado) + '\n\n')
                
        
        while True:
            
            #try catch para que el programa no deje de ejcutarse en el caso de que se ingrese texto en lugar de numeros
            try:
                
                #Selección de la columna a la que se desee aplicar el análisis y la operación seleccionada anteriormente
                numero_lista = int(input("¿Qué columna desea evaluar?: \n\n1. Datos temperatura interior      2. Datos humedad interior \n\n3. Datos temperatura exterior       4. Datos humedad exterior \n\n5. Datos presión relativa          6. Datos presión absoluta\n\n"))
                
                if 1 <= numero_lista <= 6:# condicional para verificar que  el numero ingresado se encuentre entre el rango de opciones 1-6
                    break
                else:
                    print("Debe ingresar un número entre 1 y 6.")#mensaje de error en el caso de que se ingrese un numero que se encuentre por fuera del rango 1-6
                    
            except ValueError:
                print("Debe ingresar un número válido.")#mensaje de error en el caso de que se ingrese texto en lugar de numeros
            
            
        #operación para escribir en el archivo .txt que contiene los resultados la columan elegida para traba        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write("Que columna desea evaluar?: \n\n1. Datos temperatura interior      2. Datos humedad interior \n\n3. Datos tempeatura exterior       4. Datos humedad exterior \n\n5. Datos presion relativa          6. Datos presion_ bsoluta\n\n"+                         "numero de columna seleccionado: "+str(numero_lista) + '\n\n')
        
        #Guardar el número de la lista seleccionada a su respectivo atributo en el objeto tablas de frecuencia
        self.un_cuadro_de_frecuencias.set_numero_lista(numero_lista)    
        
        
        #Llamado al metodo determinar_el_ancho_de_cada_intervalo para decifrar la cantidad de elementos que se encontrarán en el rango de cada intervalo
        self.determinar_el_ancho_de_cada_intervalo ()
    
    #A partir de este momento se trabajará con solo una lista, la cual fué seleccionada a partir de las opciones de las columnas. A continuación se
    # va a guardar en esa lista de nombre lista el contenido de esa lista elegida anteriormente
    
    def copiar_lista(self):
        lista= []
        if(self.un_cuadro_de_frecuencias.get_numero_lista()==1):# se copiara el contenido de la lista 1 elegida anteriormente
            for dato in self.un_cuadro_de_frecuencias.get_datos_temperatura_interior():
                lista.append(dato) #proceso para pasar el contenido de una lista a otra
                
        elif(self.un_cuadro_de_frecuencias.get_numero_lista()==2):
            for dato in self.un_cuadro_de_frecuencias.get_datos_humedad_interior():
                lista.append(dato)
            
        elif(self.un_cuadro_de_frecuencias.get_numero_lista()==3):
            for dato in self.un_cuadro_de_frecuencias.get_datos_temperatura_exterior():
                lista.append(dato)
        
        elif(self.un_cuadro_de_frecuencias.get_numero_lista()==4):
            for dato in self.un_cuadro_de_frecuencias.get_datos_humedad_exterior():
                lista.append(dato)
        
        elif(self.un_cuadro_de_frecuencias.get_numero_lista()==5):
            for dato in self.un_cuadro_de_frecuencias.get_datos_presion_relativa():
                lista.append(dato)
        
        elif(self.un_cuadro_de_frecuencias.get_numero_lista()==6):
            for dato in self.un_cuadro_de_frecuencias.get_datos_presion_absoluta():
                lista.append(dato)
        
        return lista #finalmente se retorna una copia de la lista elegida anteriormente
     
    
    #Método para  determinar el ancho de cada intervalo con base a restar el numero_mayor con el numero_menor y dividir todo entre el numero de intervalos
    def determinar_el_ancho_de_cada_intervalo(self):
        todos_los_datos=[]
        
        for dato in self.copiar_lista():
            todos_los_datos.append(dato) #aplicación del método anterior para copiar la lista que se haya seleccionado anteriormente

        todos_los_datos.sort() # función para organizar una lista de manera ascendente integrada en python
        
        while True:
            try:#try catch para evitar que la ejecución del programa se interrumpa por el ingreso de texto en lugar de números 
                
                #ingreso por parte del usuario la cantidad de intervalos en los que se distribuirán los datos importados del archivo .csv y la columna elegida
                num_intervalos= int(input("Por favor ingrese el numero de intervalos con los que se va a análizar los datos, minimo 5:  ")) 
                if num_intervalos>=5:
                    break
                else:
                    print("Debe ingresar un número mayor o igual a 5.") # mensaje para cuando se ingrese un número menos a 5
                    
            except ValueError:
                print("Debe ingresar un número válido.") #mensaje para cuando se ingrese texto en lugar de números                
            
            
        #Función para almacenar en el archivo .txt la cantidad de intervalos elegida por el usuario
        with open(self.un_cuadro_de_frecuencias.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:
            f.write("numero de intervalos seleccionado: "+str(num_intervalos) + '\n\n')
            
         
        numero_mas_pequeno= min(todos_los_datos)# función integrada en python para obtener el número más pequeño de una lista
        numero_mas_grande=max(todos_los_datos)# función integrada en python para obtener el número más grande de una lista
        
        
        #condicional para redondear el resultado de calcular el ancho de cada intervalo a un número entero para el caso en que los datos análiados sean enteros
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
            ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos)
            
        #condicional para redondear el resultado de calcular el ancho de cada intervalo a un número con un decimal extra para el caso en que los datos análiados sean reales 
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
            ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos,1)
            
        #condicional para redondear el resultado de calcular el ancho de cada intervalo a un número con hasta 2 decimales para el caso en que los datos análiados sean reales con un decimal extra
        else:
            ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos,2)
        
        #Llamado al metodo determinar_frecuencias_en_grados para continuar con la recoleccion de las frecuencias
        self.determinar_intervalos(ancho_intervalos, num_intervalos,todos_los_datos)
        
        
    #Metodo para hacer la lista de los intervalos que se van a crear, aunque la lista es visual, de tipo string
    def determinar_intervalos(self, ancho_intervalos,num_intervalos,todos_los_datos ):
        intervalos= []
        
        #condicional para el caso en que la lista elegida se conforme de números enteros
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
                menor= (min(todos_los_datos) -1)# calculo para definir el número más pequeño de los intervalos
                
        #condicional para el caso en que la lista elegida se conforme de números reales         
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
                menor= (min(todos_los_datos) -0.1)
       
        #condicional para el caso en que la lista elegida se conforme de números reales muy pequeños que necesiten 2 decimales   
        else:
            menor= (min(todos_los_datos) -0.01)
            
            
        mayor= (menor + ancho_intervalos)# calculo para definir el número más grande de los intervalos
        
        #Desicion para determinar como se van a crear los intervalos segun si los numeros son enteros o decimales
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
            
            #ciclo para rellenar la lista intervalos para numeros enteros con los mensajes de los intervalos que se evaluaran en un rato
            for i in range(num_intervalos):
                intervalo= "("+str(menor)+"-"+str(mayor)+")"
                intervalos.append(intervalo)
                menor+=(ancho_intervalos + 1)
                mayor+= (ancho_intervalos + 1)
                
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
            #ciclo para rellenar la lista intervalos para numeros reales con los mensajes de los intervalos que se evaluaran en un rato
            for i in range(num_intervalos):
                intervalo= str(round(menor,2))+"-"+str(round(mayor,2))
                intervalos.append(intervalo)
                menor+=(ancho_intervalos + 0.1)
                mayor+= (ancho_intervalos + 0.1)
        
        else:
             #ciclo para rellenar la lista intervalos para numeros reales que necesiten 2 decimales con los mensajes de los intervalos que se evaluaran en un rato
            for i in range(num_intervalos):
                intervalo= str(round(menor,3))+"-"+str(round(mayor,3))
                intervalos.append(intervalo)
                menor+=(ancho_intervalos + 0.01)
                mayor+= (ancho_intervalos + 0.01)
            
        #guardar la lista que contiene el texto o mensaje de los intervalos creados
        self.un_cuadro_de_frecuencias.set_datos_para_evaluar(intervalos)
        
        #Llamado al metodo determinar_la_frecuencia_de_aparicion_de_los_intervalos para continuar con la recoleccion de las frecuencias
        self.determinar_la_frecuencia_de_aparicion_de_los_intervalos(todos_los_datos,ancho_intervalos, num_intervalos,intervalos)
        
        
    #Metoto para determinar la cantidad de veces que un numero se encuentra en los rangos de cada intervalo 
    def determinar_la_frecuencia_de_aparicion_de_los_intervalos(self,todos_los_datos, ancho_intervalos, num_intervalos,intervalos):
        frecuencia_aparicion_intervalos= list()
        iteracion=0
        
        #proceso para definir el número más pequeño entre todos los datos de la lista seleccionado
        if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):
            menor= round(min(todos_los_datos) -1, 2)
           
        elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
                menor= (min(todos_los_datos) -0.1)
           
        else:
            menor= (min(todos_los_datos) -0.01)
            
        mayor= round(menor + ancho_intervalos, 2)#proceso para definir el número más grande entre todos los datos de la lista seleccionado
        
        
        #ciclo para determinar si un numero de todos los ingresados se encuentra en el rango de los intervalos
        while iteracion<= (num_intervalos-1):
            frecuencia=0
            for i in todos_los_datos:
                if (i>=menor and i<=mayor):
                    frecuencia+=1
                    
            #calculo para definir matemáticamente el rango en que se buscarán los datos para sumarlos a la frecuencia, en el caso en que los datos sean numeros enteros
            if (self.un_cuadro_de_frecuencias.numero_lista == 2 or self.un_cuadro_de_frecuencias.numero_lista == 4):                      
                frecuencia_aparicion_intervalos.append(frecuencia)
                menor+=(ancho_intervalos + 1)
                mayor+= (ancho_intervalos + 1)
            
            #calculo para definir matemáticamente el rango en que se buscarán los datos para sumarlos a la frecuencia, en el caso en que los datos sean numeros reales    
            elif(self.un_cuadro_de_frecuencias.numero_lista == 1 or self.un_cuadro_de_frecuencias.numero_lista == 3):
                frecuencia_aparicion_intervalos.append(frecuencia)
                menor+= (ancho_intervalos + 0.1)
                menor = round(menor, 2)
                mayor+= (ancho_intervalos + 0.1)
                mayor = round(mayor,2)
            
            #calculo para definir matemáticamente el rango en que se buscarán los datos para sumarlos a la frecuencia, en el caso en que los datos sean numeros reales con 2 decimales    
            else:
                frecuencia_aparicion_intervalos.append(frecuencia)
                menor+= (ancho_intervalos + 0.01)
                menor = round(menor, 3)
                mayor+= (ancho_intervalos + 0.01)
                mayor = round(mayor,3)
                
            
            iteracion +=1
        
        suma=0
        for i in frecuencia_aparicion_intervalos:
            suma+=i
            
        print ("Total de datos análizados: "+str(suma)) # mensaje que mostrará en consola la cantidad de datos análiados o que se encontraban en la lista seleccionada
        
        #proceso para almacenar en el archivo .txt la cantidad de datos análiados o que se encontraban en la lista seleccionada
        with open(self.un_cuadro_de_frecuencias.get_nombre_archivo_final(), 'a', encoding='utf-8') as f:
            f.write("Total de datos análizados: "+str(suma) + '\n\n')
            
        #Se envia la lista frecuencias_de_aparicion al objeto un_cuadro_de_frecuencia en el atributo frecuencia_de_aparicion
        self.un_cuadro_de_frecuencias.set_frecuencias_de_apari(frecuencia_aparicion_intervalos)
        
           
        self.determinar_las_frecuencias_relativas(frecuencia_aparicion_intervalos, todos_los_datos, intervalos)   
        
      
    #Metodo para obtener la frecuencia relativa de un dato con base a dividir su frecuencia entre el total de datos ingresados
    def determinar_las_frecuencias_relativas(self,frecuencias_de_apari, todos_los_datos, intervalos):
        frecuencias_relativas= list()
        
        for i in range(len(frecuencias_de_apari)):
            #operacion para dividir la frecuencia de apariciones de cada dato entre el total de datos ingresados, limitando la cantidad de decimales a 4
            frecuencias_relativas.append(round(frecuencias_de_apari[i]/(len(todos_los_datos)),4))
        
         #mandar la lista de frecuencias relativas  al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_relativas    
        self.un_cuadro_de_frecuencias.set_frecuencias_relativas(frecuencias_relativas)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_las_fecuencias_rel_acum(frecuencias_relativas, todos_los_datos, frecuencias_de_apari, intervalos)

    
    #Metodo para obtener la frecuencia relativa acumulada sumando consecutivamente los elementos de la lista de las frecuencias relativas    
    def determinar_las_fecuencias_rel_acum(self, frecuencias_relativas,todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_rel_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_relativas
        for i in range(len(frecuencias_relativas)):
            acumulado+= frecuencias_relativas[i]
            acumulado_redondeado=round(acumulado,3)
            frecuencias_rel_acum.append(acumulado_redondeado)
            
        #mandar la lista de frecuencias relativas acumuladas al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_rel_acum
        self.un_cuadro_de_frecuencias.set_frecuencias_relat_acu(frecuencias_rel_acum)
        
        self.determinar_frecuencias_porcentuales(frecuencias_relativas,todos_los_datos, frecuencias_de_apari, intervalos)
        
       
   #Metodo que saca la frecuencia porcentual tras multiplicar por 100 la frecuencia relativa 
    def determinar_frecuencias_porcentuales(self,frecuencias_relativas, todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_porcentuales= list()

        for i in range(len(frecuencias_relativas)):
            frecu_porcent=round(frecuencias_relativas[i]*100,4)# proceso para calcular la frecuencia porcentual a partir de la frecuencia relativa
            frecuencias_porcentuales.append(frecu_porcent)
            
        self.un_cuadro_de_frecuencias.set_frecuencias_procentuales(frecuencias_porcentuales)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_frecuencias_porcent_acum(frecuencias_porcentuales, todos_los_datos, frecuencias_de_apari, intervalos)
        
         
    #Metodo que almacena la sumatoria consecutiva de los datos de la lista de frecuencias_porcentuales
    def determinar_frecuencias_porcent_acum(self,frecuencias_porcentuales, todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_porcent_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_porcentuales
        for i in range(len(frecuencias_porcentuales)):
            acumulado+= frecuencias_porcentuales[i]
            acumulado_redondeado=round(acumulado,3)
            frecuencias_porcent_acum.append(acumulado_redondeado)
            
        
        self.un_cuadro_de_frecuencias.set_frecuencias_porcent_acu(frecuencias_porcent_acum)
        
        #Llamado al metodo determinar_frecuencias_en_grados para continuar con la recoleccion de las frecuencias
        self.determinar_frecuencias_en_grados(todos_los_datos, frecuencias_de_apari, intervalos)
        
       
    #Metodo que me permite convertir la frecuencia relativa en grados para poder repartirlos correctamente en un grafico de pastel   
    def determinar_frecuencias_en_grados(self, todos_los_datos, frecuencias_de_apari, intervalos):
        frecuencias_en_grados= list()
        frecuencias_relativas= self.un_cuadro_de_frecuencias.get_frecuencias_relativas()
        
        for i in range(len(frecuencias_relativas)):
            frecuencias_en_grados.append(round(frecuencias_relativas[i]*360,2)) #proceso para calcular los grados que ocuparía cada intervalo en un diagrama de pastel a pastir de la frecuencia relativa
            
        self.un_cuadro_de_frecuencias.set_frecuencias_en_grados(frecuencias_en_grados)
        
        tabla= self.un_cuadro_de_frecuencias.mostrar_la_tabla_de_frecuencias()
        
        
        #llamado al metodo para mostrar los datos organizados
        self.llamar_a_la_vista_para_mostrar_la_tabla_de_frecuencia(tabla, todos_los_datos, frecuencias_de_apari, intervalos)

     
    #metodo para llamar a la vista y mostrar los datos organizados
    def llamar_a_la_vista_para_mostrar_la_tabla_de_frecuencia(self, tabla, todos_los_datos, frecuencias_de_apari, intervalos):

        grafico_seleccionado= self.un_cuadro_de_frecuencias.get_grafico_seleccionado()# variable que contendrá el número de la operación seleccionada por el usuario 
        nombre_archivo_final=self.un_cuadro_de_frecuencias.get_nombre_archivo_final() # variable que contendrá el nombre del archivo en el que se almacenaran los resultados del análisis proporcionado por el usuario
        
        if(grafico_seleccionado ==1 or grafico_seleccionado ==9): # condicional para que se ejecute en el caso de que la opción elegida haya sido el 1 o el 12 (tabla de frecuencias o todas las tablas)
            
            self.una_grafica_de_frecuencias.dibujar(tabla)# llamado al metodo que construirá la tabla de frecuencias del objero una_grafica_de_frecuencias
            
            # llamado al metodo que construirá la tabla de frecuencias en el archivo .txt que almacena los resuldaos del objeto grafica_de_frecuencias_para_txt
            self.grafico_frecuencia_para_txt.dibujar(tabla,nombre_archivo_final)
            #se envía una lista que contiene otras listas de nombre tabla que contiene todas las frecuencias, el nombre del intervalo y los grados por cada lista. También se envía el nombre del archivo final para almacenar los datos en el archivo.txt con los resultados
            if(grafico_seleccionado ==1):
                self.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)
            
            
        if(grafico_seleccionado== 3 or grafico_seleccionado==9 ): # condicional para que se ejecute en el caso de que la opción elegida haya sido el 1 o el 9 (tabla de frecuencias o todas las tablas)
            
            self.una_grafica_histograma.dibujar(tabla,nombre_archivo_final) #llamado a el metodo dibujar de la clase una_grafica_histograma que contruirá el histograma
              
            if(grafico_seleccionado== 3):# condicional que me permite hacer que el programa se ejecute de nuevo para que mantenga abierto
                self.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)      
              
        if(grafico_seleccionado==4 or grafico_seleccionado==9): # condicional para que se ejecute en el caso de que la opción elegida haya sido el 4 o el 9 (diagrama de pastel o todas las tablas)
            
            self.un_grafico_de_pastel.dibujar(tabla, nombre_archivo_final) #llamado a el metodo dibujar de la clase Grafica_de_pastel que contruirá el diagrama de pastel

            if(grafico_seleccionado== 4):# condicional que me permite hacer que el programa se ejecute de nuevo para que mantenga abierto
                self.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)     
        
        
        if(grafico_seleccionado ==5 or grafico_seleccionado ==9): # condicional para que se ejecute en el caso de que la opción elegida haya sido el 5 o el 9 (diagrama de ojiva o todas las tablas)
            
            self.una_ojiva.dibujar(tabla)
            
            if(grafico_seleccionado== 5):# condicional que me permite hacer que el programa se ejecute de nuevo para que mantenga abierto
                self.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)
              
              
        if(grafico_seleccionado ==6 or grafico_seleccionado ==9):# condicional para que se ejecute en el caso de que la opción elegida haya sido el 6 o el 9 (diagrama de barras o todas las tablas)
            
            self.un_diagra_de_barras.dibujar(tabla,nombre_archivo_final)

            if(grafico_seleccionado== 6):# condicional que me permite hacer que el programa se ejecute de nuevo para que mantenga abierto
                self.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)     
        
        
            # condicional para que se ejecute en el caso de que la opción elegida haya sido el 2, el 7, el 8 o el 9 (medidas de tendencia central, el diagrama de caja, teorema de chevyshev o todas las tablas)
        if(grafico_seleccionado==2 or grafico_seleccionado ==7 or grafico_seleccionado==9 or grafico_seleccionado==9):        
            
            #llamado a la clase medidas_de_tendencia central para el calculo de las mismas, y posteriormente las medidas de variabilidad
            self.unas_medidas_de_tendencia.calcular_la_media(todos_los_datos,frecuencias_de_apari, intervalos, grafico_seleccionado, nombre_archivo_final) 
        