import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import functools
from collections import Counter


def  whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    i = i.resize((8,8), Image.ANTIALIAS)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)
    print(iar)
    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0
            while x <len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x += 1


    print (matchedAr)
    x = Counter(matchedAr)
    print (x)
    

whatNumIsThis('images/test1.png')
