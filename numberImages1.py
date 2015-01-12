import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


#Taking the image of a dot in a 8x8

i = Image.open('images/numbers/0.1.png')

# Returns 3-D array corresponding to the image, [row,column,pixel]
#Pixel has R,G,B and Alpha(Transparency)
iar = np.asarray(i)

plt.imshow(iar)
plt.show()

print(iar)
