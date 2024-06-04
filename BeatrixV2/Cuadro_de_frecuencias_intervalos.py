class Cuadro_de_frecuencias_intervalos:
    #atributos
    
    #Aquí estoy diciendo que los atributos son listas o arreglos, solo que en python de por sí los arreglos son dinámicos
    nombre_archivo_final= None
    grafico_seleccionado=None
    numero_lista=None
    ver_grafico_num=None
    datos_temperatura_interior=[]
    datos_humedad_interior=[]
    datos_temperatura_exterior=[]
    datos_humedad_exterior=[]
    datos_presion_relativa=[]
    datos_presion_absoluta=[]
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
    def get_nombre_archivo_final(self):
        return self.nombre_archivo_final
    
    def get_grafico_seleccionado(self):
        return self.grafico_seleccionado
    
    def get_datos_temperatura_interior(self):
        return self.datos_temperatura_interior
    
    def get_datos_humedad_interior(self):
        return self.datos_humedad_interior
    
    def get_datos_temperatura_exterior(self):
        return self.datos_temperatura_exterior
    
    def get_datos_humedad_exterior(self):
        return self.datos_humedad_exterior
    
    def get_datos_presion_relativa(self):
        return self.datos_presion_relativa
    
    def get_datos_presion_absoluta(self):
        return self.datos_presion_absoluta
    
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

    def get_numero_lista(self):
        return self.numero_lista
    
    #Metodos set//////////////////////////////////////
    def set_nombre_archivo_final(self, _nombre_archivo_final):
        self.nombre_archivo_final= _nombre_archivo_final

    def set_grafico_seleccionado(self, _grafico_seleccionado):
        self.grafico_seleccionado=_grafico_seleccionado
    
    #Este metodo va a permitir pasarle los datos que vienen en la lista _todos_los_datos al atributo de tipo lista
    # todos_los_datos a través de un metodo for que va a iterar en la lista entrante
    def set_datos_temperatura_interior(self, _datos_temperatura_interior):
        for dato in _datos_temperatura_interior:
            self.datos_temperatura_interior.append(dato) 
            
            
    def set_datos_humedad_interior(self, _datos_humedad_interior):
        for dato in _datos_humedad_interior:
            self.datos_humedad_interior.append(dato)
            
            
    def set_datos_temperatura_exterior(self, _datos_temperatura_exterior):
        for dato in _datos_temperatura_exterior:
            self.datos_temperatura_exterior.append(dato)


    def set_datos_humedad_exterior(self, _datos_humedad_exterior):
        for dato in _datos_humedad_exterior:
            self.datos_humedad_exterior.append(dato)
      
            
    def set_datos_presion_relativa(self, _datos_presion_relativa):
        for dato in _datos_presion_relativa:
            self.datos_presion_relativa.append(dato)
   
            
    def set_datos_presion_absoluta(self, _datos_presion_absoluta):
        for dato in _datos_presion_absoluta:
            self.datos_presion_absoluta.append(dato)
    
    
    #Metodo para rellenar el atributo datos_para_evaluar con base a la lista entrante _datos_para_evaluar
    def set_datos_para_evaluar(self, _datos_para_evaluar):
        self.datos_para_evaluar=[]
        for dato in _datos_para_evaluar:
            self.datos_para_evaluar.append(dato)
            
    #Metodo para rellenar el atributo frecuencias_de_apari con base a la lista entrante _frecuencias_de_apari        
    def set_frecuencias_de_apari(self, _frecuencias_de_apari):
        self.frecuencias_de_apari=[]
        for dato in _frecuencias_de_apari:
            self.frecuencias_de_apari.append(dato)
        
   #Metodo para rellenar el atributo frecuencias_relativas con base a la lista entrante _frecuencias_relativas        
    def set_frecuencias_relativas(self, _frecuencias_relativas):
        self.frecuencias_relativas=[]
        for dato in _frecuencias_relativas:
            self.frecuencias_relativas.append(dato)
    
    #Metodo para rellenar el atributo frecuencias_relat_acu con base a la lista entrante _frecuencias_relat_acu       
    def set_frecuencias_relat_acu(self, _frecuencias_relat_acu):
        self.frecuencias_relat_acu=[]
        for dato in _frecuencias_relat_acu:
            self.frecuencias_relat_acu.append(dato)

    #Metodo para rellenar el atributo set_frecuencias_procentuales con base a la lista entrante _set_frecuencias_procentuales      
    def set_frecuencias_procentuales(self, _frecuencias_porcentuales):
        self.frecuencias_porcentuales=[]
        for dato in _frecuencias_porcentuales:
            self.frecuencias_porcentuales.append(dato)

    #Metodo para rellenar el atributo frecuencias_porcent_acu con base a la lista entrante frecuencias_porcent_acu       
    def set_frecuencias_porcent_acu(self, _frecuencias_porcent_acu):
        self.frecuencias_porcent_acu=[]
        for dato in _frecuencias_porcent_acu:
            self.frecuencias_porcent_acu.append(dato)

   #Metodo para rellenar el atributo frecuencias_en_grados con base a la lista entrante _frecuencias_en_grados  
    def set_frecuencias_en_grados(self, _frecuencias_en_grados):
        self.frecuencias_en_grados=[]
        for dato in _frecuencias_en_grados:
            self.frecuencias_en_grados.append(dato)
            
    def set_numero_lista(self, num):
        self.numero_lista=num
    
    def mostrar_la_tabla_de_frecuencias(self):
        tabla=[]
        
        
        for i in range(len(self.datos_para_evaluar)):
            tabla.append([self.datos_para_evaluar[i], self.frecuencias_de_apari[i],self.frecuencias_relativas[i],self.frecuencias_relat_acu[i],self.frecuencias_porcentuales[i],self.frecuencias_porcent_acu[i],self.frecuencias_en_grados[i]])
        
        
        '''tabla=""
        #Ciclo para mostrar la tabla de frecuencia
        if (desicion == True):
            for i in range(len(self.datos_para_evaluar)):
                tabla += "   "+str(self.datos_para_evaluar[i])+ "      "+ str(self.frecuencias_de_apari[i])+ "      "+ str(self.frecuencias_relativas[i])+ "    "+ str(self.frecuencias_relat_acu[i])+"     "+ str(self.frecuencias_porcentuales[i])+ "     "+ str(self.frecuencias_porcent_acu[i])+ "    "+ str(self.frecuencias_en_grados[i])+  "\n"
        
        else:
            for i in range(len(self.datos_para_evaluar)):
            
                tabla += str(self.datos_para_evaluar[i])+ "         "+ str(self.frecuencias_de_apari[i])+ "      "+ str(self.frecuencias_relativas[i])+ "       "+ str(self.frecuencias_relat_acu[i])+"      "+ str(self.frecuencias_porcentuales[i])+ "     "+ str(self.frecuencias_porcent_acu[i])+ "     "+ str(self.frecuencias_en_grados[i])+  "\n"
'''
        return tabla