import base64 
import os 
fr = open("data/abc/69699.png", "r")
imgData = fr.read()
i = 0
while (os.path.isfile("./imageToSave"+str(i)+".png")) :
	i=i+1
with open("./imageToSave"+str(i)+".png", "wb") as fh:
    fh.write(imgData.decode('base64'))
