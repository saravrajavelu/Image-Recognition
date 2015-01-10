import numpy as np
from PIL import Image
import matplotlib


#Taking the image of a dot in a 8x8

i = Image.open('images/dot.png')

# Returns 3-D array corresponding to the image, [row,column,pixel]
#Pixel has R,G,B and Alpha
iar = np.asarray(i)

print(iar)
