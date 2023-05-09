# Orange-Clasification 🍊🤖️
El proyecto consiste en la clasificación de naranjas por calibre, en el siguiente repositorio se encuentra por una parte el codigo de OpenCV para la detección y clasifación de dichas naranjas.
Por otro lado se encuentra el codigo de robot studio, donde se ha realizado una simulación del que sería el proceso real de clasifación con el robot Scara.

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/carbonto/Orange-Clasification/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/carbonto/Orange-Clasification/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

## 📝Indice
- [Intalación](#instalacion)
- [Segmentación OpenCV](#segmentacion)
- [Simulación RobotStudio](#robot)
- [Pruebas realizadas](#pruebas)
- [Conclusiones y trabajo futuro](#conclusiones)
- [Autores](#autores)

### Instalación 🔧 <a name = "instalacion"> </a>
Para realizar pruebas y test en el proyecto realizado es necesaria la instalación de diversas herramientas:
- Instalación de [Robot Studio](https://new.abb.com/products/robotics/es/robotstudio)
- Instalación de [Python 3](https://www.python.org/downloads/)
- Instalación de [Pip](https://pypi.org/)
- Instalación de [Open CV](https://opencv.org/)
```
pip install opencv-python
```

## Segmentación OpenCV <a name = "segmentacion"> </a>
Dentro de la carpeta Orange-Segmentation se encuentran diversos archivos que nos ayudarán al proceso de segmetanción de las naranjas. Primero tenemos el script orange_radius.py el cual convierte a HSV, segmenta los objetos de color naranja y saca el radio del mismo.
```
python3 orange_radius.py

```
Otro script implementado es orange_radius_vid.py que realiza el mismo proceso que el anterior pero para videos como pueden ser lo videos obtenidos con la camara del robot para su procesamiento.

```
python3 orange_radius_vid.py

```
Las pruebas realizadas con la segmentación se encuentran en el siguiente apartado [Pruebas realizadas](#pruebas)

## Simulación Robot Studio <a name = "robot"> </a>


## Pruebas realizadas <a name = "pruebas"> </a>
Para probar la segmentación y detección de radio de las naranjas se ha creado un script llamado evaluate.sh el cual ejecutar varias veces orange_radius.py con las distintas imagenes de prueba y se ven los resultados obtenidos

```
./evaluate.sh

````

## Conclusiones y trabajo futuro <a name = "conclusiones"> </a>


## ✍️ Autores <a name = "autores"> </a>
- [David](https://github.com/carbonto)
- [Pedro](https://github.com/pedrolol440)
- [Carlos](https://github.com/carlosramos1414)
- [Leopoldo](https://github.com/leocadpin)
