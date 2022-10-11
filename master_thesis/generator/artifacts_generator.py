
from math import radians, sin, cos
from numpy import round
from PIL import Image, ImageDraw

from .randomizer import Randomizer
from config import Config

ARTIFACTS = Config.ARTIFACTS
ARTIFACTS_ELIPSE_BOTTOM = Config.ARTIFACTS_ELIPSE_BOTTOM
ARTIFACTS_ELIPSE_TOP = Config.ARTIFACTS_ELIPSE_TOP
NORD_ARM = Config.ARTIFACTS_NORD_ARM
NORD_EAST_ARM = Config.ARTIFACTS_NORD_EAST_ARM
SOUTH_EAST_ARM = Config.ARTIFACTS_SOUTH_EAST_ARM
SOUTH_WEST_ARM = Config.ARTIFACTS_SOUTH_WEST_ARM
NORD_WEST_ARM = Config.ARTIFACTS_NORD_WEST_ARM
ARTIFACTS_STRIPES_BOTTOM = Config.ARTIFACTS_STRIPES_BOTTOM
ARTIFACTS_STRIPES_TOP = Config.ARTIFACTS_STRIPES_TOP


class ArtifactsGenerator:
    def __init__(self, data_img, randomizer: Randomizer = Randomizer(ARTIFACTS['SEED'])):
        self.image = Image.fromarray(data_img[:, :]).convert('LA')
        self.__randomizer = randomizer

    def __draw_gradient_elipse(self, pos_x, pos_y, radious_range,
                               gradient_range, transparency, levels) -> None:
        """
        Draw the gradient elipse.

        Args:
            pos_x (_type_):  X position of the star.
            pos_y (_type_):  Y position of the star.
            radious_range (_type_): Radious range.
            gradient_range (_type_): Gradient range.
            transparency (_type_): Transparency.
            levels (_type_): Levels.
        """
        gradient_min, gradient_max = gradient_range
        radious_min, radious_max = radious_range

        gradient_step = float(gradient_max - gradient_min)/levels
        radious_step = float(radious_max - radious_min)/levels

        for i in range(1, levels+1, 1):
            elipse_x_0 = pos_x - (radious_max - radious_step*i)
            elipse_x_1 = pos_x + (radious_max - radious_step*i)
            elipse_y_0 = pos_y - (radious_max - radious_step*i)
            elipse_y_1 = pos_y + (radious_max - radious_step*i)
            color = (int(gradient_min + gradient_step*i), transparency)

            image_draw_elipse = ImageDraw.Draw(self.image)
            image_draw_elipse.ellipse(
                (elipse_x_0, elipse_y_0, elipse_x_1, elipse_y_1),
                fill=color, outline=color)

    def __draw_gradient_triangle(self, pos_x, pos_y, high_range, alpha, beta,
                                 gradient_range, transparency, levels) -> None:
        """
        Draw the gradient arms of the star (trinagle).

        Args:
            pos_x (_type_):  X position of the star.
            pos_y (_type_):  Y position of the star.
            high_range (_type_): High range.
            alpha (_type_): alpha angle of the trinagle.
            beta (_type_): beta angle of the trinagle.
            gradient_range (_type_): Gradient range.
            transparency (_type_): Transparency.
            levels (_type_): Levels.
        """
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

    def __draw_star_arms(self, pos_x, pos_y) -> None:
        """
        Draw the five arms of the star.

        Args:
            pos_x (int): X position of the star.
            pos_y (int): Y position of the star.
        """
        rotation = self.__randomizer.randomize_rotation(ARTIFACTS)
        # NORD STAR ARM
        nord_star_arm =  self.__randomizer.randomize_star_arm(
            rotation, NORD_ARM)
        self.__draw_gradient_triangle(pos_x, pos_y, **nord_star_arm)
        # NORD EAST STAR
        nord_east_star_arm =  self.__randomizer.randomize_star_arm(
            rotation, NORD_EAST_ARM)
        self.__draw_gradient_triangle(pos_x, pos_y, **nord_east_star_arm)
        # SOUT EAST STAR
        south_east_star_arm =  self.__randomizer.randomize_star_arm(
            rotation, SOUTH_EAST_ARM)
        self.__draw_gradient_triangle(pos_x, pos_y, **south_east_star_arm)
        # SOUTH WEST STAR
        south_west_star_arm =  self.__randomizer.randomize_star_arm(
            rotation, SOUTH_WEST_ARM)
        self.__draw_gradient_triangle(pos_x, pos_y, **south_west_star_arm)
        # NORD WEST STAR
        nord_west_star_arm =  self.__randomizer.randomize_star_arm(
            rotation, NORD_WEST_ARM)
        self.__draw_gradient_triangle(pos_x, pos_y, **nord_west_star_arm)

    def __draw_stripes(self, pos_x, pos_y, degree, max_high,
                       min_high, J, I, d_defree, intensity) -> None:
        """
        Draw light and dark radial stripes alternately.

        Args:
            pos_x (int): X position of the star.
            pos_y (int): Y position of the star.
            degree (int): The angle of the start of the stripes.
        """
        alpha = radians(degree)
        point_1 = pos_x + max_high * sin(alpha), pos_y - max_high * cos(alpha)

        all_xy = []
        for j in range(J):
            for i in range(I):
                alpha = radians(degree-d_defree*i-d_defree*I*j)
                point_1 = pos_x + max_high * sin(alpha), pos_y - max_high * cos(alpha)

                x_distance = pos_x - point_1[0]
                y_distnce = pos_y - (point_1[1]+i)
                dy = y_distnce/x_distance
                xn, yn = int(round(point_1[0])), int(round(point_1[1]))
                tmp = yn
                for i in range(int(round(x_distance))):
                    if (xn, yn) not in all_xy:
                        if (j % 2) == 0:
                            self.__increase_pixel_value(xn, yn, intensity)
                        else:
                            self.__decrease_pixel_value(xn, yn, intensity)
                    xn = xn + 1
                    tmp = tmp + dy
                    yn = int(round(tmp))
                    if xn > pos_x - min_high:
                        break

    def __increase_pixel_value(self, pos_x, pos_y, intensity) -> None:
        """
        Increases the pixel value.
        Transparency remains at the level of max.

        Args:
            pos_x (int): Pixel x position.
            pos_y (int): Pixel y position.
            intensity (int): Change the intensity.

        """
        # load image as pixels array
        pixels = self.image.load()
        # get pixel values
        B, T = pixels[pos_x, pos_y]
        # increase pixel value
        B = B + intensity
        if B > 255:
            B = 255
        pixels[pos_x, pos_y] = tuple([B, 255])

    def __decrease_pixel_value(self, pos_x, pos_y, intensity) -> None:
        """
        Decreases the pixel value.
        Transparency remains at the level of min

        Args:
            pos_x (int): Pixel x position.
            pos_y (int): Pixel y position.
            intensity (int): Change the intensity.
        """
        # load image as pixels array
        pixels = self.image.load()
        # get pixel values
        B, T = pixels[pos_x, pos_y]
        # decrease pixel value
        B = B - intensity
        if B == 0:
            B = 0
        pixels[pos_x, pos_y] = tuple([B, 255])

    def generate(self) -> ImageDraw:
        """
        Generate artificats.

        Returns:
            ImageDraw: Created image with artificats.
        """

        # BOTTOM ARTIFACTS
        elipse_bottom = self.__randomizer.randomize_elipse(ARTIFACTS_ELIPSE_BOTTOM)
        stripes_bottom = self.__randomizer.randomize_stripes(ARTIFACTS_STRIPES_BOTTOM)
        self.__draw_stripes(elipse_bottom['pos_x'], elipse_bottom['pos_y'], **stripes_bottom)
        self.__draw_gradient_elipse(**elipse_bottom)
        self.__draw_star_arms(elipse_bottom['pos_x'], elipse_bottom['pos_y'])

        # TOP ARTIFACTS
        elipse_top = self.__randomizer.randomize_elipse(ARTIFACTS_ELIPSE_TOP)
        stripes_top = self.__randomizer.randomize_stripes(ARTIFACTS_STRIPES_TOP)
        self.__draw_stripes(elipse_top['pos_x'], elipse_top['pos_y'], **stripes_top)
        self.__draw_gradient_elipse(**elipse_top)
        self.__draw_star_arms(elipse_top['pos_x'], elipse_top['pos_y'])

        return self.image
