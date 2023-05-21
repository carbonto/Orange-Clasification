# Orange-Clasification 🍊🤖️
El proyecto consiste en la clasificación de naranjas por calibre. Como ya se comentó en la practica 3, el sistema ideado se basaba en un robot scara que depositaba las naranjas en distintas cajas según el calibre detectado con un sistema de visón artificial. En el siguiente repositorio se encuentra por una parte el codigo de OpenCV para la detección y clasificación de dichas naranjas por camara, y 
por otro lado, se encuentra el codigo de Robot Studio, donde se ha realizado una simulación del que sería el proceso real de clasificación con el robot Scara.
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/carbonto/Orange-Clasification/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

## 📝Indice
- [Instalación](#instalacion)
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
## Simulación Robot Studio <a name = "robot"> </a>
Para la simulación en Robot Studio se ha empleado el robot Scara IRB 910SC de ABB, pues como ya se comentó en la memoria de la práctica 3, es el mas adecuado y rentable para nuestro proyecto de clasificación de naranjas por calibres. En la siguiente imagen podemos ver el robot empleado, en la posición en la cual se dispone a coger la naranja de la cinta para depositarla en las diferentes cajas. Este proceso se realiza una vez se ha detectado el calibre de la naranja con el sistema de visión  artificial:
![Robot Scara](/robot_scara.png)

En la siguiente imagen se muestra una visión global del sistema. Como se puede observar, el sistema esta formado por una cinta principal, a través del cual llegan las naranjas(represantadas por la esfera gris). Una vez llegan a la posición del robot, se detiene la cinta y se realizaría el proceso de detección de calibre (que en este caso aun no se ha integrado en Robot Studio). Una vez detectado el calibre, el robot cogería la naranja y la transportaría a una de las cajas que se encuentran a los lados del robot. Una vez llenas estas cajas, se activarían las cintas para transportarlas hacia el siguiente punto en la estación en la que se encuentre. Esta disposición no es exactamente la misma que la descrita en la memoria de la práctica 3. Esto se debe principalmente que las limitaciones de Robot Studio no permitieron recrear la idea de estación deseada y se tuvo que adaptar a lo anteriormente descrito.
![Estacion Completa](/Estacion_completa.png)

A continuación se muestra un video en el que se puede observar el funcionamiento del sistema en la estación de Robot Studio:
![Robot Studio Classification](Classification_Robot_Studio.gif)
Se ha conseguido simular de manera bastante precisa el funcionamiento de como sería el sistema real. Únicamente difiere en que para simular la llegada de naranjas al robot por la cinta, una vez el robot la deposita en la caja, esta desaparece y vuelve a aparecer en la posición inicial para ser transportado hacia el robot de nuevo. Por tanto, la lógica e implementación del sistema del sistema se basa en lo siguiente:
- El robot coge la primera naranja y la deja en la primera caja utilizando componentes attacher y dettacher de Robot Studio.
- La naranja se reposiciona al comienzo de la cinta cuando la deja el robot utilizando un componente Positioner.
- La naranja empieza a moverse hacia al robot por la cinta utilizando un componente LinearMover.
- Se utiliza un componente Plane Sensor que detecta cuando la naranja ha llegado a la posición. 
- Una vez detecta que ha llegado se desactiva el componente LinearMover para que se deje de mover la naranja.
- El robot la coge y se vuelve a iniciar todo el proceso.

## Segmentación OpenCV <a name = "segmentacion"> </a>
Dentro de la carpeta Orange-Segmentation se encuentran diversos archivos que nos ayudarán al proceso de segmetanción de las naranjas. Primero tenemos el script orange_radius.py el cual convierte a HSV, segmenta los objetos de color naranja y obtiene el radio del mismo.
```
python3 orange_radius.py

```
Otro script implementado es orange_radius_vid.py, el cual realiza el mismo proceso que el anterior, pero para videos como los obtenidos con la camara del robot para en el procesamiento de naranjas.

```
python3 orange_radius_vid.py

```
Las pruebas realizadas con la segmentación se encuentran en el siguiente apartado [Pruebas realizadas](#pruebas)

## Pruebas realizadas <a name = "pruebas"> </a>
### Segmentacion de imagenes 
Para probar la segmentación y detección de radio de las naranjas se ha creado un script llamado evaluate.sh, el cual ejecuta varias veces orange_radius.py con las distintas imagenes de prueba y se ven los resultados obtenidos

```
./evaluate.sh

````
De esta manera optenemos los siguientes resultados:
![Orange Result](/Orange_segmentation/results/1.png)


### Segmentación de videos
Para probar la segmentación y detección de radio de las naranjas, se ha creado un script llamado orange_radius_vid.py el cual sería capaz de segmentar mediante video la imagen que le pasa el robot de la camara y obtener el radio de la naranja. En nuestro caso, se ha realizado la prueba utilizando un video con el punto de vista que tendría la camara del robot en el proceso de clasificación de naranjas.

```
python3 orange_radius_vid.py

```

De esta manera optenemos los siguientes resultados:
![Orange Video Result](Video_clasification.gif)

Una vez hemos obtenido el calibre de la naranja mediante el programa escrito en OpenCV, tenemos que conectando ese script al robot y usando la cámara "Integrated Visión" el robot se mueve directamente hacía la naranja y la coje para ponerla en su correpondiente caja. El vídeo que se muestra a continuación no es significativo del proyecto, simplemente es un ejemplo puesto que la estación en RobotStudio se ha desarrollado para otro robot, es una aproximación de como sería, además de que no  es posible recoger la naranja puesto que el compresor del robot del laboratorio funciona de manera errática.

![OrangeRobotTrial](video_fondo_balnco.gif)

## Conclusiones <a name = "conclusiones"> </a>
En este proyecto se ha desarrollado un sistema de segmentación de naranjas por calibre, utilizando técnicas de visión por computadora, y se ha simulado el movimiento de un robot SCARA en el software Robot Studio para su clasificación. Se ha logrado una precisión razonable en la detección y clasificación de las naranjas en diferentes calibres, lo que podría resultar en una mejora significativa en la eficiencia y precisión del proceso de clasificación manual.

La simulación del robot SCARA en Robot Studio permitió evaluar la viabilidad de un sistema automatizado de clasificación de naranjas por calibre y proporcionó una comprensión detallada de la integración del proceso de clasificación de naranjas y la manipulación de un robot.

Sin embargo, hay ciertas limitaciones en el modelo actual que podrían ser mejoradas en trabajos futuros. Uno de los principales desafíos es la variabilidad en el tamaño, forma y color de las naranjas, lo que puede afectar la precisión de la segmentación y clasificación. Además, se podría explorar la posibilidad de integrar otras técnicas de procesamiento de imágenes, como la eliminación de ruido y la normalización de color, para mejorar aún más el rendimiento del modelo.

Este proyecto sienta las bases para un sistema automatizado de clasificación de naranjas por calibre, lo que podría ser beneficioso para la industria agrícola en términos de eficiencia y reducción de costos. Se espera que este trabajo inspire futuras investigaciones en esta área y proporcione una base sólida para el desarrollo de soluciones más avanzadas y precisas en el futuro.
## Trabajo futuro <a name = "Trabajofuturo"> </a>
- Investigar la integración del modelo de segmentación y clasificación de naranjas con el control de un robot SCARA real en un ambiente de producción.
- Entrenar y evaluar modelos de segmentación de naranjas con diferentes arquitecturas de redes neuronales.
- Investigar técnicas adicionales de procesamiento de imágenes para mejorar la precisión del modelo.
- Realizar pruebas en diferentes condiciones de iluminación y en diferentes tipos de naranjas para evaluar la robustez del modelo.
- Evaluar el costo-beneficio de implementar un sistema automatizado de clasificación de naranjas en una empresa agrícola.
## ✍️ Autores <a name = "autores"> </a>
- [David](https://github.com/carbonto)
- [Pedro](https://github.com/pedrolol440)
- [Carlos](https://github.com/carlosramos1414)
- [Leopoldo](https://github.com/leocadpin)
