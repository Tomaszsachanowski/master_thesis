#!/usr/bin/env python3


"""Singleton class definition and basic configuration"""


class Singleton(type):
    """Metaclass with the Singleton pattern"""
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Config(metaclass=Singleton):
    MRI_IMAGES = {
        "PATHS": ['MRI_MSC_Dataset/sub-001/ses-1/anat/image-001.nii.gz'],
        #  'MRI_MSC_Dataset/sub-002/ses-1/anat/image-002.nii.gz',
        #  'MRI_MSC_Dataset/sub-003/ses-1/anat/image-003.nii.gz',
        #  'MRI_MSC_Dataset/sub-004/ses-1/anat/image-004.nii.gz']
        "FORMAT": ".png",
        "PREFIX": "sub-001/sub-001-image-",
        "ORGINAL_DIR": "images/orginal/",
        "GENERATED_DIR": "images/generated/",
    }
    ARTIFACTS_ELIPSE = {
        "RANDOM_SEED": 32,
        "RADIUS_MIN": (1.5, 1.9),
        "RADIUS_MAX": (4.5, 5.1),
        "CIRCLE_POS_X_RANGE": [125.0, 135.0],
        "CIRCLE_POS_Y_RANGE": [137.0, 145.0],
        "TRANSPARENCY": 255,
        "GRADIENT_RANGE": [135, 255],
        "LEVELS": 15,
    }
    ARTIFACTS_NORD_ARM = {
        "HIGH_MIN": [3.5, 5],
        "HIGH_MAX": [10, 12],
        "ALPHA": [80, 75],
        "BETA": [105, 100],
        "GRADIENT_RANGE": [135, 255],
        "TRANSPARENCY": 255,
        "LEVELS": 15
    }
    ARTIFACTS_NORD_EAST_ARM = {
        "HIGH_MIN": [3.4, 5],
        "HIGH_MAX": [4, 5],
        "ALPHA": [155, 150],
        "BETA": [180, 170],
        "GRADIENT_RANGE": [135, 255],
        "TRANSPARENCY": 255,
        "LEVELS": 15
    }
    ARTIFACTS_SOUTH_EAST_ARM = {
        "HIGH_MIN": [3.5, 5],
        "HIGH_MAX": [10, 12],
        "ALPHA": [225, 220],
        "BETA": [250, 245],
        "GRADIENT_RANGE": [135, 255],
        "TRANSPARENCY": 255,
        "LEVELS": 15
    }
    ARTIFACTS_SOUTH_WEST_ARM = {
        "HIGH_MIN": [3.5, 5],
        "HIGH_MAX": [5, 8],
        "ALPHA": [295, 290],
        "BETA": [325, 320],
        "GRADIENT_RANGE": [135, 255],
        "TRANSPARENCY": 255,
        "LEVELS": 15
    }
    ARTIFACTS_NORD_WEST_ARM = {
        "HIGH_MIN": [3.5, 5],
        "HIGH_MAX": [10, 12],
        "ALPHA": [365, 360],
        "BETA": [395, 390],
        "GRADIENT_RANGE": [135, 255],
        "TRANSPARENCY": 255,
        "LEVELS": 15
    }
    ARTIFACTS_STRIPES = {
        "INTENESITY": 11,
        "HIGH_MAX": [92, 89],
        "HIGH_MIN": [25, 20],
        "DEGREE_FIRST": [308, 292],
        "DEGREE_SECOND": [268, 252],
        "D_DEGREE": 0.2,
        "J": 10,
        "I": 8,

    }
