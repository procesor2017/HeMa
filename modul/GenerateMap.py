import noise
import numpy as np
from PIL import Image
import random

shape = (1024, 1024)
scale = 350
octaves = 6
persistence = 0.6
lacunarity = 2

blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [255, 250, 250]
mountain = [139, 137, 137]

base_random = random.randrange(0, 800)

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i / scale,
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=1024,
                                    repeaty=1024,
                                    base=base_random)


def add_color(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.08:
                color_world[i][j] = blue
            elif world[i][j] < -0.05:
                color_world[i][j] = beach
            elif world[i][j] < 0.20:
                color_world[i][j] = green
            elif world[i][j] < 0.30:
                color_world[i][j] = mountain
            elif world[i][j] < 1.0:
                color_world[i][j] = snow
    return color_world


color_world = add_color(world)
Image.fromarray((color_world).astype(np.uint8)).save('../data/map.png')
