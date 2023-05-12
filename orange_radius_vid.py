import cv2 as cv
import os
import argparse
import numpy as np

# Parsear los argumentos de línea de comandos
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Ruta del archivo de video")
args = vars(ap.parse_args())

# Ruta del archivo de video
video_path = args['video']

# Crear el objeto para leer el video
video = cv.VideoCapture(video_path)

# Leer el primer frame del video para obtener las dimensiones
_, frame = video.read()
height, width, _ = frame.shape

# Definir el tamaño de reescalado deseado
rescale_width = 640
rescale_height = 480

# Calcular el factor de escala para reescalar los resultados
scale_factor_x = rescale_width / width
scale_factor_y = rescale_height / height

#Opciones de guardado
# Define el codec y crea el objeto VideoWriter. El resultado se guarda en el archivo 'output_path'.
fourcc = cv.VideoWriter_fourcc(*'MJPG')  # Codec de video para el archivo de salida
out = cv.VideoWriter('naranjita.avi', fourcc, 30.0, (rescale_width, rescale_height))




# Bucle para procesar cada frame del video
while True:
    # Leer el frame actual del video
    ret, frame = video.read()

    # Verificar si se llegó al final del video
    if not ret:
        break

    # Reescalar el frame al tamaño deseado
    frame = cv.resize(frame, (rescale_width, rescale_height))

    # Resto del código para procesar el frame, realizar la segmentación, medición, etc.
    #Conversion a HSV
    img_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    pixel_to_cm = 0.15  # Relación de conversión de píxeles a centímetros

    # Definir los rangos de naranja
    lower_orange1 = np.array([0, 50, 50])
    upper_orange1 = np.array([30, 255, 255])
    lower_orange2 = np.array([160, 50, 50])
    upper_orange2 = np.array([180, 255, 255])

    # Crear la máscara para naranjas
    mask_orange1 = cv.inRange(img_hsv, lower_orange1, upper_orange1)
    mask_orange2 = cv.inRange(img_hsv, lower_orange2, upper_orange2)
    mask_orange = cv.bitwise_or(mask_orange1, mask_orange2)

    contours, _ = cv.findContours(mask_orange, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame, contours, -1, (255, 0, 0), 2)

    for i in contours:

        x, y, w, h = cv.boundingRect(i)
        center = ((x+x+w)//2, (y+y+h)//2)
        area = cv.contourArea(i)
        radius = np.sqrt(area / np.pi) * pixel_to_cm
        # (x,y), radius = cv.minEnclosingCircle(i)
        cv.circle(frame, (center), 2, (255, 0, 0), 2)
        cv.putText(frame, "R: {:.2f} cm".format(radius * pixel_to_cm), (center[0]-45, center[1]+40), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
        # cv.putText(img, "R: ", (center[0]-45, center[1]+40), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

    # Aplicar la máscara a la imagen original
    result = cv.bitwise_and(frame, frame, mask=mask_orange)

    # Escalar los resultados
    # ...

    # Mostrar el frame procesado
    cv.imshow("Segmentacion", result)
    # Guardar el frame procesado en el video de salida
    out.write(result)
    # Detener el bucle si se presiona la tecla 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



# Liberar los recursos
video.release()
cv.destroyAllWindows()
