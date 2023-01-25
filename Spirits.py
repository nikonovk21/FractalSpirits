import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from random import choice
import imageio
from PIL import Image

def mandelbrot(c):
    z = c
    n = 256
    for i in range(n):
        if abs(z) > 2:
            return i
        z = z*z + c
    return n

def create_fractal(xmin, xmax, ymin, ymax, xpoints, ypoints):
    x = np.linspace(xmin, xmax, xpoints)
    y = np.linspace(ymin, ymax, ypoints)
    c = x + y * 1j
    mandel = np.array([mandelbrot(c) for c in c.flat]).reshape(xpoints, ypoints)
    return mandel

def create_spirits():
    fractal = create_fractal(-2, 2, -2, 2, 800, 800)
    fractal = np.asarray(fractal)
    fractal = np.interp(fractal, (fractal.min(), fractal.max()), (0, 255))
    fractal = fractal.astype(np.uint8)
    image = Image.fromarray(fractal)
    image = image.resize((500,500))
    spirits = Image.open("spirits.jpg")
    spirits.paste(image, (50,50))
    spirits.show()

if __name__ == '__main__':
    create_spirits()
