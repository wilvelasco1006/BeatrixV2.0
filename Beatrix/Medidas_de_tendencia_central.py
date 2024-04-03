
class Medidas_de_tendencia_central:
    #Atributos
    media= None
    mediana= None
    moda= None
    cuartil_1=None
    cuartil_2=None
    cuartil_3=None
    cuartil_4=None
    datos_en_el_cuartil_1= list()
    datos_en_el_cuartil_2= list()
    datos_en_el_cuartil_3= list()
    datos_en_el_cuartil_4= list()
    resultado_percentil=None
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    #Metodos get
    
    def get_media(self):
        return self.media
    
    def get_mediana(self):
        return self.mediana
    
    def get_moda(self):
        return self.moda
    
    def get_cuartil_1(self):
        return self.cuartil_1
    
    def get_cuartil_2(self):
        return self.cuartil_2
    
    def get_cuartil_3(self):
        return self.cuartil_3
    
    def get_cuartil_4(self):
        return self.cuartil_4
    
    def get_datos_en_el_cuartil_1(self):
        return self.datos_en_el_cuartil_1
    
    def get_datos_en_el_cuartil_2(self):
        return self.datos_en_el_cuartil_2
    
    def get_datos_en_el_cuartil_3(self):
        return self.datos_en_el_cuartil_3
    
    def get_datos_en_el_cuartil_4(self):
        return self.datos_en_el_cuartil_4
    
    def get_resultado_percentil(self):
        return self.resultado_percentil
    
    #Metodos set

    def set_media(self, _media):
        self.media=_media
    
    def set_mediana(self, _mediana):
        self.mediana=_mediana
    
    def set_moda(self, _moda):
        self.moda=_moda
    
    def set_cuartil_1(self, _cuartil_1):
        self.cuartil_1= _cuartil_1
    
    def set_cuartil_2(self, _cuartil_2):
        self.cuartil_2= _cuartil_2
    
    def set_cuartil_3(self, _cuartil_3):
        self.cuartil_3= _cuartil_3
    
    def set_cuartil_4(self, _cuartil_4):
        self.cuartil_4= _cuartil_4
    
    def set_datos_en_el_cuartil_1(self, _datos_en_el_cuartil_1):
        for dato in _datos_en_el_cuartil_1:
            self.datos_en_el_cuartil_1.append(dato)

    def set_datos_en_el_cuartil_2(self, _datos_en_el_cuartil_2):
        for dato in _datos_en_el_cuartil_2:
            self.datos_en_el_cuartil_2.append(dato) 
            
    def set_datos_en_el_cuartil_3(self, _datos_en_el_cuartil_3):
        for dato in _datos_en_el_cuartil_3:
            self.datos_en_el_cuartil_3.append(dato) 
    
    def set_datos_en_el_cuartil_4(self, _datos_en_el_cuartil_4):
        for dato in _datos_en_el_cuartil_4:
            self.datos_en_el_cuartil_4.append(dato) 
    
    def set_resultado_percentil(self, _resultado_percentil):
        self.resultado_percentil= _resultado_percentil
        
    def acomodar_los_datos_para_mostrar(self,):
        datos="Media: "+ str(self.media)+"\nMediana: "+ str(self.mediana)+"\nModa: "+ str(self.moda)+"\n\nCuartil 1: "+ str(self.cuartil_1)+"\nCuartil 2: "+ str(self.cuartil_2)+"\nCuartil 3: "+ str(self.cuartil_3)+"\nCuartil 4: "+ str(self.cuartil_4)+"\n\n"
        ciclo=True
        datos_de_los_cuartiles=""
        while (ciclo==True):
            datos_de_los_cuartiles+="Datos_en_el_cuartil_1: "
            for j in self.datos_en_el_cuartil_1:
                datos_de_los_cuartiles+=(str(j)+", ")
            
            datos_de_los_cuartiles+="\nDatos_en_el_cuartil_2: "
            
            for k in self.datos_en_el_cuartil_2:
                datos_de_los_cuartiles+=(str(k)+", ")
                
            datos_de_los_cuartiles+="\nDatos_en_el_cuartil_3: "
            
            for l in self.datos_en_el_cuartil_3:
                datos_de_los_cuartiles+=(str(l)+", ")
                
            datos_de_los_cuartiles+="\nDatos_en_el_cuartil_4: "
            
            for m in self.datos_en_el_cuartil_4:
                datos_de_los_cuartiles+=(str(m)+", ")

            ciclo=False
        
        datos+= datos_de_los_cuartiles+"\n\n"
        
        datos+= "El dato que se encuentra en ese percentil es: "+str(self.resultado_percentil)
        
        return datos