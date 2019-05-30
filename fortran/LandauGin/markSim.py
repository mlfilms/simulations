import cv2
import matplotlib.pyplot as plt
import pprint as pp
import numpy as np
from PIL import Image
import glob
import os
import json


def pointing(original_img , predictions):
    newImage = np.copy(original_img)

    for result in predictions:
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']
        
        x = int((top_x+btm_x)/2)
        y = int((top_y+btm_y)/2)
    
        confidence = result['confidence']
        label = result['label'] + " " + str(round(confidence, 3))
        
        if confidence > 0.3:
            newImage = cv2.circle(newImage, (x, y), 2, (255,0,0), -1)
            #newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
        
    return newImage
    
    
    
