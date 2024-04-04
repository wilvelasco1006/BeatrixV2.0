
class Medidas_de_variabilidad:
    #atributos
    todos_los_datos=list()
    rango=None
    rango_intercuartico=None
    media_muestral=None 
    cuadrado_de_la_desviación_respecto_a_la_medida= list()
    suma_del_cuadrado_de_desviaciacion_respecto_a_la_medida=None
    varianza=None
    poblacion_o_muestra=None
    desviacion_estandar=None
    num_menor_rango=None
    num_mayor_rango=None
    porcentaje_chevyshev=None
    numero_puntos_z=None
    puntos_z=None
    
    #Metodos
    #Metodo_constructor
    def __init__(self):
        pass
    

    #metodos_get
    def get_todos_los_datos(self):
        return self.todos_los_datos
    
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
    
    def get_poblacion_o_muestra(self):
        return self.poblacion_o_muestra

    def get_desviacion_estandar(self):
        return self.desviacion_estandar

    def get_num_menor_rango(self):
        return self.num_menor_rango

    def get_num_mayor_rango(self):
        return self.num_mayor_rango

    def get_porcentaje_chevyshev(self):
        return self.porcentaje_chevyshev

    def get_numero_puntos_z(self):
        return self.numero_puntos_z
    
    def get_puntos_z(self):
        return self.puntos_z

    #metodos set//////////////////////////////////////////

    def set_todos_los_datos(self, _todos_los_datos):
        for dato in _todos_los_datos:
            self.todos_los_datos.append(dato)

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

    def set_poblacion_o_muestra(self, _poblacion_o_muestra):
        self.poblacion_o_muestra= _poblacion_o_muestra
    
    def set_desviacion_estandar(self,_desviacion_estandar):
        self.desviacion_estandar=_desviacion_estandar

    def set_num_menor_rango(self,_num_menor_rango):
        self.num_menor_rango=_num_menor_rango

    def set_num_mayor_rango(self,_num_mayor_rango):
        self.num_mayor_rango=_num_mayor_rango

    def set_porcentaje_chevyshev(self,_porcentaje_chevyshev):
        self.porcentaje_chevyshev=_porcentaje_chevyshev

    def set_numero_puntos_z(self, _numero_puntos_z):
        self.numero_puntos_z=_numero_puntos_z

    def set_puntos_z(self,_puntos_z):
        self.puntos_z=_puntos_z
    
    
    #Metodo que me permite almacenar y organizar todos los datos en una sola variable
    def mostrar_los_datos_de_las_medidas_de_variabilidad(self,desicion_punt_z):
        todos_los_datos=self.get_todos_los_datos()
        cuadrado_de_la_desviación_respecto_a_la_medida=self.get_cuadrado_de_la_desviación_respecto_a_la_medida()
        medidas_de_variabilidad= ""
        cuadro_de_medidas_de_variabilidad=""
        
        medidas_de_variabilidad+="El rango es: "+ str(self.get_rango())+"\nEl rango intercuartico es: "+str(self.get_rango_intercuartico())+"\n"
        
        cuadro_de_medidas_de_variabilidad="\n|  Xi  |  media_muestral(Xˉ) | (Xi - Xˉ )^2 | \n"
        
        for i in range(len(todos_los_datos)):
            cuadro_de_medidas_de_variabilidad+= "   "+ str(todos_los_datos[i])+ "                "+ str(self.get_media_muestral())+ "            "  + str(cuadrado_de_la_desviación_respecto_a_la_medida[i])+"\n"
 

        medidas_de_variabilidad+= cuadro_de_medidas_de_variabilidad + "\n"
        
        if(self.get_poblacion_o_muestra() == True):
            medidas_de_variabilidad+= "La varianza poblacional es de: "+ str(self.get_varianza())+"\n"
            
        else:
            medidas_de_variabilidad+= "La varianza muestral es de: "+ str(self.get_varianza())+"\n"
            
        medidas_de_variabilidad+="La desviacion estandar es de: "+ str(self.get_desviacion_estandar())+ "\n el porcentaje en el que se encuentra el rango ingresado anteriormente segun la media muestral es de: "+str(self.get_porcentaje_chevyshev())
        
        medidas_de_variabilidad+="\n El numero "+str(self.get_numero_puntos_z())+", se encuentra a "+ str(self.get_puntos_z()) +", de desviaciones estandar de la media muestral"
        
        #retorno de la variable con todos los datos organizados
        return medidas_de_variabilidad