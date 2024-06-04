from Controlador_vista_cuadro_de_frecuencias_intervalos import Controlador_vista_cuadro_de_frecuencias_intervalos

class menu:
    #Constructor 
    def __init__(self):
        pass
    
    #Metodo para dibujar el menu
    def dibujar (self):
        print ("\033["+"7;30;45"+"m "+'\u250F'+('\u2501')*95+'\u2513'" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                \u2572     \u2571\u203E\u2572     \u2571  \u250C\u2500\u2500\u2500   \u2502    \u250C\u2500\u2500\u2500  \u256D\u2500\u2500\u2500\u256E   \u2571\u203E\u2572   \u2571\u203E\u2572   \u250C\u2500\u2500\u2500                    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                 \u2572   \u2571   \u2572   \u2571   \u251C\u2500\u2500\u2500   \u2502    \u2502     \u2502   \u2502  \u2571   \u2572_\u2571   \u2572  \u251C\u2500\u2500\u2500                    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                  \u2572\u005F\u2571     \u2572\u005F\u2571    \u2514\u2500\u2500\u2500   \u2514\u2500\u2500\u2500 \u2514\u2500\u2500\u2500  \u2570\u2500\u2500\u2500\u256F \u2571           \u2572 \u2514\u2500\u2500\u2500                    \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                       \u2500\u2500\u2500\u252C\u2500\u2500\u2500 \u256D\u2500\u2500\u2500\u256E                                           \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                          \u2502    \u2502   \u2502                                           \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                          \u2502    \u2570\u2500\u2500\u2500\u256F                                           \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                         \u250c\u2500\u2500\u2500\u256E  \u250c\u2500\u2500\u2500    \u2571\u203E\u2572   \u2500\u2500\u2500\u252C\u2500\u2500\u2500 \u250c\u2500\u2500\u2500\u2510  \u2500\u2500\u2500\u252C\u2500\u2500\u2500   \u2572 \u2571                     \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                         \u251C\u2500\u2500\u2500\u2524  \u251C\u2500\u2500\u2500   \u2571 \u2500 \u2572     \u2502    \u2502\u2500\u2500\u2500\u2518     \u2502       \u2573                      \u2503"+" \033[0m")   
        print ("\033["+"7;30;45"+"m "+"\u2503                         \u2514\u2500\u2500\u2500\u256F  \u2514\u2500\u2500\u2500  \u2571     \u2572    \u2502    \u2502  \u2572   \u2500\u2500\u2500\u2534\u2500\u2500\u2500   \u2571 \u2572                     \u2503"+" \033[0m") 
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2523" +('\u2501')*95+"\u252B"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                              POR FAVOR INGRESE EL NOMBRE QUE QUIERA QUE                       \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                               TENGA EL ARCHIVO FINAL CON LOS RESULTADOS                       \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+"\u2503                                                                                               \u2503"+" \033[0m")
        print ("\033["+"7;30;45"+"m "+'\u2517'+('\u2501')*95+'\u251B'+" \033[0m")
        nombre_archivo_final = input("")
        #Creación del archivo .txt que contendrá los resultados de los análisis
        # Abre el archivo en modo append (crea el archivo si no existe) 
        with open(nombre_archivo_final, 'a', encoding='utf-8') as f:
            f.write("" + '\n')
        controlador= Controlador_vista_cuadro_de_frecuencias_intervalos()
        controlador.ingresar_y_almacenar_todos_los_datos(nombre_archivo_final)
        
        
