
from random import Random
from math import radians, sin, cos 
import random

from config import Config
from PIL import Image, ImageDraw
#import matplotlib.pyplot as plt

GENERATOR_CONFIGURATION = Config.ARTIFACTS_GENERATOR


class ArtifactsGenerator:
    def __init__(self, data_img):
        self.image = Image.fromarray(data_img[:,:]).convert('RGBA')


    @staticmethod
    def randomizer():
        randomizer= Random()
        return randomizer

    def draw_gradient_elipse(self, pos_x, pos_y, radious_range, gradient_range, transparent_range, levels):
        gradient_min, gradient_max = gradient_range
        transparent_min, transparent_max = transparent_range
        radious_min, radious_max = radious_range

        gradient_step = float(gradient_max - gradient_min)/levels
        transparent_step = float(transparent_max - transparent_min)/levels
        radious_step = float(radious_max - radious_min)/levels

        for i in range(1, levels+1, 1):
            elipse_x_0 = pos_x - (radious_max - radious_step*i) 
            elipse_x_1 = pos_x + (radious_max - radious_step*i)
            elipse_y_0 = pos_y - (radious_max - radious_step*i)
            elipse_y_1 = pos_y + (radious_max - radious_step*i)
            color = (int(gradient_min + gradient_step*i), int(gradient_min + gradient_step*i),
                     int(gradient_min + gradient_step*i), int(transparent_min + transparent_step*i))

            image_draw_elipse = ImageDraw.Draw(self.image)
            image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
                                    fill=color, outline=color)

    def draw_gradient_triangle(self, pos_x, pos_y, high_range, alpha, beta, gradient_range, transparent_range, levels):
        gradient_min, gradient_max = gradient_range
        transparent_min, transparent_max = transparent_range
        high_min, high_max = high_range

        gradient_step = float(gradient_max - gradient_min)/levels
        transparent_step = float(transparent_max - transparent_min)/levels
        high_step = float(high_max - high_min)/levels

        point_0 = pos_x, pos_y
        image_draw_triangle = ImageDraw.Draw(self.image)

        for i in range(1, levels+1, 1):
            high = high_max - high_step*i
            point_1 = pos_x + high * sin(alpha), pos_y - high * cos(alpha)
            point_2 = pos_x + high * sin(beta), pos_y - high * cos(beta)

            color = (int(gradient_min + gradient_step*i), int(gradient_min + gradient_step*i),
                     int(gradient_min + gradient_step*i), int(transparent_min + transparent_step*i))

            image_draw_triangle.polygon(point_0 + point_1 + point_2, fill=color)


    # def generate_radiues_noses(self, pos_x, pos_y):
    #     point_0 = pos_x, pos_y
    #     randomizer= Random()
    #     for i in range(8):
    #         if randomizer.choice([True, False]):
    #             a = randomizer.uniform(i*0.7853981633974, (i+1)*0.7853981633974)
    #             b = randomizer.uniform(i*0.7853981633974, (i+1)*0.7853981633974)
    #             r = randomizer.uniform(5.0, 12.0)
    #             alpha = randomizer.randint(210, 255)
    #             color = (255, 255, 255, alpha)

    #             print("Triangle:",i, a, b, r)
    #             point_1 = int(pos_x + r * sin(a)), int(pos_y - r * cos(a))
    #             point_2 = int(pos_x + r * sin(b)), int(pos_y - r * cos(b))
    #             image_draw_triangle = ImageDraw.Draw(self.image)
    #             image_draw_triangle.polygon(point_0 + point_1 + point_2, fill=color)

    def generate_stars(self, pos_x, pos_y):
        # NORD STAR
        randomizer = ArtifactsGenerator.randomizer()
        high_range = [randomizer.uniform(2,4), randomizer.uniform(15, 19)]
        alpha = radians(randomizer.uniform(-10, -5))
        beta = radians(randomizer.uniform(5, 10))
        gradient_range = [180, 255]
        transparent_range = [200, 255]
        levels = 10
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta, gradient_range, transparent_range, levels)

        # NORD EAST STAR
        high_range = [randomizer.uniform(2,3), randomizer.uniform(10, 15)]
        alpha = radians(randomizer.uniform(-10+72, 10+72))
        beta = radians(randomizer.uniform(-10+72, 10+72))
        gradient_range = [100, 180]
        transparent_range = [100, 180]
        levels = 10
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta, gradient_range, transparent_range, levels)

        # SOUT EAST STAR
        high_range = [randomizer.uniform(3, 5), randomizer.uniform(15, 19)]
        alpha = radians(randomizer.uniform(-10+2*72, 10+2*72))
        beta = radians(randomizer.uniform(-10+2*72, 10+2*72))
        gradient_range = [180, 255]
        transparent_range = [150, 255]
        levels = 10
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta, gradient_range, transparent_range, levels)


    def generate_symmetrical_elipses(
        self, circle_pos_x_range=GENERATOR_CONFIGURATION["CIRCLE_POS_X_RANGE"],
        circle_pos_y_range=GENERATOR_CONFIGURATION["CIRCLE_POS_Y_RANGE"],
        circle_radious=GENERATOR_CONFIGURATION["CIRCLE_RADIUS"],
        gradient_range=GENERATOR_CONFIGURATION["GRADIENT_RANGE"],
        transparent_range=GENERATOR_CONFIGURATION["TRANSPARENT_RANGE"],
        levels=GENERATOR_CONFIGURATION["LEVELS"]):

        randomizer = ArtifactsGenerator.randomizer()

        # FIRST ELIPSE
        pos_x_1 = randomizer.uniform(*circle_pos_x_range)
        pos_y_1 = randomizer.uniform(*circle_pos_y_range)
        radious_range = [2, randomizer.uniform(*circle_radious)]

        self.draw_gradient_elipse(pos_x_1, pos_y_1, radious_range, gradient_range, transparent_range, levels)
        self.generate_stars(pos_x_1, pos_y_1)
        self.image.show()

        # # SECOND ELIPSE
        # pos_x_2 = pos_x_1 + randomizer.uniform(-2.0, 2.0)
        # pos_y_2 = 2*127.0 - pos_y_1 + randomizer.uniform(-2.0, 2.0)
        # radious_range = [2, randomizer.uniform(*circle_radious)]

        # self.draw_gradient_elipse(pos_x_2, pos_y_2, radious_range, [100, 255], transparent_range, levels)





        # # 2*127.0 - randomizer.uniform(*self.circle_pos_y_min_max) + randomizer.uniform(-1.5, 1.5)
        # w = randomizer.uniform(*self.circle_radious_min_max)
        # h = randomizer.uniform(*self.circle_radious_min_max)
        # alpha = randomizer.randint(210, 255)

        # elipse_x_0 = pos_x - w 
        # elipse_x_1 = pos_x + w 
        # elipse_y_0 = pos_y - h 
        # elipse_y_1 = pos_y + h 
        # color = (255, 255, 255, alpha)

        # image_draw_elipse = ImageDraw.Draw(self.image)
        # image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
        #                           fill=color, outline=color)

        # self.generate_radiues_noses(pos_x, pos_y)
        # print(elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1, w, h, alpha)
        # pos_x = randomizer.uniform(*circle_pos_x_range)
        # pos_y = randomizer.uniform(*circle_pos_y_range)
        # radious_range = [1, randomizer.uniform(*circle_radious)]
 
        # self.draw_gradient_elipse(pos_x, pos_y, radious_range, gradient_range, alpha_range, levels)
        # for j in range(5):
        #     i = 4-j
        #     print(i)
        #     elipse_x_0 = pos_x - w/(5-i) 
        #     elipse_x_1 = pos_x + w/(5-i) 
        #     elipse_y_0 = pos_y - h/(5-i) 
        #     elipse_y_1 = pos_y + h/(5-i) 
        #     color = (int(255-15*i), int(255-15*i), int(255-15*i), int(255-15*i))
        #     image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
        #                             fill=color, outline=color)
            # self.image = self.image.resize((255, 255))

        # i = 3
        # elipse_x_0 = pos_x - w/(10-i) 
        # elipse_x_1 = pos_x + w/(10-i) 
        # elipse_y_0 = pos_y - h/(10-i) 
        # elipse_y_1 = pos_y + h/(10-i) 
        # color = (255, 255, 255, 255)
        # image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
        #                         fill=color, outline=color)
        # elipse_x_0 = pos_x - w/2.0 
        # elipse_x_1 = pos_x + w/2.0 
        # elipse_y_0 = pos_y - h/2.0 
        # elipse_y_1 = pos_y + h/2.0 
        # color = (20, 20, 20, alpha)
        # image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
        #                         fill=color, outline=color)
        # # for i in range(10):
        #     w_i = (w/10.0)*i
        #     h_i = (h/10.0)*i
        #     elipse_x_0 = pos_x - w_i
        #     elipse_x_1 = pos_x + w_i 
        #     elipse_y_0 = pos_y - h_i 
        #     elipse_y_1 = pos_y + h_i
        #     color = (int(255 - 25.5*i), int(255 - 25.5*i), int(255 - 25.5*i), alpha)
        #     print((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1, color))
        #     image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
        #                             fill=color, outline=color)

        # self.generate_radiues_noses(pos_x, pos_y)
        # print(elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1, w, h, alpha)

        # pos_x = pos_x + randomizer.uniform(-2.0, 2.0)
        # pos_y = 2*127.0 - pos_y + randomizer.uniform(-2.0, 2.0) 
        # # 2*127.0 - randomizer.uniform(*self.circle_pos_y_min_max) + randomizer.uniform(-1.5, 1.5)
        # w = randomizer.uniform(*self.circle_radious_min_max)
        # h = randomizer.uniform(*self.circle_radious_min_max)
        # alpha = randomizer.randint(210, 255)

        # elipse_x_0 = pos_x - w 
        # elipse_x_1 = pos_x + w 
        # elipse_y_0 = pos_y - h 
        # elipse_y_1 = pos_y + h 
        # color = (255, 255, 255, alpha)

        # image_draw_elipse = ImageDraw.Draw(self.image)
        # image_draw_elipse.ellipse((elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
        #                           fill=color, outline=color)

        # self.generate_radiues_noses(pos_x, pos_y)
        # print(elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1, w, h, alpha)
        # return self.image






