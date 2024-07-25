#%%
#from google.colab.patches import cv2_imshow solo para google colab
import numpy as np
import cv2 as cv

#%%
def show_im(im):
    cv.imshow('window', im)
    cv.waitKey(0)
    cv.destroyAllWindows()

#%%
def draw_triangle(im, triangle, color=(0,255,0)):
    # Normalizar coordenadas homogeneas
    triangle = np.array([ v[:-1]/v[-1] for v in triangle] , np.uint16)
    cv.drawContours(im, [triangle.astype(int)], 0, color, -1)
    for v in triangle:
        cv.circle(im, tuple(v), 2, (255,0,255),-1)

#%%
def scale(vertex, sx, sy):
    M=np.array([[sx,0,0], [0,sy,0], [0,0,1]])
    res= M @ vertex.T
    return res.T

#%%
def rotate(vertex, teta):
    M=np.array([[np.cos(teta), -np.sin(teta), 0], [np.sin(teta), np.cos(teta), 0], [0,0,1]])
    res= M @ vertex.T
    return res.T

#%%
def translate(vertex, dx, dy):
    M=np.array([[1,0,dx], [0,1,dy], [0,0,1]])
    res= M @ vertex.T
    return res.T

#%%
def compuesta(vertex, dx, dy, sx, sy, teta):
    M=np.array([[sx*np.cos(teta),-np.sin(teta),dx], [np.sin(teta),sy*np.cos(teta),dy], [0,0,1]])
    res= M @ vertex.T
    return res.T

#%%
# image size
w = 500
h = 500
im = np.zeros((h,w,3), np.uint8)

# Parametros de las transformaciones
# Traslada a centro y realiza escala y rotacion
angle = 30
s = 3
t = 250

#%%
# Sistema coordenado de imagenes
triangle1 = np.array( [[10,10,1], [70,10,1], [40, 60,1]])

#%%
triangle2 = translate(rotate(scale(translate(triangle1, -40,-30),s,s) ,np.radians(angle)), t,t)
triangle3 = compuesta(triangle1,t,t,s,s,np.radians(angle))
#%%
draw_triangle(im, triangle1)
draw_triangle(im, triangle2, color= (155,255,130))
draw_triangle(im, triangle3, color= (0,100,255))

show_im(im)
# %%
