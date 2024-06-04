
class Medidas_de_tendencia_central:
    #Atributos
    nombre_archivo_final= None
    grafico_seleccionado=None
    media= None
    mediana= None
    moda= None
    cuartil_1=None
    cuartil_2=None
    cuartil_3=None
    cuartil_4=None
    resultado_percentil=None
    
    #Metodos
    #Metodo constructor
    def __init__(self):
        pass
    
    #Metodos get
    
    def get_nombre_archivo_final(self):
        return self.nombre_archivo_final
    
    def get_grafico_seleccionado(self):
        return self.grafico_seleccionado
    
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
    
    
    #Metodos set //////////////////////////////////////////
    
    def set_nombre_archivo_final(self, _nombre_archivo_final):
        self.nombre_archivo_final= _nombre_archivo_final
    
    def set_grafico_seleccionado(self, _grafico_seleccionado):
        self.grafico_seleccionado=_grafico_seleccionado    
    
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

    #metodo para organizar y almacenar todos los datos en una sola variable
    def acomodar_los_datos_para_mostrar(self,):
        datos="Media: "+ str(self.media)+"\nMediana: "+ str(self.mediana)+"\nModa: "+ str(self.moda)+"\n\nCuartil 1: "+ str(self.cuartil_1)+"\nCuartil 2: "+ str(self.cuartil_2)+"\nCuartil 3: "+ str(self.cuartil_3)+"\nCuartil 4: "+ str(self.cuartil_4)+"\n\n"
        
        #retorno de los datos en una sola variable
        return datos