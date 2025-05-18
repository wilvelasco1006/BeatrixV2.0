# Beatrix Statistics 📊

## 🔍 Descripción general

**Beatrix** es una herramienta de análisis estadístico desarrollada completamente en **Python puro**, sin necesidad de librerías externas. Diseñada para procesar grandes conjuntos de datos desde la consola, ofrece un análisis estadístico completo con visualizaciones en formato texto.

---

## ✨ Características principales

### 📁 Procesamiento de datos
- **Importación desde CSV**: Permite analizar grandes volúmenes de datos provenientes de archivos `.csv` de bases de datos meteorológicas.
- **Análisis multicolumna**: Soporta hasta **6 columnas** independientes de forma simultánea de esas bases de datos.
- **Compatibilidad de datos**: Capaz de manejar distintos tipos de datos numéricos.

### 📈 Análisis estadístico

#### 📍 Medidas de tendencia central
- Cálculo de **media**, **mediana** y **moda**.
- Determinación de **cuartiles** (Q1, Q2, Q3).

#### 📏 Medidas de dispersión
- **Rango** y **rango intercuartílico**.
- **Varianza** y **desviación estándar**.
- **Cálculo de percentiles**.

#### 📚 Teoremas estadísticos aplicados
- **Teorema de Chebyshev**: Estimación de porcentajes entre rangos de desviaciones estándar.
- **Regla empírica**: Para distribuciones normales.

### 🎨 Visualizaciones en texto
- **Tablas de frecuencia**: Con intervalos personalizables.
- **Diagramas de barras**: Para frecuencias absolutas y relativas.
- **Diagramas de caja (boxplot)**: Visualiza cuartiles y valores atípicos.
- **Gráficos de ojiva**: Representan frecuencias acumuladas.
- **Gráficos circulares**: Muestran proporciones de los datos.
- **Visualizaciones del Teorema de Chebyshev**: Distribuciones estadísticas en texto.

### 💾 Persistencia de datos
- **Generación automática de informes**: Todos los resultados se guardan en archivos `.txt`.
- **Personalización del archivo de salida**: El usuario define el nombre del archivo que se genera en la raíz del proyecto.

---

## 🖥️ Interfaz por consola

### Inicio del programa
Aquí se define el nombre del archivo `.txt` que registrará toda tu sesión de análisis:

![Pantalla inicial](/BeatrixV2.0/img/Beatrix-init.png)

### Menú principal
Desde esta pantalla puedes elegir qué tipo de análisis deseas realizar:

![Menú principal](/BeatrixV2.0/img/Beatrix-menu.png)

---

## 🚀 ¿Cómo usar Beatrix?

1. Clona este repositorio en tu máquina local.
2. Abre la carpeta donde lo guardaste.
3. Ejecuta el archivo `main.py`.
4. Sigue las instrucciones para cargar tu archivo `.csv`.
5. Selecciona las columnas de datos que deseas analizar.
6. Elige la operación estadística que quieras realizar.
7. Visualiza los resultados tanto en la consola como en el archivo `.txt` generado automáticamente.

> ⚠️ **Importante**: Actualmente, Beatrix está diseñada exclusivamente para analizar **cuatro archivos específicos de bases de datos meteorológicas** incluidos en este repositorio. Estos datasets contienen **miles de datos**, por lo que el programa ha sido optimizado para trabajar únicamente con ellos.  
>  
> Si intentas cargar un archivo diferente, es posible que el programa no funcione correctamente.

📌 Sin embargo, **se espera seguir desarrollando Beatrix** para que en futuras versiones acepte **cualquier archivo `.csv`** con datos separados por comas, incluyendo aquellos ingresados manualmente.  
👥 El proyecto está **abierto a colaboración**, así que si deseas contribuir con mejoras, soporte para más formatos de archivo o nuevas funcionalidades, ¡eres bienvenido!

---

## ❓¿Necesitas ayuda?

¡No te preocupes! Al clonar el repositorio, recibirás un **manual paso a paso** que te guiará en el uso de Beatrix. Además, incluimos **bases de datos meteorológicas funcionales** para que puedas empezar a practicar de inmediato. Suerte en tu análisis.
