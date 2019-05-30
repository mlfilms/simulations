How to use for darkflow training

./call_defect.sh

That command will generate a new folder containing the simulation results

Modified datAnnotate.py to point to the data subfolder in the new folder
run datAnnotate.py with python to generate text annotations
imgGen.py should be inside the data folder. Run that file to gnerate .jpg images

You now need the files in mlfilms/ImageAnnotation. Clone from github if needed.
Modify fileConvertBatch to point to the data folder and change the size variable if needed.
This will output .xml annotations in a new /out folder in the data folder.

In the darkflow folder inside defectTracker, modify trainFlow.py to point to the .jpg images and .xml annotations
Run the script to train the model
Modify and run runFlow.py to test the new model

Currently does not make a very good model. Need to create methods for aggregating more data.