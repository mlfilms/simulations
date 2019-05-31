import numpy as np
import matplotlib.pyplot as plt
import glob as glob
import skimage
import imageio

def schler(angle):
    return np.sin(2.*angle)**2.
def imgGen():
    names = glob.glob('*out*.dat')
    frames = [schler(np.loadtxt(n)) for n in names]
    
    names = [n.replace('out', 'defect') for n in names]
    
    [imageio.imwrite(n.split('.')[0]+'.jpg',skimage.img_as_ubyte(im)) for n,im in zip(names,frames)]
    
    
if __name__ == "__main__":
    imgGen()

