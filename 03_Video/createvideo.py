import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('/home/asrc/01_SDCE_Udacity/Proyecto_3_Sensor-Fusion-and-Object-Tracking/nd013-c2-fusion-starter-main_End_Project/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('my_tracking_results.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()