import cv2 as cv
import os
import argparse
import numpy as np
from cv2 import split
import time as tm


# Read the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "nombre de la imagen")

args = vars(ap.parse_args())
path = os.path.join('images', '{}.jpeg'.format(args['image']))
# path = os.path.join('images', '1.jpeg')
# n = args['image']
# save_path = os.path.join('results', '{}.png'.format(n))
# save_path2 = os.path.join('results', 'colour{}.png'.format(n))
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

# Aplicar la máscara a la imagen original
result = cv.bitwise_and(img, img, mask=mask_orange)

cv.imshow("Segmentacion", result)
cv.waitKey(0)
cv.destroyAllWindows()

# # Draw rectangular bounded line on the detected red area
# contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)