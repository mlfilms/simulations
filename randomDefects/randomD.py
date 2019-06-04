import numpy as np
import matplotlib.pyplot as plt
import imageio 
import skimage
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('decross',nargs='?',help='delta angle of the decrossed polarizers',type = float,default = 0)
args=parser.parse_args()
beta = np.pi/2+args.decross/180*np.pi
def decrossI(beta,image):
    #beta is the angle between pol and anl (90 for completely crossed)
    temp= ( np.sin(image)*np.cos(image)*np.sin(beta)-np.sin(image)**2*np.cos(beta)-np.cos(beta))**2
    return temp/temp.max()
nDefects = 20
grid = np.reshape(np.zeros(200*200),(200,200))
dgrid = np.reshape(np.zeros(200*200),(200,200))
ix,iy = np.indices((200,200))

def schler(grid):
    return np.sin(2.*grid)**2
def dGen(grid,x,y,k,off):
    grid = np.mod(grid+k*np.arctan2(ix-x,iy-y)+off,2*np.pi)
    return grid


for i in np.arange(nDefects):
    dxp = random.randint(0,199)
    dyp = random.randint(0,199)

    dxn = random.randint(0,199)
    dyn = random.randint(0,199)

    grid = dGen(grid,dxp,dyp,1,random.random()*2*np.pi)
    grid = dGen(grid,dxn,dyn,-1,random.random()*2*np.pi)
    dgrid[dxp,dyp] =1
    dgrid[dxn,dyn] =-1
imageio.imwrite('training.bmp',skimage.img_as_ubyte(decrossI(beta, grid)))
np.savetxt('out.dat',dgrid)
np.savetxt('defect.dat',dgrid)

