
class Medidas_de_variabilidad:
    #atributos
    media_muestral=None 
    rango=None
    rango_intercuartico=None
    cuadrado_de_la_desviación_respecto_a_la_medida= list()
    suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida=None
    varianza=None
    desviacion_estandar=None
    num_menor_rango=None
    num_mayor_rango=None
    porcentaje_chevyshev=None
    puntos_z=None
    
    #Metodos
    #Metodo_constructor
    def __init__(self):
        pass
    

    #metodos_get
    
    def get_media_muestral(self):
        return self.media_muestral
        
    def get_rango (self):
        return self.rango

    def get_rango_intercuartico(self):
        return self.rango_intercuartico

    def get_cuadrado_de_la_desviación_respecto_a_la_medida(self):
        return self.cuadrado_de_la_desviación_respecto_a_la_medida

    def get_suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida(self):
        return self.suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida

    def get_varianza(self):
        return self.varianza

    def get_desviacion_estandar(self):
        return self.desviacion_estandar

    def get_num_menor_rango(self):
        return self.num_menor_rango

    def get_num_mayor_rango(self):
        return self.num_mayor_rango

    def get_porcentaje_chevyshev(self):
        return self.porcentaje_chevyshev

    def get_puntos_z(self):
        return self.puntos_z

    #metodos set//////////////////////////////////////////

    def set_media_muestral(self,_media_muestral):
        self.media_muestral= _media_muestral
    

    def set_rango (self,_rango):
        self.rango=_rango

    def set_rango_intercuartico(self,_rango_intercuartico):
        self.rango_intercuartico= _rango_intercuartico

    def set_cuadrado_de_la_desviación_respecto_a_la_medida(self,_cuadrado_de_la_desviación_respecto_a_la_medida):
        for dato in _cuadrado_de_la_desviación_respecto_a_la_medida:
            self.cuadrado_de_la_desviación_respecto_a_la_medida.append(dato)
        
    def set_suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida(self,_suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida):
        self.suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida=_suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida

    def set_varianza(self,_varianza):
        self.varianza=_varianza

    def set_desviacion_estandar(self,_desviacion_estandar):
        self.desviacion_estandar=_desviacion_estandar

    def set_num_menor_rango(self,_num_menor_rango):
        self.num_menor_rango=_num_menor_rango

    def set_num_mayor_rango(self,_num_mayor_rango):
        self.num_mayor_rango=_num_mayor_rango

    def set_porcentaje_chevyshev(self,_porcentaje_chevyshev):
        self.porcentaje_chevyshev=_porcentaje_chevyshev

    def set_puntos_z(self,_puntos_z):
        self.puntos_z=_puntos_z
    
    def mostrar_los_datos_de_las_medidas_de_variabilidad(self,desicion_punt_z):
        pass
