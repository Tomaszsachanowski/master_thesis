
from random import Random
from math import sin, cos
import random

from config import Config
from PIL import Image, ImageDraw
#import matplotlib.pyplot as plt

GENERATOR_CONFIGURATION = Config.ARTIFACTS_GENERATOR


class ArtifactsGenerator:
    def __init__(self, data_img, circle_pos_x_min_max=GENERATOR_CONFIGURATION["CIRCLE_POS_X_MIN_MAX"],
                 circle_pos_y_min_max=GENERATOR_CONFIGURATION["CIRCLE_POS_Y_MIN_MAX"],
                 circle_radious_min_max=GENERATOR_CONFIGURATION["CIRCLE_RADIUS_MIN_MAX"]):

        self.image = Image.fromarray(data_img[:,:]).convert('RGBA')
        self.circle_pos_x_min_max = circle_pos_x_min_max
        self.circle_pos_y_min_max = circle_pos_y_min_max
        self.circle_radious_min_max = circle_radious_min_max

    @staticmethod
    def randomizer():
        randomizer= Random()
        return randomizer

    def generate_symmetrical_elipses(self):
        randomizer = ArtifactsGenerator.randomizer()
 
        pos_x = randomizer.uniform(*self.circle_pos_x_min_max)
        pos_y = randomizer.uniform(*self.circle_pos_y_min_max)
        w = randomizer.uniform(*self.circle_radious_min_max)
        h = randomizer.uniform(*self.circle_radious_min_max)
        alpha = randomizer.randint(210, 255)
 
        elipse_x_0 = pos_x - w 
        elipse_x_1 = pos_x + w 
        elipse_y_0 = pos_y - h 
        elipse_y_1 = pos_y + h 
        color = (255, 255, 255, alpha)

        image_draw_elipse = ImageDraw.Draw(self.image)
        image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
                                  fill=color, outline=color)

        self.generate_radiues_noses(pos_x, pos_y)
        print(elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1, w, h, alpha)

        pos_x = pos_x + randomizer.uniform(-1.5, 1.5)
        pos_y = 2*127 - randomizer.uniform(*self.circle_pos_y_min_max) + randomizer.uniform(-1.5, 1.5)
        w = randomizer.uniform(*self.circle_radious_min_max)
        h = randomizer.uniform(*self.circle_radious_min_max)
        alpha = randomizer.randint(210, 255)

        elipse_x_0 = pos_x - w 
        elipse_x_1 = pos_x + w 
        elipse_y_0 = pos_y - h 
        elipse_y_1 = pos_y + h 
        color = (255, 255, 255, alpha)

        image_draw_elipse = ImageDraw.Draw(self.image)
        image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
                                  fill=color, outline=color)

        self.generate_radiues_noses(pos_x, pos_y)
        print(elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1, w, h, alpha)
        return self.image


    def generate_radiues_noses(self, pos_x, pos_y):
        point_0 = pos_x, pos_y
        randomizer= Random()
        for i in range(8):
            if randomizer.choice([True, False]):
                a = randomizer.uniform(i*0.7853981633974, (i+1)*0.7853981633974)
                b = randomizer.uniform(i*0.7853981633974, (i+1)*0.7853981633974)
                r = randomizer.uniform(5.0, 12.0)
                alpha = randomizer.randint(210, 255)
                color = (255, 255, 255, alpha)

                print("Triangle:",i, a, b, r)
                point_1 = int(pos_x + r * sin(a)), int(pos_y - r * cos(a))
                point_2 = int(pos_x + r * sin(b)), int(pos_y - r * cos(b))
                image_draw_triangle = ImageDraw.Draw(self.image)
                image_draw_triangle.polygon(point_0 + point_1 + point_2, fill=color)



