import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image

# x = np.array ([5 , 18 , 27 , 14])
# y = np.array ([10 , 20 ,30 , 40])
# c = ["red" , "hotpink" , "blue" , "orange"]

# plt.scatter(x,y ,color = c , s = 150)
# plt.title("Scatler Graph") 
# plt.show()


# changing a img color

f_name = r'C:\Users\op_Bh\code_base\data_science\butterfly.jpg'

img = Image.open(f_name).convert('L')
# plt.imshow(img,cmap='inferno')
# plt.imshow(img,cmap='hot')
plt.imshow(img , cmap ='gray')
plt.title ('Butterfly')

# for save img 
plt.savefig(f_name)
plt.show()