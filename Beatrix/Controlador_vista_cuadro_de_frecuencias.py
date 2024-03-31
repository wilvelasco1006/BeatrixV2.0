from Cuadro_de_frecuencias import Cuadro_de_frecuencias_datos_individuales as cuadro_de_frecuencias

class Controlador_vista_cuadro_de_frecuencias:
    #Atributos
    #Aquí estoy inicializando un objeto cuadro de frecuencias
    un_cuadro_de_frecuencias= cuadro_de_frecuencias()
    
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    #Este metodo va a recibir todos los datos a los que se les va a sacar las frecuencias
    def ingresar_y_almacenar_todos_los_datos(self):
        continuar= 1
        todos_los_datos= list()
        
        #Metodo para llenar una lista con todos los datos para analizar
        while(continuar== 1):
            dato=input("Por favor ingrese los datos que desee analizar:  ")
            todos_los_datos.append(dato)
            continuar= int(input("\nDesea agregar otro dato? 1.Si  2.No\n"))
            while (continuar<1 or continuar>2):
                continuar= int(input("Se ingresó un numero distinto a  1.Si  2.No  Por favor inténtelo de nuevo\n"))
        
        #Aquí estoy llenando el atributo lista todos_los_datos del objeto cuadro de frecuencias
        self.un_cuadro_de_frecuencias.set_todos_los_datos(todos_los_datos)
        
        #Llamado al metodo determinar_los_datos_repetidos para continuar con la recoleccion de las frecuencias
        self.determinar_los_datos_repetidos(todos_los_datos)
            
            
        #metodo para crear una lista que solo contendrá los datos que se repiten 
    def determinar_los_datos_repetidos(self, todos_los_datos):
        
        #estoy creando una lista datos_para_evaluar que se llenará solo con los datos que se repiten de la lista, o mejor dicho una vez cada vez que un dato aparece
        datos_para_evaluar= list(set(todos_los_datos))    
        
        #Aquí estoy llenando el atributo lista todos_los_datos del objeto cuadro de frecuencias
        self.un_cuadro_de_frecuencias.set_datos_para_evaluar(datos_para_evaluar)
        
        #Llamado al metodo determinar_la_frecuencia_de_aparicion_de_los_dato para continuar con la recoleccion de las frecuencias
        self.determinar_la_frecuencia_de_aparicion_de_los_datos(datos_para_evaluar)
        
        
    #metodo para determinar y alamcenar la cantidad de veces que aparece un elemento de la lista datos_para_evaluar en la lista todos_los_datos
    def determinar_la_frecuencia_de_aparicion_de_los_datos(self,datos_para_evaluar):
        frecuencias_de_apari= list()
        
        #Ciclo que va a iterar segun la cantidad de elementos que tenga la lista datos_para_evaluar
        for i in range(len(datos_para_evaluar)):
            
            #Se almacena en la lista fecuencias de aparicion
            frecuencias_de_apari.append(self.un_cuadro_de_frecuencias.get_todos_los_datos().count(datos_para_evaluar[i])) 
            
            #Se envia la lista frecuencias_de_aparicion al objeto un_cuadro_de_frecuencia en el atributo frecuencia_de_aparicion
        self.un_cuadro_de_frecuencias.set_frecuencias_de_apari(frecuencias_de_apari)
        
        #Llamado al metodo determinar_las_frecuencias_relativas para continuar con la recoleccion de las frecuencias
        self.determinar_las_frecuencias_relativas(frecuencias_de_apari)
        
    
    #Metodo para obtener la frecuencia relativa de un dato con base a dividir su frecuencia entre el total de datos ingresados
    def determinar_las_frecuencias_relativas(self,frecuencias_de_apari):
        frecuencias_relativas= list()
        todos_los_datos=self.un_cuadro_de_frecuencias.get_todos_los_datos()
        
        
        for i in range(len(frecuencias_de_apari)):
            #operacion para dividir la frecuencia de apariciones de cada dato entre el total de datos ingresados, limitando la cantidad de decimales a 4
            frecuencias_relativas.append(round(frecuencias_de_apari[i]/(len(todos_los_datos)),4))
        
         #mandar la lista de frecuencias relativas  al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_relativas    
        self.un_cuadro_de_frecuencias.set_frecuencias_relativas(frecuencias_relativas)
        
        #Llamado al metodo determinar_las_fecuencias_rel_acum para continuar con la recoleccion de las frecuencias
        self.determinar_las_fecuencias_rel_acum(frecuencias_relativas)
        
        
    #Metodo para obtener la frecuencia relativa acumulada sumando consecutivamente los elementos de la lista de las frecuencias relativas    
    def determinar_las_fecuencias_rel_acum(self, frecuencias_relativas):
        frecuencias_rel_acum= list()
        acumulado=0
        
        #Ciclo para asignarle a la variable acumulado la suma consecutiva de los elementos de la lista frecuencias_relativas
        for i in range(len(frecuencias_relativas)):
            acumulado+= frecuencias_relativas[i]
            frecuencias_rel_acum.append(acumulado)
            
        #mandar la lista de frecuencias relativas acumuladas al objeto un_cuadro_de_frecuencias para almacenar los datos en el atributo de lista fecuencias_rel_acum
        self.un_cuadro_de_frecuencias.set_frecuencias_relat_acu(frecuencias_rel_acum)
        
        