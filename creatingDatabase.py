import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import functools


def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            #print(str(eachNum)+'.'+str(eachVer))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            lineToWrite = str(eachNum) + '::' +eiar1 + '\n'
            numberArrayExamples.write(lineToWrite)
    
createExamples()

def threshold(imageArray):
    balanceArray = []
    newArray = imageArray

    for eachRow in imageArray:
        for eachPixel in eachRow:
            #print (eachPixel)
            #avgNum = functools.reduce(lambda x, y: x + y, eachPixel[:3])/len(eachPixel[:3])
            avgNum = sum(eachPixel)/3
            balanceArray.append(avgNum)
         #   time.sleep(5)
    balance = sum(balanceArray)/len(balanceArray)
    #balance = functools.reduce(lambda x, y: x + y, balanceArray)/len(balanceArray)

    for eachRow in newArray:
        for eachPixel in eachRow:
            if sum(eachPixel)/3 > balance:
                eachPixel[0] = 255
                eachPixel[1] = 255
                eachPixel[2] = 255
                eachPixel[3] = 255
            else:
                eachPixel[0] = 0
                eachPixel[1] = 0
                eachPixel[2] = 0
                eachPixel[3] = 255
    return (newArray)


i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)


threshold(iar2)
threshold(iar3)
threshold(iar4)

'''
fig = plt.figure()

ax1 = plt.subplot2grid((8,6),(0,0),rowspan =4 , colspan =3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan =4 , colspan =3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan =4 , colspan =3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan =4 , colspan =3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()


print(iar3)
'''
