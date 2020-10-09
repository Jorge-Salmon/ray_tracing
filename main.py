#!/usr/bin/env python
''' Ray tracer in Python by Jorge Salmon, 2020 '''

from multiprocessing import cpu_count

from image import Image
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material

# import scene
from scene_2spheres import *

def main():
    process_count = cpu_count()

    scene = Scene(CAMERA, OBJECTS, LIGHTS, WIDTH, HEIGHT)
    engine = RenderEngine()
    with open("scene1.ppm", "w") as img_fileobj:
        engine.render_multiprocess(scene, process_count, img_fileobj)

if __name__ == "__main__":
    main()
