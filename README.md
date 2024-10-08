# Asignación de Seminarios - CSV Processor

## Introducción

Este proyecto en Python tiene como objetivo procesar datos de encuestas provenientes de un archivo CSV, donde los estudiantes ordenan una lista de seminarios según su preferencia. El script asigna a los estudiantes a los seminarios de acuerdo con su orden de preferencia y la capacidad de los seminarios. Finalmente, genera un archivo Excel (`asignacion_seminarios.xlsx`) con las asignaciones.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Dependencias](#dependencias)
- [Configuración](#configuración)
- [Ejemplos](#ejemplos)
- [Licencia](#licencia)

# Instalación

Para instalar las dependencias necesarias, puedes ejecutar el siguiente comando en la terminal. El código incluye una función que instala automáticamente los paquetes requeridos usando `pip`:

pip install pandas numpy chardet xlsxwriter openpyxl
O puedes ejecutar el script y los paquetes se instalarán automáticamente si no los tienes.

# Uso

Coloca el archivo CSV en la ruta especificada en el código. El archivo debe tener los siguientes campos clave:

Nombre Completo
Ordene los seminarios desde el que más llamó su atención al que menos atrajo su interés
El script detecta automáticamente la codificación del archivo CSV para garantizar su correcta lectura.

Luego, procesa el archivo y elimina varias columnas no necesarias, como correos electrónicos, horas de inicio y fin, entre otros.

El script divide las preferencias de seminarios en columnas separadas, asigna a los estudiantes a seminarios y distribuye equitativamente según la capacidad.

Finalmente, genera un archivo Excel asignacion_seminarios.xlsx con las asignaciones por cada seminario.

# Ejecución

Puedes ejecutar el script de la siguiente manera:

Copiar código
python script.py

# Características

Detección de codificación: Utiliza la librería chardet para detectar automáticamente la codificación del archivo CSV.
Preprocesamiento de datos: Elimina columnas irrelevantes y organiza los datos de preferencia de seminarios en columnas separadas.
Asignación de estudiantes a seminarios: Asigna a los estudiantes a seminarios de manera equitativa, respetando el orden de preferencia.
Exportación a Excel: Crea un archivo Excel con las asignaciones de estudiantes por seminario, eliminando filas vacías.

# Dependencias
El proyecto depende de las siguientes librerías:

pandas: Para manipulación y análisis de datos.
numpy: Para cálculos numéricos.
chardet: Para detectar la codificación de archivos.
xlsxwriter: Para la creación de archivos Excel.
openpyxl: Para la manipulación de archivos Excel.

# Configuración

Archivo CSV
Asegúrate de que tu archivo CSV esté codificado correctamente. El script intentará detectar la codificación automáticamente, pero si el archivo no tiene la codificación esperada, asegúrate de que sea compatible con ISO-8859-1 o ajusta el parámetro de codificación en la lectura del CSV.

# Ejemplos
Ejemplo de entrada
Un ejemplo del archivo CSV que el código procesaría debe tener una estructura similar a esta:

csv
Copiar código
Nombre Completo;Ordene los seminarios desde el que mas llamo su atención al que menos atrajo su interés;...
Juan Pérez;Seminario 1;Seminario 2;Seminario 3;...
María Gómez;Seminario 2;Seminario 1;Seminario 3;...
...
Ejemplo de salida
El script genera un archivo asignacion_seminarios.xlsx con hojas separadas para cada seminario y los estudiantes asignados.

# Licencia
Este proyecto se distribuye bajo la licencia MIT.
