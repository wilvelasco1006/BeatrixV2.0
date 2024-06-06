class Diagrama_de_caja_para_txt:
    #Constructor 
    def __init__(self):
        pass
    def dibujar (self,lista_datos,datos_atipicos, nombre_archivo_final):
        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write("\n\nDiagrama de caja\n\n")
            
        for dato in (lista_datos):
            limite_inferior= dato[0]
            limite_inferior=self.modificador_dibujar_primario (limite_inferior)
            q1=dato[1]
            q1=self.modificador_dibujar_general (q1)
            q2=dato [2]
            q2=self.modificador_dibujar_general (q2)
            q3= dato[3]
            q3=self.modificador_dibujar_general (q3)
            limite_superior= dato[4]
            limite_superior=self.modificador_dibujar_ultimo (limite_superior)
            linea= "".join ([str(limite_inferior),
                            str(q1),
                            str(q2),
                            str(q3),
                            str(limite_superior),])
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write  ("\n\nDiagrama de caja\\n")  
            f.write (" "+"  ________________________________________________________ "+" \n")
            f.write (" "+" |                                                        |"+" \n")
            f.write (" "+" |                                                        |"+" \n")
            f.write (" "+" |    |             _________ _________             |     |"+" \n")
            f.write (" "+" |    |            |         |         |            |     |"+" \n")
            f.write (" "+" |    |            |         |         |            |     |"+" \n")
            f.write (" "+" |    |            |         |         |            |     |"+" \n")
            f.write (" "+" |    |            |         |         |            |     |"+" \n")
            f.write (" "+" |    |             ¯¯¯¯¯¯¯¯¯ ¯¯¯¯¯¯¯¯¯             |     |"+" \n")
            f.write (" "+" |                 |         |         |                  |"+" \n")
            f.write (" "+" |                 |         |         |                  |"+" \n")
            f.write (" "+" |  _______________|_________|_________|_________________ |"+" \n")
            f.write (" " + linea +"\n ")
            f.write (" "+" |  LIMITE        Q1        Q2        Q3        LIMITE    |"+" \n")
            f.write (" "+" | INFERIOR                                    SUPERIOR   |"+" \n")
            f.write (" "+" |________________________________________________________|"+" \n")

        
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write("\nDatos atípicos\n\n")
        
        
        for i in datos_atipicos: # ciclo para mostrar lo datos atipicos
            with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
                f.write(str(i)+ "\n")
    
                     
    
    def modificador_dibujar_general (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje=""+"    "+dato_acomodar+"    "+" "
        elif(len (dato_acomodar) == 2):
            mensaje=" "+"  "+dato_acomodar+"     "+" "
        elif(len (dato_acomodar) == 3):
            mensaje=" "+"   "+dato_acomodar+"  "+" "
        elif(len (dato_acomodar) == 4):
            mensaje=" "+"   "+dato_acomodar+"   "+" "
        elif(len (dato_acomodar) == 5):
            mensaje=" "+"  "+dato_acomodar+"   "+" "
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL PRIMER DATO
    def modificador_dibujar_primario (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje=""+"|    "+ dato_acomodar +"    "+"    "
        elif(len (dato_acomodar) == 2):
            mensaje=""+"|   "+dato_acomodar+"    "+"   "
        elif(len (dato_acomodar) == 3):
            mensaje=""+"|   "+dato_acomodar+"  "+"    "
        elif(len (dato_acomodar) == 4):
            mensaje=""+"    "+dato_acomodar+"   "
        elif(len (dato_acomodar) == 5):
            mensaje=" "+"    "+dato_acomodar+"  "
 
        return (mensaje)
    #SIRVE PARA ACOMODAR EL TAMAÑO DEL ULTIMO DAÑO
    def modificador_dibujar_ultimo (self,dato_acomodar):
        dato_acomodar = str(dato_acomodar)
        if (len (dato_acomodar) == 1):
            mensaje=""+"       "+dato_acomodar+ "    "+" |"+" "
        elif(len (dato_acomodar) == 2):
            mensaje=""+"     "+dato_acomodar+"    "+"| "+""
        elif(len (dato_acomodar) == 3):
            mensaje=""+"       "+dato_acomodar+"   "+" |"+" "
        elif(len (dato_acomodar) == 4):
            mensaje=""+"    "+dato_acomodar+"   "
        elif(len (dato_acomodar) == 5):
            mensaje=" "+"   "+dato_acomodar+"   "


        return (mensaje)
'''ejecutar_9 = accion_9()
lista_datos = [[-2.5, 1.5, 3.5, 5.5, 9.5]]
ejecutar_9.dibujar(lista_datos)'''