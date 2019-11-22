# TT arritmia 2018-B034 predicción y clasificación de arritmias cardiacas.
Este trabajo terminal fue realizado para un trabajo terminal de la Escuela Superior de Cómputo (ESCOM) del Instituto Politécnico Nacional (IPN).
La idea es implementar dos modelos de inteligencia artificial para clasificar arritmias cardiacas con información de un ECG o la imagen del mismo.
## Comenzando 🚀

Para crear una copia del repositorio ejecuta en la terminal:

```
git clone https://github.com/Huitzoo/tt_arrhythmias_detection.git
```

### Pre-requisitos 📋
Para correr el proyecto, es necesario tener una versión de python >= 3 y tener instalado pip para descargar bibliotecas de python.
Si eres experimentado ejecuta:

```
pip install -r requirements.txt
```
Si no lo eres, ejecuta da click en sara.sh para instalar los paquetes y correr el proyecto.

Debes descargar los archivos del modelo de cnn en las url debajo y guardarlos en la carpeta keras_model.
```
Modelo json para keras:
https://tt-documentation-arritmias.s3-us-west-2.amazonaws.com/cnn/model.json
```
```
Pesos del modelo:
https://tt-documentation-arritmias.s3-us-west-2.amazonaws.com/cnn/weights_cnn.h5
```

### Instalación 🔧

Para correr el proyecto, si tienes experiencia ejecuta:
```
pytho3 manage.py runserver
```
Sino, da click en sara.sh para poder correr el proyecto

Para entrar a la aplicación, abres el navegador e ingresas a localhost:8000
