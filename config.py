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
    ARTIFACTS_GENERATOR = {
        "RANDOM_SEED": 32,
        "CIRCLE_RADIUS_MIN_MAX": (1.5, 3.0),
        "CIRCLE_POS_X_MIN_MAX": [125.0, 135.0],
        "CIRCLE_POS_Y_MIN_MAX": [130.0, 140.0],
    }