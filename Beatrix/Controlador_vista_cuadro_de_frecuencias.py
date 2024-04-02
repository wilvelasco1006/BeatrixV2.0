from Cuadro_de_frecuencias import Cuadro_de_frecuencias_datos_individuales as cuadro_de_frecuencias
from Vista_cuadro_de_frecuencias import Vista_cuadro_de_frecuencias
from Controlador_vista_medidas_de_tendencia_central import Controlador_vista_medidas_de_tendencia_central

class Controlador_vista_cuadro_de_frecuencias:
    #Atributos
    #Aquí estoy inicializando un objeto cuadro de frecuencias
    un_cuadro_de_frecuencias= cuadro_de_frecuencias()
    una_vista_cuadro_de_frecuencias= Vista_cuadro_de_frecuencias()
    unas_medidas_de_tendencia= Controlador_vista_medidas_de_tendencia_central()
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    #Este metodo va a recibir todos los datos a los que se les va a sacar las frecuencias
    def ingresar_y_almacenar_todos_los_datos(self):
        organizar_datos=False
        continuar= 1
        todos_los_datos= list()
        
        #Proceso para determinar si los datos que se van a ingresar son numéricos o de tipo texto, para decidir si organizar la lista todos_los_datos
        #esto ayudará para facilitar la busqueda de la mediana de los datos numericos 
        desicion= int(input("Que tipo de datos va a ingresar?  1.Numericos  2. De texto o nombres\n"))
        while (desicion<1 or desicion>2):
                desicion= int(input("Se ingresó un numero distinto a  1.Numericos  2.De texto o nombres  Por favor inténtelo de nuevo\n"))
        if (desicion== 1):
            organizar_datos=True
            opcion=True
        else:
            organizar_datos= False
            opcion=False
            
        
            
        #Metodo para llenar una lista con todos los datos para analizar
        while(continuar== 1):
            
            if(desicion==1):
                dato=int(input("Por favor ingrese los datos que desee analizar:  "))
                todos_los_datos.append(dato)
            else:
                dato=input("Por favor ingrese los datos que desee analizar:  ")
                todos_los_datos.append(dato.lower())
            
            continuar= int(input("\nDesea agregar otro dato? 1.Si  2.No\n"))
            while (continuar<1 or continuar>2):
                continuar= int(input("Se ingresó un numero distinto a  1.Si  2.No  Por favor inténtelo de nuevo\n"))
        
        if(desicion==2):
            #Aquí estoy llenando el atributo lista todos_los_datos del objeto cuadro de frecuencias
            self.un_cuadro_de_frecuencias.set_todos_los_datos(todos_los_datos)
        
            #Llamado al metodo determinar_los_datos_repetidos para continuar con la recoleccion de las frecuencias
            self.determinar_los_datos_repetidos(todos_los_datos,desicion)
        
        else:
            self.organizar_los_datos(todos_los_datos, opcion)
            
            
    #Metodo para organizar la lista de todos los datos a traves del metodo de insercion            
    def organizar_los_datos(self, todos_los_datos, desicion):
        #metodo de ordenamiento por insercion  
        for i in range(len(todos_los_datos)):
            pos=i
            auxiliar=todos_los_datos[i]
            
            while ((pos >0) and (auxiliar < todos_los_datos[pos-1])):
                todos_los_datos[pos]= todos_los_datos[pos-1]  
                todos_los_datos[pos-1]=auxiliar
                pos-=1
                auxiliar= todos_los_datos[pos]
  
        self.un_cuadro_de_frecuencias.set_todos_los_datos(todos_los_datos)
        
        self.determinar_los_datos_repetidos(todos_los_datos, desicion)
        
        #metodo para crear una lista que solo contendrá los datos que se repiten 
    def determinar_los_datos_repetidos(self, todos_los_datos, desicion):
        #estoy creando una lista datos_para_evaluar que se llenará solo con los datos que se repiten de la lista, o mejor dicho una vez cada vez que un dato aparece
        datos_para_evaluar= list(set(todos_los_datos))    
        
        for i in range(len(datos_para_evaluar)):
            pos=i
            auxiliar=datos_para_evaluar[i]
            
            while ((pos >0) and (auxiliar < datos_para_evaluar[pos-1])):
                datos_para_evaluar[pos]= datos_para_evaluar[pos-1]  
                datos_para_evaluar[pos-1]=auxiliar
                pos-=1
                auxiliar= datos_para_evaluar[pos]
        
        #Aquí estoy llenando el atributo lista todos_los_datos del objeto cuadro de frecuencias
        self.un_cuadro_de_frecuencias.set_datos_para_evaluar(datos_para_evaluar)
        
        #Llamado al metodo determinar_la_frecuencia_de_aparicion_de_los_dato para continuar con la recoleccion de las frecuencias
        self.determinar_la_frecuencia_de_aparicion_de_los_datos(datos_para_evaluar, desicion)
        
        
    #metodo para determinar y alamcenar la cantidad de veces que aparece un elemento de la lista datos_para_evaluar en la lista todos_los_datos
    def determinar_la_frecuencia_de_aparicion_de_los_datos(self,datos_para_evaluar, desicion):
        frecuencias_de_apari= list()
        
        #Ciclo que va a iterar segun la cantidad de elementos que tenga la lista datos_para_evaluar
        for i in range(len(datos_para_evaluar)):
            
            #Se almacena en la lista fecuencias de aparicion
            frecuencias_de_apari.append(self.un_cuadro_de_frecuencias.get_todos_los_datos().count(datos_para_evaluar[i])) 
            
            #Se envia la lista frecuencias_de_aparicion al objeto un_cuadro_de_frecuencia en el atributo frecuencia_de_aparicion
        self.un_cuadro_de_frecuencias.set_frecuencias_de_apari(frecuencias_de_apari)
        
        #Llamado al metodo determinar_las_frecuencias_relativas para continuar con la recoleccion de las frecuencias
        self.determinar_las_frecuencias_relativas(frecuencias_de_apari, desicion,datos_para_evaluar)
        
    
    #Metodo para obtener la frecuencia relativa de un dato con base a dividir su frecuencia entre el total de datos ingresados
    def determinar_las_frecuencias_relativas(self,frecuencias_de_apari, desicion,datos_para_evaluar):
        frecuencias_relativas= list()
        todos_los_datos=self.un_cuadro_de_frecuencias.get_todos_los_datos()
        
        for i in range(len(frecuencias_de_apari)):
            #operacion para dividir la frecuencia de apariciones de cada dato entre el total de datos ingresados, limitando la cantidad de decimales a 4
            frecuencias_relativas.append(round(frecuencias_de_apari[i]/(len(todos_los_datos)),2))
        
         #mandar la lista de frecuencias relativas  al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_relativas    
        self.un_cuadro_de_frecuencias.set_frecuencias_relativas(frecuencias_relativas)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_las_fecuencias_rel_acum(frecuencias_relativas,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar)
        
        
    #Metodo para obtener la frecuencia relativa acumulada sumando consecutivamente los elementos de la lista de las frecuencias relativas    
    def determinar_las_fecuencias_rel_acum(self, frecuencias_relativas, todos_los_datos, frecuencias_de_apari, desicion,datos_para_evaluar):
        frecuencias_rel_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_relativas
        for i in range(len(frecuencias_relativas)):
            acumulado+= frecuencias_relativas[i]
            acumulado_redondeado=round(acumulado,2)
            frecuencias_rel_acum.append(acumulado_redondeado)
            
        #mandar la lista de frecuencias relativas acumuladas al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_rel_acum
        self.un_cuadro_de_frecuencias.set_frecuencias_relat_acu(frecuencias_rel_acum)
        
        self.determinar_frecuencias_porcentuales(frecuencias_relativas, todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar)
        
        
    def determinar_frecuencias_porcentuales(self,frecuencias_relativas,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar):
        frecuencias_porcentuales= list()
        
        for i in range(len(frecuencias_relativas)):
            frecuencias_porcentuales.append(round(frecuencias_relativas[i]*100,2))
            
        self.un_cuadro_de_frecuencias.set_frecuencias_procentuales(frecuencias_porcentuales)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_frecuencias_porcent_acum(frecuencias_porcentuales,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar)
        
        
        
    def determinar_frecuencias_porcent_acum(self,frecuencias_porcentuales,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar):
        frecuencias_porcent_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_porcentuales
        for i in range(len(frecuencias_porcentuales)):
            acumulado+= frecuencias_porcentuales[i]
            acumulado_redondeado=round(acumulado,2)
            frecuencias_porcent_acum.append(acumulado_redondeado)
            
        
        self.un_cuadro_de_frecuencias.set_frecuencias_porcent_acu(frecuencias_porcent_acum)
        
        #Llamado al metodo determinar_frecuencias_en_grados para continuar con la recoleccion de las frecuencias
        self.determinar_frecuencias_en_grados(todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar)
        
        
    def determinar_frecuencias_en_grados(self,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar):
        frecuencias_en_grados= list()
        frecuencias_relativas= self.un_cuadro_de_frecuencias.get_frecuencias_relativas()
        
        for i in range(len(frecuencias_relativas)):
            frecuencias_en_grados.append(round(frecuencias_relativas[i]*360,2))
            
        self.un_cuadro_de_frecuencias.set_frecuencias_en_grados(frecuencias_en_grados)
        
        #Llamado al metodo mostrar_la_tabla_de_frecuencias del objeto un_cuadro_de_frecuencias para obtener 
        #una variable de tipo string que contiene todos los datos de la tabla de frecuencia
        tabla= self.un_cuadro_de_frecuencias.mostrar_la_tabla_de_frecuencias()
        
        self.llamar_a_la_vista_para_mostrar_la_tabla_de_frecuencia(tabla,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar)
        
        
    def llamar_a_la_vista_para_mostrar_la_tabla_de_frecuencia(self, tabla,todos_los_datos,frecuencias_de_apari, desicion,datos_para_evaluar):
        print(self.un_cuadro_de_frecuencias.get_todos_los_datos())
        self.una_vista_cuadro_de_frecuencias.mostrar_la_tabla_de_frecuencias(tabla)
        
        self.unas_medidas_de_tendencia.calcular_la_media(todos_los_datos,frecuencias_de_apari,desicion,datos_para_evaluar)
        