
class Medidas_de_tendencia_central:
    #Atributos
    media= list()
    mediana= list()
    moda= list()
    cuartil_1=0
    cuartil_2=0
    cuartil_3=0
    cuartil_4=0
    datos_en_el_cuartil_1= list()
    datos_en_el_cuartil_2= list()
    datos_en_el_cuartil_3= list()
    datos_en_el_cuartil_4= list()
    resultado_percentil=0
    
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
        self.datos_en_el_cuartil_1= _datos_en_el_cuartil_1

    def set_datos_en_el_cuartil_2(self, _datos_en_el_cuartil_2):
        self.datos_en_el_cuartil_2= _datos_en_el_cuartil_2
    
    def set_datos_en_el_cuartil_3(self, _datos_en_el_cuartil_3):
        self.datos_en_el_cuartil_3= _datos_en_el_cuartil_3
    
    def set_datos_en_el_cuartil_4(self, _datos_en_el_cuartil_4):
        self.datos_en_el_cuartil_4= _datos_en_el_cuartil_4
    
    def set_resultado_percentil(self, _resultado_percentil):
        self.resultado_percentil= _resultado_percentil
        
    def acomodar_los_datos_para_mostrar(self,):
        datos="Media: "+ str(self.media)+"\nMediana: "+ str(self.mediana)+"\nModa: "+ str(self.moda)+"\nCuartil 1"+ str(self.cuartil_1)+"\nCuartil 2"+ str(self.cuartil_2)+"\nCuartil 3"+ str(self.cuartil_3)+"\nCuartil4"+ str(self.cuartil_4)+"\n"
        ciclo=True
        datos_de_los_cuartiles=""
        while (ciclo==True):
            for j in self.datos_en_el_cuartil_1:
                datos_de_los_cuartiles+=j
            
            datos_de_los_cuartiles+="\n"
            
            for k in self.datos_en_el_cuartil_2:
                datos_de_los_cuartiles+=k
                
            datos_de_los_cuartiles+="\n"
            
            for l in self.datos_en_el_cuartil_3:
                datos_de_los_cuartiles+=l
                
            datos_de_los_cuartiles+="\n"
            
            for m in self.datos_en_el_cuartil_4:
                datos_de_los_cuartiles+=m
                
            datos_de_los_cuartiles+="\n"

            ciclo=False
        
        datos+= datos_de_los_cuartiles
        
        datos+="\n"
        
        datos+= str(self.resultado_percentil)
        
        return datos