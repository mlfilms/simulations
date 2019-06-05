import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pprint as pp
import numpy as np
from PIL import Image
import glob
import os
import random
from scipy.ndimage.filters import gaussian_filter

def randAdd(row):
    return row+random.randint(0,30)

def addScans(img):
    xDim,yDim,zDim = img.shape
    for i in range(0,xDim):
        img[i,:,:] = img[i,:,:]+random.randint(-30,30)
    for i in range(0,yDim):
        img[:,i,:] = img[:,i,:]+random.randint(-30,30)
    
    return img

targetDir = os.path.join(os.getcwd(),'accumulated')
ext = 'jpg'
outEXT = 'bmp'
outDir = targetDir+"\\outMess\\"

if not os.path.exists(outDir):
    os.makedirs(outDir)

filePattern = 	targetDir+"\\*." + ext

for filename in glob.glob(filePattern):
    
    imgcv = cv2.imread(filename)
    #print(imgcv.dtype)

    sections = filename.split("\\")
    imName = sections[-1]
    
    #im.save(outDir+imName)
    
    #print(result)
    prePost = imName.split(".")
    noEnd = prePost[0]


    imgMean = np.mean(imgcv)
    imgSTD = np.std(imgcv)
    #print(imgMean)
    #print(imgSTD)

    imgcv= (imgcv - imgMean)/(6*imgSTD)
    imgcv = imgcv+0.5
    imgcv = imgcv*255
    imgcv = np.clip(imgcv,1,255)
    imgcv = imgcv.astype(np.uint8)
    imgcv = gaussian_filter(imgcv,sigma=2)
    imgcv = addScans(imgcv)

    im = Image.fromarray(imgcv)
    im.save(outDir+noEnd+'.'+outEXT)
    fig,ax = plt.subplots()
    imgplot = ax.imshow(imgcv)
    #plt.show()


