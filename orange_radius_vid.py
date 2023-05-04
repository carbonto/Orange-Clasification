import cv2 as cv
import os
import argparse
import numpy as np
from cv2 import split
import time as tm

# # Create a VideoCapture object
# cap = cv.VideoCapture(0)

# Read the image
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required = True, help = "nombre de la imagen")
args = vars(ap.parse_args())
path = os.path.join('videos', args['video'])
cap = cv.VideoCapture(path)

# # Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv.VideoWriter('outpy.avi',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(cap.isOpened()):
    ret, img = cap.read()
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

    out.write(result)
    cv.imshow('frame',result)



    cv.imshow("Segmentacion", result)
    cv.waitKey(0)
    cv.destroyAllWindows()
