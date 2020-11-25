from PIL import Image
from matplotlib import pyplot
import numpy as np
import os



def interpolate_bilinear(array_in, width_in, height_in, array_out, width_out, height_out):
    for i in range(height_out):
        for j in range(width_out):
            
            # Relative coordinates of the pixel in output space
            x_out = j / width_out
            y_out = i / height_out
 
            # Corresponding absolute coordinates of the pixel in input space
            x_in = (x_out * width_in)
            y_in = (y_out * height_in)
 
            # Nearest neighbours coordinates in input space
            x_prev = int(x_in)
            x_next = x_prev + 1
            y_prev = int(y_in)
            y_next = y_prev + 1
 
            # Sanitize bounds - no need to check for < 0
            x_prev = min(x_prev, width_in - 1)
            x_next = min(x_next, width_in - 1)
            y_prev = min(y_prev, height_in - 1)
            y_next = min(y_next, height_in - 1)
            
            # Distances between neighbour nodes in input space
            Dy_next = y_next - y_in
            Dy_prev = 1. - Dy_next
            Dx_next = x_next - x_in
            Dx_prev = 1. - Dx_next
            
            # Aplica algoritmo bilinear
            array_out[i][j] = Dy_prev * (array_in[y_next][x_prev] * Dx_next + array_in[y_next][x_next] * Dx_prev) + Dy_next * (array_in[y_prev][x_prev] * Dx_next + array_in[y_prev][x_next] * Dx_prev)
                
    return array_out


# load image
im = Image.open("images/tulio.jpg").convert('LA')
width_2 = im.width * 2
height_2 = im.height *2
im2 = (np.array(im) )
 
out = np.zeros((height_2, width_2, 2))
out = interpolate_bilinear(im2, im.width, im.height, out, width_2, height_2)

 #Sow image
out = (out).astype(np.uint8)
out = Image.fromarray(out)
out.show()
