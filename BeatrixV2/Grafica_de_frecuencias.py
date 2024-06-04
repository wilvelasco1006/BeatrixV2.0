class accion_1:

    #Constructor 
    def __init__(self):
        pass
    #METODO PARA DIBUJAR LA TABLA DE FRECUENCIA
    def dibujar (self,intervalos,nombre_archivo_final):
        
        #CILO UTILIZADO PARA ASIGNARLE LOS VALORES A VARIABLES LAS CUALES SRAN LAS QUE SE VAN A IMPRIMIR
        tamano= self.saber_mayor (intervalos) +1
        self.dibujar_indice (tamano,nombre_archivo_final)
        for intervalo in (intervalos):          
            valor_intervalo= intervalo [0]
            valor_intervalo= self.modificador_dibujar_primario (valor_intervalo,tamano)
            valor_frecuencia=  intervalo [1]
            valor_frecuencia= self.modificador_dibujar_general (valor_frecuencia,tamano)
            valor_fr= intervalo [2]
            valor_fr= self.modificador_dibujar_general (valor_fr,tamano)
            valor_fra= intervalo [3]
            valor_fra= self.modificador_dibujar_general (valor_fra,tamano)
            valor_frp= intervalo [4]
            valor_frp= self.modificador_dibujar_general (valor_frp,tamano)
            valor_frpa= intervalo [5]
            valor_frpa= self.modificador_dibujar_general (valor_frpa,tamano)
            valor_fo= intervalo [6]
            valor_fo= self.modificador_dibujar_ultimo(valor_fo,tamano)
        #JOIN UTILIZADO PARA GUARDAR EL MENSAJE CON CADA UNO DE LOS DATOS SEPARADOS POR UN |
            linea= "".join ([str(valor_intervalo),
                            str(valor_frecuencia),
                            str(valor_fr),
                            str(valor_fra),
                            str(valor_frp),
                            str(valor_frpa),
                            str(valor_fo)])
            with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write(( "|"+" "* tamano +"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|" ) + '\n') 
            print ( "|"+" "* tamano +"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" "* tamano+"|"+" ")
            
            with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write((linea+"\n") + '\n')
            print (linea)
            
            with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write(( " -"+"-"* (tamano*7)+"----- " ) + '\n')
            print ( " -"+"-"* (tamano*7)+"----- "+" ")

    def saber_mayor (self, intervalos):
        tamaño_mayor = 0
        for intervalo in intervalos:
            valor_1 = len(str(intervalo [0]))
            valor_2 = len(str(intervalo [1]))
            valor_3 = len(str(intervalo [2]))
            valor_4 = len(str(intervalo [3]))
            valor_5 = len(str(intervalo [4]))
            valor_6 = len(str(intervalo [5]))
            valor_7 = len(str(intervalo [6]))
            lista_valores = [valor_1,valor_2,valor_3,valor_4,valor_5,valor_6,valor_7]
            nuermo_selecto= max(lista_valores)
            if (nuermo_selecto > tamaño_mayor):
                tamaño_mayor = nuermo_selecto
        return (tamaño_mayor)
    def dibujar_indice (self, tamaño_mayor,nombre_archivo_final):
        if (tamaño_mayor < 12):
            tamaño_mayor = 12

        indice= "".join ([str("| "+"INTERVALO".center(tamaño_mayor-2," ")+" |"),
                            str(" "+"FRECUENCIA".center(tamaño_mayor-2," ")+" | "),
                            str(" "+"FR".center(tamaño_mayor-2," ")+"| "),
                            str(" "+"FRA".center(tamaño_mayor-2," ")+"| "),
                            str(" "+"FRP".center(tamaño_mayor-2," ")+"| "),
                            str(" "+"FRPA".center(tamaño_mayor-2," ")+"| "),
                            str(" "+"F°".center(tamaño_mayor-2," ")+"|")])
        linea_superior = "|"+" "*(tamaño_mayor)+"|"+" "*(tamaño_mayor)+"|"+" "*(tamaño_mayor)+"|"+" "*(tamaño_mayor)+"|"+" "*(tamaño_mayor)+"|"+" "*(tamaño_mayor)+"|"+" "*(tamaño_mayor)+"|"
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write(( " _"+"_"*(tamaño_mayor*7)+"_____ " ) + '\n')        
        print ( " _"+"_"*(tamaño_mayor*7)+"_____ "+" ")
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write( ( linea_superior ) + '\n')
        print ( linea_superior+" ")
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write(( indice ) + '\n')
        print ( indice+" ")
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write(( " -"+"-"*(tamaño_mayor*7)+"----- " )   + '\n')
        print ( " -"+"-"*(tamaño_mayor*7)+"----- "+" ")       
        
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL DATO A AGREGAR EN VALORES DIFERENTES AL PRIMERO Y AL ULTIMO
    def modificador_dibujar_general (self,dato_acomodar,tamano):
        dato_acomodar = str(dato_acomodar)
        if (tamano < 12):
            tamano = 12
        mensaje="\033["+"7;30;45"+"m"+dato_acomodar.center(tamano-1," ")+"|"+" "
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar,tamano):
        dato_acomodar = str(dato_acomodar)
        if (tamano < 12):
            tamano = 12
        mensaje="\033["+"7;30;45"+"m"+" |"+dato_acomodar.center(tamano," ")+"|"+" "
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar,tamano):
        dato_acomodar = str(dato_acomodar)
        if (tamano < 12):
            tamano = 12
        mensaje="\033["+"7;30;45"+"m"+dato_acomodar.center(tamano-1," ")+"|"+" "
        return (mensaje)
#INSTACIA DE LA CLASE ACCION_1
'''
creacion_accion_1 = accion_1()
intervalos = [['jusb',5456456,67867867866,742345345,4564568,123457894855690,123457894855690],['jusb',5456456,67867867866,742345345,4564568,123457894855690,123457894855690]]
creacion_accion_1.dibujar(intervalos)'''