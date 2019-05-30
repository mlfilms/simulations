import glob
import os
import shutil

allDat = glob.glob('**/**/defect*.dat')


outDir = os.path.join(os.getcwd(),'accumulated');
shutil.rmtree(outDir)
print(outDir)
if not os.path.exists(outDir):
    os.makedirs(outDir)
    
    
number = 1
for dat in allDat:
    drive,pathAndFile = os.path.splitdrive(dat)
    path, file = os.path.split(pathAndFile)
    simNum = int(file.split('defect')[-1].split('.dat')[0])
    #print(simNum)
    if simNum>3:
        name = 'defect'+str(number)+'.dat'
        newFilename = os.path.join(outDir,name)
        shutil.copyfile(dat,newFilename)
        number = number +1