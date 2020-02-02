import random
import numpy as np

def color_change(image, pos):
    if pos == "f&b":
        #Change image background color
        r1 = random.randint(0, 255)
        r2 = random.randint(200, 255)
        r3 = random.randint(150, 200)
        image[np.where((image >= [165, 165, 165]).all(axis=2))]=[r1, r2, r3]
        #Change image Object Color
        p1 = random.randint(0, 15)
        p2 = random.randint(0, 255)
        p3 = random.randint(200, 255)
        image[np.where((image <= [145, 145, 145]).all(axis=2))] = [p1, p2, p3]
        return image
    elif pos == "front":
        #Change image Object Color
        r1 = random.randint(0, 255)
        r2 = random.randint(0, 255)
        r3 = random.randint(0, 255)
        image[np.where((image <= [145, 145, 145]).all(axis=2))] = [r1, r2, r3]

        return image
    elif pos == "back":
        #Change image Object Color
        r1 = random.randint(0, 255)
        r2 = random.randint(0, 255)
        r3 = random.randint(0, 255)
        image[np.where((image >= [165, 165, 165]).all(axis=2))] = [r1, r2, r3]

        return image