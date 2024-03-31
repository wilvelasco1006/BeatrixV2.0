from Cuadro_de_frecuencias import Cuadro_de_frecuencias_datos_individuales as cuadro_de_frecuencias

class Controlador_vista_cuadro_de_frecuencias_intervalos():
    #Atributos
    un_cuadro_de_frecuencias= cuadro_de_frecuencias()
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass


    #Metodo para llenar una lista con todos los datos para analizar
    def ingresar_y_almacenar_todos_los_datos(self):
        continuar= 1
        todos_los_datos= list()
        
        while(continuar== 1):
            dato=int(input("Por favor numeros los datos que desee analizar:  "))
            todos_los_datos.append(dato)
            continuar= int(input("\nDesea agregar otro dato? 1.Si  2.No\n"))
            while (continuar<1 or continuar>2):
                continuar= int(input("Se ingresó un numero distinto a  1.Si  2.No  Por favor inténtelo de nuevo\n"))
        
        #Aquí- estoy llenando el atributo lista todos_los_datos del objeto cuadro de frecuencias
        self.un_cuadro_de_frecuencias.set_todos_los_datos(todos_los_datos)
        
        #Llamado al metodo determinar_la_cantidad_de_intervalos_a_crear para pedirle al usuario que ingrese la cantidad de intervalos
        #En los que quiere dividir la información
        self.determinar_la_cantidad_de_intevalos_a_crear(todos_los_datos)
      
        
    #Metodo para pedirle al usuario que digite la cantidad de intervalos en la que quiere visualizar la información
    def determinar_la_cantidad_de_intevalos_a_crear(self, todos_los_datos):
        num_intervalos= int(input("Por favor la cantidad de intervalos para evaluar los datos(de 5 a 10): "))
        while num_intervalos<5 or num_intervalos>10:
            num_intervalos= int(input("Por favor la cantidad de intervalos para evaluar los datos(DE 5 A 10): "))
            
        #Llamado al metodo determinar_el_ancho_de_cada_intervalo para decifrar la cantidad de elementos que se encontrarán en el rango de cada
        #intervalo    
        self.determinar_el_ancho_de_cada_intervalo(todos_los_datos, num_intervalos)
    
    
    #Método para  determinar el ancho de cada intervalo con base a restar el numero_mayor con el numero_menor y dividir todo entre el numero de intervalos
    def determinar_el_ancho_de_cada_intervalo(self, todos_los_datos, num_intervalos):
        numero_mas_pequeno= min(todos_los_datos)
        numero_mas_grande=max(todos_los_datos)
        ancho_intervalos= round((numero_mas_grande- numero_mas_pequeno)/num_intervalos)
        
        
        #Llamado al metodo determinar_frecuencias_en_grados para continuar con la recoleccion de las frecuencias
        self.determinar_intervalos(ancho_intervalos, num_intervalos)
       
        
    #Metodo para hacer la lista de los intervalos que se van a crear, aunque la lista es visual, de tipo string
    def determinar_intervalos(self, ancho_intervalos,num_intervalos ):
        todos_los_datos=self.un_cuadro_de_frecuencias.get_todos_los_datos()
        intervalos= list()
        menor= (min(todos_los_datos) -2)
        mayor= (menor + ancho_intervalos)
        
        #ciclo para rellenar la lista intervalos con los mensajes de los intervalos que se evaluaran en un rato
        for i in range(num_intervalos):
            intervalo= str(menor),"-",str(mayor)
            intervalos.append(intervalo)
            menor+=(ancho_intervalos + 1)
            mayor+= (ancho_intervalos + 1)
            
        
        self.un_cuadro_de_frecuencias.set_datos_para_evaluar(intervalos)
        
        #Llamado al metodo determinar_la_frecuencia_de_aparicion_de_los_intervalos para continuar con la recoleccion de las frecuencias
        self.determinar_la_frecuencia_de_aparicion_de_los_intervalos(todos_los_datos,ancho_intervalos, num_intervalos)
        
        
    #Metoto para determinar la cantidad de veces que un numero se encuentra en los rangos de cada intervalo 
    def determinar_la_frecuencia_de_aparicion_de_los_intervalos(self,todos_los_datos, ancho_intervalos, num_intervalos):
        frecuencia_intervalos= list()
        iteracion=0
        menor= (min(todos_los_datos) -2)
        mayor= (menor + ancho_intervalos)
        
        #ciclo para determinar si un numero de todos los ingresados se encuentra en el rango de los intervalos
        while iteracion<= (num_intervalos-1):
            frecuencia=0
            for i in range(len(todos_los_datos)):
                if (todos_los_datos[i]>=menor and todos_los_datos[i]<=mayor):
                    frecuencia+=1
                    
            frecuencia_intervalos.append(frecuencia)
            menor+=(ancho_intervalos + 1)
            mayor+= (ancho_intervalos + 1)
            iteracion +=1
            
        #Se envia la lista frecuencias_de_aparicion al objeto un_cuadro_de_frecuencia en el atributo frecuencia_de_aparicion
        self.un_cuadro_de_frecuencias.set_frecuencias_de_apari(frecuencia_intervalos)
        


        
        