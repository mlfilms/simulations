#!/bin/bash
import sys
import os
import datetime
import shutil

def create_defects(defectNum,dims):
    baseDir = os.getcwd()

    def safeMake(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
    def safeRemake(dir):
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)

    decross = 50
    iterations = 10

    now = datetime.datetime.now()

    dataDir = os.path.join(os.getcwd(),'dataFolder')
    safeRemake(dataDir)

    runDir = os.path.join(dataDir,"run%d%d%d_%d%d%d" %(now.year,now.month,now.day,now.hour,now.minute,now.second))
    safeMake(runDir)



    dataDir2 = os.path.join(runDir,'data')
    imDir = os.path.join(runDir,'im')
    safeMake(dataDir2)
    safeMake(imDir)
    shutil.copyfile('randomD.py',os.path.join(runDir,'randomD.py'))
    sys.path.append(runDir)
    os.chdir(runDir)
    from randomD import randomD

    for i in range(0,defectNum):
        randomD(decross,dims)
        shutil.copyfile('out.dat',os.path.join(dataDir2,'out%d.dat' %(i)))
        shutil.copyfile('defect.dat',os.path.join(dataDir2,'defect%d.dat' %(i)))
        shutil.copyfile('training.bmp',os.path.join(imDir,'image%d.bmp' %(i)))
    os.chdir(baseDir)
if __name__ == "__main__":
    create_defects(10,[300,300])

