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
- [Conclusiones](#conclusiones)
- [Trabajo futuro](#Trabajofuturo)
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
### Segmentacion de imagenes 
Para probar la segmentación y detección de radio de las naranjas se ha creado un script llamado evaluate.sh el cual ejecutar varias veces orange_radius.py con las distintas imagenes de prueba y se ven los resultados obtenidos

```
./evaluate.sh

````
De esta manera optenemos los siguientes resultados:
![](https://github.com/carbonto/Orange-Clasification/tree/main/Orange_segmentation/results/1.png)


### Segmentación de videos
Para probar la segmentación y detección de radio de las naranjas se ha creado un script llamado orange_radius_vid.py el cual sería capaz de segmentar mediante video la imagen que le pasa el robot de la camara y sacar el radio de la naranja. En nuestro caso se ha realizado la prueba utilizando un video con el punto de vista que tendría la camara del robot en el proceso de clasificación de naranjas.

```
python3 orange_radius_vid.py

```

De esta manera optenemos los siguientes resultados:
![](https://github.com/carbonto/Orange-Clasification/tree/main/Orange_segmentation/naranjita.avi)

## Conclusiones <a name = "conclusiones"> </a>
En este proyecto se ha desarrollado un sistema de segmentación de naranjas por calibre, utilizando técnicas de visión por computadora y aprendizaje profundo, y se ha simulado el movimiento de un robot SCARA en el software Robot Studio para su clasificación. Se ha logrado una precisión razonable en la detección y clasificación de las naranjas en diferentes calibres, lo que podría resultar en una mejora significativa en la eficiencia y precisión del proceso de clasificación manual.

La simulación del robot SCARA en Robot Studio permitió evaluar la viabilidad de un sistema automatizado de clasificación de naranjas por calibre y proporcionó una comprensión detallada de la integración del proceso de clasificación de naranjas y la manipulación de un robot.

Sin embargo, hay ciertas limitaciones en el modelo actual que podrían ser mejoradas en trabajos futuros. Uno de los principales desafíos es la variabilidad en el tamaño, forma y color de las naranjas, lo que puede afectar la precisión de la segmentación y clasificación. Además, se podría explorar la posibilidad de integrar otras técnicas de procesamiento de imágenes, como la eliminación de ruido y la normalización de color, para mejorar aún más el rendimiento del modelo.

Este proyecto sienta las bases para un sistema automatizado de clasificación de naranjas por calibre, lo que podría ser beneficioso para la industria agrícola en términos de eficiencia y reducción de costos. Se espera que este trabajo inspire futuras investigaciones en esta área y proporcione una base sólida para el desarrollo de soluciones más avanzadas y precisas en el futuro.
## Trabajo futuro <a name = "Trabajofuturo"> </a>
- Investigar la integración del modelo de segmentación y clasificación de naranjas con el control de un robot SCARA real en un ambiente de producción.
- Entrenar y evaluar modelos de segmentación de naranjas con diferentes arquitecturas de redes neuronales.
- Investigar técnicas adicionales de procesamiento de imágenes para mejorar la precisión del modelo.
- Realizar pruebas en diferentes condiciones de iluminación y en diferentes tipos de naranjas para evaluar la robustez del modelo.
- Desarrollar una aplicación web o móvil para que los usuarios puedan cargar una imagen de una naranja y obtener su clasificación de calibre automáticamente.
- Evaluar el costo-beneficio de implementar un sistema automatizado de clasificación de naranjas en una empresa agrícola.
## ✍️ Autores <a name = "autores"> </a>
- [David](https://github.com/carbonto)
- [Pedro](https://github.com/pedrolol440)
- [Carlos](https://github.com/carlosramos1414)
- [Leopoldo](https://github.com/leocadpin)
