class Cuadro_de_frecuencias_datos_individuales:
    #atributos
    
    #Aquí estoy diciendo que los atributos son listas o arreglos, solo que en python de por sí los arreglos son dinámicos
    todos_los_datos=[]
    datos_para_evaluar=[]
    frecuencias_de_apari=[]
    frecuencias_relativas=[]
    frecuencias_relat_acu=[]
    frecuencias_porcentuales=[]
    frecuencias_porcent_acu=[]
    frecuencias_en_grados=[]
    
    
    #Metodos
    #Metodo constructor    
    def __init__(self):
        pass
    
    #Metodos get//////////////////////////////////////
    def get_todos_los_datos(self):
        return self.todos_los_datos
    
    def get_datos_para_evaluar(self):
       return self.datos_para_evaluar
    
    def get_frecuencias_de_apari(self):
        return self.frecuencias_de_apari
    
    def get_frecuencias_relativas (self):
        return self.frecuencias_relativas
    
    def get_frecuencias_relat_acu (self):
        return self.frecuencias_relat_acu
    
    def get_frecuencias_porcentuales (self):
        return self.frecuencias_porcentuales
    
    def get_frecuencias_porcent_acu (self):
        return self.frecuencias_porcent_acu
    
    def get_frecuencias_en_grados (self):
        return self.frecuencias_en_grados

    
    #Metodos set//////////////////////////////////////
    
    #Este metodo va a permitir pasarle los datos que vienen en la lista _todos_los_datos al atributo de tipo lista
    # todos_los_datos a través de un metodo for que va a iterar en la lista entrante
    def set_todos_los_datos(self, _todos_los_datos):
        for dato in _todos_los_datos:
            self.todos_los_datos.append(dato) 
    
    #Metodo para rellenar el atributo datos_para_evaluar con base a la lista entrante _datos_para_evaluar
    #Este metodo tambien almacenará los intervalos en la clase Cuadro de_frecuencias_intervalos
    def set_datos_para_evaluar(self, _datos_para_evaluar):
        for dato in _datos_para_evaluar:
            self.datos_para_evaluar.append(dato)
            
    #Metodo para rellenar el atributo frecuencias_de_apari con base a la lista entrante _frecuencias_de_apari        
    def set_frecuencias_de_apari(self, _frecuencias_de_apari):
        for dato in _frecuencias_de_apari:
            self.frecuencias_de_apari.append(dato)
        
   #Metodo para rellenar el atributo frecuencias_relativas con base a la lista entrante _frecuencias_relativas        
    def set_frecuencias_relativas(self, _frecuencias_relativas):
        for dato in _frecuencias_relativas:
            self.frecuencias_relativas.append(dato)
    
    #Metodo para rellenar el atributo frecuencias_relat_acu con base a la lista entrante _frecuencias_relat_acu       
    def set_frecuencias_relat_acu(self, _frecuencias_relat_acu):
        for dato in _frecuencias_relat_acu:
            self.frecuencias_relat_acu.append(dato)

    #Metodo para rellenar el atributo set_frecuencias_procentuales con base a la lista entrante _set_frecuencias_procentuales      
    def set_frecuencias_procentuales(self, _frecuencias_porcentuales):
        for dato in _frecuencias_porcentuales:
            self.frecuencias_porcentuales.append(dato)

    #Metodo para rellenar el atributo frecuencias_porcent_acu con base a la lista entrante frecuencias_porcent_acu       
    def set_frecuencias_porcent_acu(self, _frecuencias_porcent_acu):
        for dato in _frecuencias_porcent_acu:
            self.frecuencias_porcent_acu.append(dato)

   #Metodo para rellenar el atributo frecuencias_en_grados con base a la lista entrante _frecuencias_en_grados  
    def set_frecuencias_en_grados(self, _frecuencias_en_grados):
        for dato in _frecuencias_en_grados:
            self.frecuencias_en_grados.append(dato)
    
    def mostrar_la_tabla_de_frecuencias(self):
        tabla=""
        
        #Ciclo para mostrar la tabla de frecuencia
        for i in range(len(self.datos_para_evaluar)):
           tabla+= " "+str(self.datos_para_evaluar[i])+ "\t"+ str(self.frecuencias_de_apari[i])+ "    "+ str(self.frecuencias_relativas[i])+ "   "+ str(self.frecuencias_relat_acu[i])+"\t "+ str(self.frecuencias_porcentuales[i])+ "\t   "+ str(self.frecuencias_porcent_acu[i])+ "   "+ str(self.frecuencias_en_grados[i])+  "\n"
        
        return tabla

    
    