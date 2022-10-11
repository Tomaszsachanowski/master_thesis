from random import Random
from math import radians
from typing import Dict, Tuple

class Randomizer:
    def __init__(self, seed: int):
        self.__random = Random(seed)

    def randomize_star_arm(self, rotation: float, star_arm_param: Dict[str, Tuple[float, float]]) -> Dict[str, float]:
        """
        Randomize the star arm parameters within the given ranges and return values.
        Args:
            rotation (float): Rotation value between 0 and 6.28.
            star_arm_param (Dict[str, Tuple[float, float]]): Parameter ranges for randomization

        Returns:
            Dict[str, float]: Parameters randomized
        """
        high_range = [self.__random.uniform(*star_arm_param["MIN_HIGH"]),
                      self.__random.uniform(*star_arm_param["MAX_HIGH"])]
        alpha = radians(self.__random.uniform(*star_arm_param["ALPHA"])) + rotation
        beta = radians(self.__random.uniform(*star_arm_param["BETA"])) + rotation
        gradient_range = star_arm_param["GRADIENT_RANGE"]
        transparency = star_arm_param["TRANSPARENCY"]
        levels = star_arm_param["LEVELS"]
        return {
            'high_range': high_range,
            'alpha': alpha,
            'beta': beta,
            'gradient_range': gradient_range,
            'transparency': transparency,
            'levels': levels
        }
    
    def randomize_rotation(self, param: Dict[str, Tuple[float, float]]) -> float:
        """
        Randomize the rotation parameter within the given ranges and return value.

        Args:
            param ( Dict[str, Tuple[float, float]]): Parameter ranges for randomization

        Returns:
            float: Rotation value between 0 and 6.28.
        """        
        return self.__random.uniform(*param['ROTATION'])

    def randomize_elipse(self, elipse_param: Dict[str, Tuple[float, float]])-> Dict[str, float]:
        """
        Randomize the elipse parameters within the given ranges and return values.

        Args:
            elipse_param (Dict[str, Tuple[float, float]]): Parameter ranges for randomization

        Returns:
            Dict[str, float]: Parameters randomized
        """
        pos_x = self.__random.uniform(*elipse_param["POS_X"])
        pos_y = self.__random.uniform(*elipse_param["POS_Y"])
        radious_range = [self.__random.uniform(*elipse_param["MIN_RADIUS"]),
                         self.__random.uniform(*elipse_param["MAX_RADIUS"])]
        gradient_range = elipse_param["GRADIENT_RANGE"]
        transparency = elipse_param["TRANSPARENCY"]
        levels = elipse_param["LEVELS"]
        return {
            'pos_x': pos_x,
            'pos_y': pos_y,
            'radious_range': radious_range,
            'gradient_range': gradient_range,
            'transparency': transparency,
            'levels': levels
        }

    def randomize_stripes(self, stripes_param: Dict[str, Tuple[float, float]])-> Dict[str, float]:
        """
        Randomize the stripes parameters within the given ranges and return values.

        Args:
            stripes_param (Dict[str, Tuple[float, float]]): Parameter ranges for randomization

        Returns:
            Dict[str, float]: Parameters randomized
        """
        max_high = self.__random.uniform(*stripes_param['MAX_HIGH'])
        min_high = self.__random.uniform(*stripes_param['MIN_HIGH'])
        degree = self.__random.uniform(*stripes_param['DEGREE'])
        return {
            'max_high': max_high,
            'min_high': min_high,
            'degree': degree,
            'J': stripes_param['J'],
            'I': stripes_param['I'],
            'd_defree': stripes_param['D_DEGREE'],
            'intensity': stripes_param['INTENSITY']
        }
