import glob
import os
import shutil
import sys
from datAnnotate import datAnnotate

fileConvertPath = 'E:/Projects/fake/ImageAnnotation/'
mainDir = os.getcwd()
outDir = os.path.join(os.getcwd(),'accumulated');

#print(outDir)
if os.path.exists(outDir):
    shutil.rmtree(outDir)
#if not os.path.exists(outDir):
os.makedirs(outDir)
    
allDDat = glob.glob('**/**/defect*.dat')

for dat in allDDat:
    drive,pathAndFile = os.path.splitdrive(dat)
    filePath, file = os.path.split(pathAndFile)
    filePath = os.path.dirname(dat)
    numPath = os.path.dirname(filePath)
    runNum = numPath.split('_')[-1]
    print(runNum)
    simNum = int(file.split('defect')[-1].split('.dat')[0])
    #print(simNum)
    if simNum>3:
        name = runNum+'_defect'+str(simNum)+'.dat'
        newFilename = os.path.join(outDir,name)
        shutil.copyfile(dat,newFilename)
    
allODat = glob.glob('**/**/out*.dat')

datAnnotate()

for dat in allODat:
    drive,pathAndFile = os.path.splitdrive(dat)
    filePath, file = os.path.split(pathAndFile)
    filePath = os.path.dirname(dat)
    numPath = os.path.dirname(filePath)
    runNum = numPath.split('_')[-1]
    print(runNum)
    simNum = int(file.split('out')[-1].split('.dat')[0])
    #print(simNum)
    if simNum>3:
        name = runNum+'_out'+str(simNum)+'.dat'
        newFilename = os.path.join(outDir,name)
        shutil.copyfile(dat,newFilename)
    
shutil.copyfile('imgGen.py',os.path.join(outDir,'imgGen.py'))
sys.path.append(outDir)
os.chdir(outDir)
from imgGen import imgGen
imgGen()
sys.path.append(fileConvertPath)
from fileConvertBatch import fileConvertBatch
fileConvertBatch(outDir,[100,100])


os.chdir(mainDir)


