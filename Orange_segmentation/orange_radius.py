import cv2 as cv
import os
import argparse
import numpy as np
from cv2 import split
import time as tm


# Read the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "nombre de la imagen")

#Gestion de argumentos
args = vars(ap.parse_args())
path = os.path.join('images', '{}.jpeg'.format(args['image']))
n = args['image']
save_path = os.path.join('results', '{}.png'.format(n))

#Conversion a HSV
img = cv.imread(path)
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

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
cv.drawContours(img, contours, -1, (255, 0, 0), 2)

for i in contours:

    x, y, w, h = cv.boundingRect(i)
    center = ((x+x+w)//2, (y+y+h)//2)
    (x,y), radius = cv.minEnclosingCircle(i)
    cv.circle(img, (center), 2, (255, 0, 0), 2)
    cv.putText(img, "R: {} ".format(radius), (center[0]-45, center[1]+40), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
    # cv.putText(img, "R: ", (center[0]-45, center[1]+40), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)

# Aplicar la máscara a la imagen original
result = cv.bitwise_and(img, img, mask=mask_orange)

cv.imwrite(save_path,result)
cv.imshow("Segmentacion", result)
cv.waitKey(0)
cv.destroyAllWindows()

# # Draw rectangular bounded line on the detected red area
# contours, hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)