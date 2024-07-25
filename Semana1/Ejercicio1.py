#%%
import numpy as np
import cv2
import PIL
from PIL import Image, ImageDraw

#%%
def show_im(im):
    cv2.imshow('window', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#%%
im1 = np.zeros((100,100), np.uint8)
show_im(im1)

#%%
for i in range(100): im1[i,i]=255
show_im(im1)

#%%


