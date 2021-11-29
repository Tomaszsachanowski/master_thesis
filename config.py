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
        "PATHS":['MRI_MSC_Dataset/sub-001/ses-1/anat/image-001.nii.gz',],
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
        "RADIUS_MIN": (1.5, 2.5),
        "RADIUS_MAX": (4.5, 6.5),
        "CIRCLE_POS_X_RANGE": [125.0, 135.0],
        "CIRCLE_POS_Y_RANGE": [137.0, 145.0],
        "TRANSPARENT_RANGE": [210, 255],
        "GRADIENT_RANGE": [100, 255],
        "LEVELS": 5,
    }
    ARTIFACTS_NORD_STAR = {
        "HIGH_MIN": [2, 4],
        "HIGH_MAX": [16, 19],
        "ALPHA": [80, 80],
        "BETA": [100, 110],
        "GRADIENT_RANGE": [110, 255],
        "TRANSPARENT_RANGE": [200, 255],
        "LEVELS": 20
    }
    ARTIFACTS_NORD_EAST_STAR = {
        "HIGH_MIN": [2, 3],
        "HIGH_MAX": [5, 9],
        "ALPHA": [150, 155],
        "BETA": [170, 180],
        "GRADIENT_RANGE": [120, 255],
        "TRANSPARENT_RANGE": [200, 255],
        "LEVELS": 10
    }
    ARTIFACTS_SOUTH_EAST_STAR = {
        "HIGH_MIN": [3, 5],
        "HIGH_MAX": [15, 19],
        "ALPHA": [220, 225],
        "BETA": [240, 250],
        "GRADIENT_RANGE": [120, 255],
        "TRANSPARENT_RANGE": [200, 255],
        "LEVELS": 20
    }
    ARTIFACTS_SOUTH_WEST_STAR = {
        "HIGH_MIN": [3, 5],
        "HIGH_MAX": [8, 10],
        "ALPHA": [290, 295],
        "BETA": [315, 325],
        "GRADIENT_RANGE": [110, 255],
        "TRANSPARENT_RANGE": [200, 255],
        "LEVELS": 10
    }
    ARTIFACTS_NORD_WEST_STAR = {
        "HIGH_MIN": [3, 5],
        "HIGH_MAX": [15, 19],
        "ALPHA": [360, 365],
        "BETA": [390, 400],
        "GRADIENT_RANGE": [120, 255],
        "TRANSPARENT_RANGE": [200, 255],
        "LEVELS": 10
    }