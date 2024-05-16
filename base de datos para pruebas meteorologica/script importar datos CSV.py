import csv

# Ruta del archivo CSV
archivo_csv = "C:\\Users\\felip\\Downloads\\base de datos para pruebas meteorologica\\prueba.csv"

# Lista para almacenar los datos
datos = []

# Abrir el archivo CSV en modo de lectura ('r')
try:
    with open(archivo_csv, mode='r') as file:
        # Crear un objeto reader
        reader = csv.reader(file)
        
        # Leer los datos del archivo CSV fila por fila
        for fila in reader:
            datos.append(fila)
except FileNotFoundError:
    print(f"El archivo {archivo_csv} no fue encontrado.")
except Exception as e:
    print("Ocurrió un error al leer el archivo CSV:", e)

# Mostrar los datos importados
print("Datos importados del archivo CSV:")
#for fila in datos:
#    print(fila)

print (datos)