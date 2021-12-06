
from random import Random
from math import radians, sin, cos, ceil, floor
from numpy import round
from config import Config
from PIL import Image, ImageDraw, ImageFilter


ARTIFACTS_ELIPSE = Config.ARTIFACTS_ELIPSE
NORD_ARM = Config.ARTIFACTS_NORD_ARM
NORD_EAST_ARM = Config.ARTIFACTS_NORD_EAST_ARM
SOUTH_EAST_ARM = Config.ARTIFACTS_SOUTH_EAST_ARM
SOUTH_WEST_ARM = Config.ARTIFACTS_SOUTH_WEST_ARM
NORD_WEST_ARM = Config.ARTIFACTS_NORD_WEST_ARM
STRIPES = Config.ARTIFACTS_STRIPES


class ArtifactsGenerator:
    def __init__(self, data_img):
        self.image = Image.fromarray(data_img[:, :]).convert('LA')

    @staticmethod
    def randomizer():
        randomizer= Random()
        return randomizer

    def blur(self, pos_x_0, pos_y_0, pos_x_1, pos_y_1):
        region_blured = self.image.crop((pos_x_0, pos_y_0, pos_x_1, pos_y_1))
        region_blured = region_blured.filter(ImageFilter.GaussianBlur(1))
        self.image.paste(region_blured, (pos_x_0, pos_y_0, pos_x_1, pos_y_1))

    def draw_gradient_elipse(self, pos_x, pos_y, radious_range, gradient_range,
                             transparency, levels):
        gradient_min, gradient_max = gradient_range
        radious_min, radious_max = radious_range

        gradient_step = float(gradient_max - gradient_min)/levels
        radious_step = float(radious_max - radious_min)/levels

        for i in range(1, levels+1, 1):
            elipse_x_0 = pos_x - (radious_max - radious_step*i)
            elipse_x_1 = pos_x + (radious_max - radious_step*i)
            elipse_y_0 = pos_y - (radious_max - radious_step*i)
            elipse_y_1 = pos_y + (radious_max - radious_step*i)
            color = (int(gradient_min + gradient_step*i),
                     transparency)

            image_draw_elipse = ImageDraw.Draw(self.image)
            image_draw_elipse.ellipse(
                (elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
                fill=color, outline=color)

        # # Rectangle for blur
        # elipse_x_0 = floor(pos_x - radious_range[1])
        # elipse_x_1 = ceil(pos_x + radious_range[1])
        # elipse_y_0 =  floor(pos_y - radious_range[1])
        # elipse_y_1 =  ceil(pos_y + radious_range[1])
        # self.blur(elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1)

    def draw_gradient_triangle(self, pos_x, pos_y, high_range, alpha, beta,
                               gradient_range, transparency, levels):
        gradient_min, gradient_max = gradient_range
        high_min, high_max = high_range

        gradient_step = float(gradient_max - gradient_min)/levels
        high_step = float(high_max - high_min)/levels

        point_0 = pos_x, pos_y
        image_draw_triangle = ImageDraw.Draw(self.image)

        for i in range(1, levels+1, 1):
            high = high_max - high_step*i
            point_1 = pos_x + high * sin(alpha), pos_y - high * cos(alpha)
            point_2 = pos_x + high * sin(beta), pos_y - high * cos(beta)

            color = (int(gradient_min + gradient_step*i),
                     transparency)

            image_draw_triangle.polygon(point_0 + point_1 + point_2,
                                        fill=color)

        # # Rectangle for blur
        # all_pos_x = [pos_x, pos_x + high_max * sin(alpha), pos_x + high_max * sin(beta)]
        # all_pos_y = [pos_y, pos_y - high_max * cos(alpha), pos_y - high_max * cos(beta)]
        # self.blur(floor(min(all_pos_x)), floor(min(all_pos_y)), ceil(max(all_pos_x)), ceil(max(all_pos_y)))

    def generate_star_arms(self, pos_x, pos_y):
        randomizer = ArtifactsGenerator.randomizer()
        rotation = randomizer.uniform(0, 6.28)

        # NORD STAR ARM
        high_range = [randomizer.uniform(*NORD_ARM["HIGH_MIN"]),
                      randomizer.uniform(*NORD_ARM["HIGH_MAX"])]
        alpha = radians(randomizer.uniform(*NORD_ARM["ALPHA"])) + rotation
        beta = radians(randomizer.uniform(*NORD_ARM["BETA"])) + rotation
        gradient_range = NORD_ARM["GRADIENT_RANGE"]
        transparency = NORD_ARM["TRANSPARENCY"]
        levels = NORD_ARM["LEVELS"]
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta,
                                    gradient_range, transparency, levels)

        # NORD EAST STAR
        high_range = [randomizer.uniform(*NORD_EAST_ARM["HIGH_MIN"]),
                      randomizer.uniform(*NORD_EAST_ARM["HIGH_MAX"])]
        alpha = radians(randomizer.uniform(*NORD_EAST_ARM["ALPHA"])) + rotation
        beta = radians(randomizer.uniform(*NORD_EAST_ARM["BETA"])) + rotation
        gradient_range = NORD_EAST_ARM["GRADIENT_RANGE"]
        transparency = NORD_EAST_ARM["TRANSPARENCY"]
        levels = NORD_EAST_ARM["LEVELS"]
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta,
                                    gradient_range, transparency, levels)

        # SOUT EAST STAR
        high_range = [randomizer.uniform(*SOUTH_EAST_ARM["HIGH_MIN"]),
                      randomizer.uniform(*SOUTH_EAST_ARM["HIGH_MAX"])]
        alpha = radians(randomizer.uniform(*SOUTH_EAST_ARM["ALPHA"])) + rotation
        beta = radians(randomizer.uniform(*SOUTH_EAST_ARM["BETA"])) + rotation
        gradient_range = SOUTH_EAST_ARM["GRADIENT_RANGE"]
        transparency = SOUTH_EAST_ARM["TRANSPARENCY"]
        levels = SOUTH_EAST_ARM["LEVELS"]
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta,
                                    gradient_range, transparency, levels)

        # SOUT WEST STAR
        high_range = [randomizer.uniform(*SOUTH_WEST_ARM["HIGH_MIN"]),
                      randomizer.uniform(*SOUTH_WEST_ARM["HIGH_MAX"])]
        alpha = radians(randomizer.uniform(*SOUTH_WEST_ARM["ALPHA"])) + rotation
        beta = radians(randomizer.uniform(*SOUTH_WEST_ARM["BETA"])) + rotation
        gradient_range = SOUTH_WEST_ARM["GRADIENT_RANGE"]
        transparency = SOUTH_WEST_ARM["TRANSPARENCY"]
        levels = SOUTH_WEST_ARM["LEVELS"]
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta,
                                    gradient_range, transparency, levels)

        # NORD WEST STAR
        high_range = [randomizer.uniform(*NORD_WEST_ARM["HIGH_MIN"]),
                      randomizer.uniform(*NORD_WEST_ARM["HIGH_MAX"])]
        alpha = radians(randomizer.uniform(*NORD_WEST_ARM["ALPHA"])) + rotation
        beta = radians(randomizer.uniform(*NORD_WEST_ARM["BETA"])) + rotation
        gradient_range = NORD_WEST_ARM["GRADIENT_RANGE"]
        transparency = NORD_WEST_ARM["TRANSPARENCY"]
        levels = NORD_WEST_ARM["LEVELS"]
        self.draw_gradient_triangle(pos_x, pos_y, high_range, alpha, beta,
                                gradient_range, transparency, levels)

    def generate_symmetrical_stars(self):
        randomizer = ArtifactsGenerator.randomizer()

        # FIRST ELIPSE
        pos_x_1 = randomizer.uniform(*ARTIFACTS_ELIPSE["CIRCLE_POS_X_RANGE"])
        pos_y_1 = randomizer.uniform(*ARTIFACTS_ELIPSE["CIRCLE_POS_Y_RANGE"])
        radious_range = [randomizer.uniform(*ARTIFACTS_ELIPSE["RADIUS_MIN"]),
                         randomizer.uniform(*ARTIFACTS_ELIPSE["RADIUS_MAX"])]
        gradient_range = ARTIFACTS_ELIPSE["GRADIENT_RANGE"]
        transparency = ARTIFACTS_ELIPSE["TRANSPARENCY"]
        levels = ARTIFACTS_ELIPSE["LEVELS"]

        degree = randomizer.uniform(*STRIPES["DEGREE_FIRST"])
        self.generate_stripes(pos_x_1, pos_y_1, degree)
        self.draw_gradient_elipse(
            pos_x_1, pos_y_1, radious_range, gradient_range,
            transparency, levels)
        self.generate_star_arms(pos_x_1, pos_y_1)

        # SECOND ELIPSE
        pos_x_2 = pos_x_1 + randomizer.uniform(-2.0, 2.0)
        pos_y_2 = self.image.size[1] - pos_y_1 + randomizer.uniform(-2.0, 2.0)
        radious_range = [randomizer.uniform(*ARTIFACTS_ELIPSE["RADIUS_MIN"]),
                         randomizer.uniform(*ARTIFACTS_ELIPSE["RADIUS_MAX"])]
        gradient_range = ARTIFACTS_ELIPSE["GRADIENT_RANGE"]
        transparency = ARTIFACTS_ELIPSE["TRANSPARENCY"]
        levels = ARTIFACTS_ELIPSE["LEVELS"]
        degree = randomizer.uniform(*STRIPES["DEGREE_SECOND"])

        self.generate_stripes(pos_x_2, pos_y_2, degree)
        self.draw_gradient_elipse(
            pos_x_2, pos_y_2, radious_range, gradient_range,
            transparency, levels)
        self.generate_star_arms(pos_x_2, pos_y_2)
        return self.image

    def generate_stripes(self, pos_x, pos_y, degree):
        randomizer = self.randomizer()
        max_high = randomizer.uniform(*STRIPES["HIGH_MAX"])
        min_high = randomizer.uniform(*STRIPES["HIGH_MIN"])
        alpha = radians(degree)
        point_1 = pos_x + max_high * sin(alpha), pos_y - max_high * cos(alpha)

        all_xy = []
        for j in range(STRIPES["J"]):
            for i in range(STRIPES["I"]):
                alpha = radians(degree-STRIPES["D_DEGREE"]*i-STRIPES["D_DEGREE"]*STRIPES["I"]*j)
                point_1 = pos_x + max_high * sin(alpha), pos_y - max_high * cos(alpha)

                x_distance = pos_x - point_1[0]
                y_distnce = pos_y - (point_1[1]+i)
                dy = y_distnce/x_distance
                xn, yn = int(round(point_1[0])), int(round(point_1[1]))
                tmp = yn
                for i in range(int(round(x_distance))):
                    if (xn, yn) not in all_xy:
                        if (j % 2) == 0:
                            self.increase_pixel_value(xn, yn)
                        else:
                            self.decrease_pixel_value(xn, yn)
                    xn = xn + 1
                    tmp = tmp + dy
                    yn = int(round(tmp))
                    if xn > pos_x - min_high:
                        break

    def increase_pixel_value(self, x, y):
        pixels = self.image.load()
        B, T = pixels[x, y]
        B = B + STRIPES["INTENESITY"]
        if B > 255:
            B = 255
        pixels[x, y] = tuple([B, 255])

    def decrease_pixel_value(self, x, y):
        pixels = self.image.load()
        B, T = pixels[x, y]
        B = B - STRIPES["INTENESITY"]
        if B == 0:
            B = 0
        pixels[x, y] = tuple([B, 255])
