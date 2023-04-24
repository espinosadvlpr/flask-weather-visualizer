# App meteorológica con Flask

Este repositorio contiene un proyecto Python Flask para visualizar datos climáticos de ciudades específicas.
El proyecto lee los datos de un archivo CSV y utiliza Flask para construir una aplicación web que muestra los datos meteorológicos de las ciudades seleccionadas. Los usuarios pueden interactuar con la aplicación para ver las condiciones meteorológicas. El proyecto incluye herramientas de visualización para ayudar a los usuarios a comprender y analizar mejor los patrones climáticos en las ciudades del dataset.

La aplicación está construida con el framework web Flask de Python y utiliza Bootstrap para el diseño de la interfaz de usuario.

## Descarga del proyecto

Para descargar el proyecto puede clonar este repositorio usando el comando:

```
git clone https://github.com/espinosadvlpr/flask-weather-visualizer.git
```

## Instalación

Para instalar el proyecto, siga estos pasos:

1. Asegurarse de tener Python 3 y MySQL instalado.

3. Instalar las dependencias requeridas usando el archivo requirements.txt. 
Puede hacer esto ejecutando el siguiente comando en su terminal:

```
pip install -r requirements.txt
```

4. Para cargar los datos a MySQL se usará el archivo `upload_data.py`. 
- Antes de ejecutar el script se debe cambiar la configuración en la linea 14 del archivo parala conexión de la base de datos, para esta conexión se debe tener previamente creado un esquema de base de datos. La configuración a editar es la siguiente:
```
'mysql+pymysql://[user]:[password]@127.0.0.1/[database_name]'
```
- Ejecutar el archivo `upload_data.py` usando el siguiente comando:

```
python upload_data.py
```
Si todo funciona correctamente verá el mensaje `Data successfully charged to table datos_meteorologicos.`
 
## Uso

Para iniciar la aplicación, ejecute el siguiente comando en su terminal:

```
python App.py
```

Esto iniciará el servidor de Flask en su máquina local. 
Puede acceder a la aplicación visitando <http://localhost:3000> en su navegador web.

![image](https://user-images.githubusercontent.com/38819699/233885834-e2603e4c-7c3a-42aa-a3f3-647ed36609f8.png)

## Recorrido por la aplicación

Despues de dar en el botón **Comenzar** podemos empezar a navegar en cada una de las preguntas del taller.

**1. ¿Cuál es el promedio de la temperatura y la humedad para cada ciudad?**

![image](https://user-images.githubusercontent.com/38819699/233886407-718ae43c-1e5f-4064-ac4f-510a59ca616d.png)

**2. Mostrar el promedio de la velocidad del viento, la temperatura máxima y mínima de cada ciudad.**

![image](https://user-images.githubusercontent.com/38819699/233886471-576e194d-af41-405e-8496-ae13faaeae37.png)

**3. Pronostico del clima para una ciudad y una fecha determinada.**
- Primero se debe seleccionar la ciudad y la fecha para la cual se desea conocer el pronostico.

![image](https://user-images.githubusercontent.com/38819699/233886576-c8d63eeb-9c2c-4fb7-a958-ef5ce4b36497.png)

- Despues de dar click en el botón **Revisar**, se nos dirige una pagina con los datos del clima para la fecha y la ciudad seleccionadas.

![image](https://user-images.githubusercontent.com/38819699/233887100-97c70f8c-de81-4f82-98e6-06790d911f79.png)

**4. Gráfico de dispersión para una ciudad y una variable determinada.**
- Primero se debe seleccionar la ciudad y la variable para la cual se desea revisar el gráfico de dispersión.

![image](https://user-images.githubusercontent.com/38819699/233887368-72709cd5-7f6d-42a1-89a2-65451ecc4365.png)

- Despues de dar click en el botón **Ver Gráfico**, se nos dirige una pagina con el gráfico para la variable (promediada por fecha) y la ciudad seleccionadas.

![image](https://user-images.githubusercontent.com/38819699/233887854-68696b6b-b353-4989-8787-05cad314fa47.png)

**5. Gráfico de comportamiento de la variable Temperatura para cada ciudad.**

![image](https://user-images.githubusercontent.com/38819699/233888588-fbb126de-bed1-41b4-9231-ce812123a62d.png)


---
`
NOTA: Se pueden realizar contribuciones al proyecto en caso de que alguien desee hacerlo.
`

*Happy coding! :)*
