# CRUD con Django Rest Framework y script para consolidar resultados electorales

Esta aplicación es un CRUD sobre un modelo de usuarios y geolocalización por ciudad y dirección.

## Pasos requeridos para inicializar la aplicación

1.  Es recomendado usar **Python 3.7** o una versión mayor
2.  Instala los paquetes que están en el archivo **requirements.txt** usando el comando
    `pip install -r requirements.txt`
3.  Ejecuta `python manage.py makemigrations`
4.  Ejecuta `python manage.py migrate`
5.  Ejecuta `python manage.py runserver`
  
# CRUD
## Para crear un usuario

-  Abre en el navegador Web <http://localhost:8000/api/create>
   o <http://127.0.0.1:8000/api/create>
 
## Para listar los usuarios

-  Abre en el navegador Web <http://localhost:8000/api/list>
   o <http://127.0.0.1:8000/api/list>

## Para editar un usuario

-  Abre en el navegador Web <http://localhost:8000/api/update/1>
   o <http://127.0.0.1:8000/api/update/1>
 
## Para eliminar un usuario

-  Abre en el navegador Web <http://localhost:8000/api/1/delete>
   o <http://127.0.0.1:8000/api/1/delete>
 
## Consulta a la API Geocoding por ciudad y dirección los usuarios con la latitud y longitud en null

-  Abre en el navegador Web <http://localhost:8000/api/geocoding_base>
   o <http://127.0.0.1:8000/api/geocoding_base>
   
# Script para consolidar resultados electorales
- Se corre el archivo consolidate.py con el comando `python consolidate.py` para generar el consolidado por *candidato*,
  para generar consolidados por *partido*, *puesto*, *mpio* y *dept* solo hay que descomentar las lineas. 
 