from complex import Complex, is_prisonier
import numpy as np
from PIL import Image
from tqdm import tqdm
import math


if __name__ == "__main__":
    complexes = [
        Complex.from_algebra(0.243, 0.545),
        Complex.from_algebra(0, 0),
        Complex.from_algebra(-0.75, 0.11),
        Complex.from_algebra(-1.2, 0),
        Complex.from_algebra(-0.443, -0.592),
        Complex.from_algebra(0.285, 0.01),
        Complex.from_algebra(-1.417022285618, 0.0099534),
        Complex.from_algebra(-0.038088, 0.9754633),
        Complex.from_algebra(0.285, 0.013),
        Complex.from_algebra(-0.8, 0.156),
        Complex.from_algebra(1, 0),
        Complex.from_algebra(0, 1),
        Complex.from_algebra(1, 1),
    ]


    # final dimension in pixel
    dim = 10000
    # On veut qu'en (2000, 2000), on aie le point (2 + 2i)
    # et qu'en      (300,300), on aie             (??? + ???i)
    # 2000 = 2
    # 300  = ???
    div = 2 / (dim/2)

    width = dim
    heigth = dim
    for c in complexes:
        print(f"start {c.a}+{c.b}i")
        end = np.zeros((width,heigth, 3))
        for x in tqdm(range(int(-width/2), int(width/2), 1)):
            for y in range(int(-heigth/2), int(heigth/2), 1):
                z0 = Complex.from_algebra(x*div,y*div)
                end[int(y+heigth/2), int(x+width/2)] = is_prisonier(z0, c)[1]

        img = Image.fromarray(np.uint8(end) , 'RGB')
        img.save(f"images/[{c.a}+{c.b}i].{dim}x{dim}.png")
