class Teorema_chevyshev_para_txt:
    #Constructor 
    def __init__(self):
        pass
    def dibujar (self,lista_datos, nombre_archivo_final):
        for dato in (lista_datos):
            x_3s= dato[0]
            x_3s=self.modificador_dibujar_primario (x_3s)
            x_2s=dato[1]
            x_2s=self.modificador_dibujar_general (x_2s)
            x_1s=dato [2]
            x_1s=self.modificador_dibujar_general (x_1s)
            x= dato[3]
            x=self.modificador_dibujar_general (x)
            x__s= dato[4]
            x__s=self.modificador_dibujar_general (x__s)
            x__2s= dato[5]
            x__2s=self.modificador_dibujar_general (x__2s)
            x__3s = dato [6]
            x__3s=self.modificador_dibujar_ultimo (x__3s)
            linea= "".join ([str(x_3s),
                            str(x_2s),
                            str(x_1s),
                            str(x),
                            str(x__s),
                            str(x__2s),
                            str(x__3s)])
            
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write (""+"  ____________________________________________________ "+" \n")
            f.write (""+" |                                                    |"+" \n")
            f.write (""+" |                                                    |"+"\n ")
            f.write (""+" |                      _______                       |"+"\n ")
            f.write (""+" |                     /   |   \                      |"+" \n")
            f.write (""+" |                ____/    |    \____                 |"+"\n ")
            f.write (""+" |               / |       |       | \                |"+"\n ")
            f.write (""+" |              /  |       |       |  \               |"+"\n ")
            f.write (""+" |         ____/   | 34%   |  34%  |   \____          |"+" \n")
            f.write (""+" |        /|       |       |       |       |\         |"+" \n")
            f.write (""+" |  _____/ | 13.5% |       |       | 13.5% | \_____   |"+"\n ")
            f.write (""+" | / | 24% |       |       |       |       | 24% | \  |"+"\n ")
            f.write (""+"  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+" \n")
            f.write (""+linea+" ")
            f.write (""+" |                  <------ ------>                   |"+" \n")
            f.write (""+" |                    EL 68% DENTRO                   |"+" \n")
            f.write (""+" |                     1 DESVIACION                   |"+" \n")
            f.write (""+" |                      ESTANDAR                      |"+"\n ")
            f.write (""+" |                                                    |"+"\n ")
            f.write (""+" |           <-------------  ------------->           |"+"\n ")
            f.write (""+" |                    EL 95% DENTRO                   |"+" \n")
            f.write (""+" |                      2 DESVICIONES                 |"+"\n ")
            f.write (""+" |                       ESTANDAR                     |"+" \n")
            f.write (""+" |    <--------------------    ----------------->     |"+" \n")
            f.write (""+" |                    EL 97% DE TODOS                 |"+" \n")
            f.write (""+" |                    LOS DATOS ESTAN                 |"+" \n")
            f.write (""+" |                DENTRO DE 3 DESVIACIONES            |"+" \n")
            f.write (""+" |                       ESTANDAR                     |"+" \n")
            f.write (""+" |                                                    |"+"\n ")
            f.write (""+"  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "+"\n")
    
                     
    
    def modificador_dibujar_general (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje=""+"  "+dato_acomodar+"   "+" "
        elif(len (dato_acomodar) == 2):
            mensaje=""+" "+dato_acomodar+"  "+" "
        elif(len (dato_acomodar) == 3):
            mensaje=""+" "+dato_acomodar+" "+" "
        elif(len (dato_acomodar) == 4):
            mensaje=""+"   "+dato_acomodar+"   "+" "
        elif(len (dato_acomodar) == 5):
            mensaje=""+"  "+dato_acomodar+"   "+" "
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje=""+"|   "+ dato_acomodar +"    "
        elif(len (dato_acomodar) == 2):
            mensaje=""+"|  "+dato_acomodar+"    "
        elif(len (dato_acomodar) == 3):
            mensaje=""+"| "+dato_acomodar+"    "
        elif(len (dato_acomodar) == 4):
            mensaje=""+"    "+dato_acomodar+"   "
        elif(len (dato_acomodar) == 5):
            mensaje=""+"    "+dato_acomodar+"  "
 
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje=""+"    "+dato_acomodar+ "   "+" |"+" "
        elif(len (dato_acomodar) == 2):
            mensaje=""+"    "+dato_acomodar+"  "+" | "+""
        elif(len (dato_acomodar) == 3):
            mensaje=""+"    "+dato_acomodar+" "+" |"+" "
        elif(len (dato_acomodar) == 4):
            mensaje=""+"    "+dato_acomodar+"   "
        elif(len (dato_acomodar) == 5):
            mensaje=""+"   "+dato_acomodar+"   "


        return (mensaje)
    
'''ejecutar_8 = accion_8()
lista_datos =  [['19.04', '10.32', '-1.6', '7.12', '15.84', '24.56', '33.28']]
ejecutar_8.dibujar(lista_datos)'''