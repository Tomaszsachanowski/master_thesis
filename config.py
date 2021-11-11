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
        "PATH": 'MRI_MSC_Dataset/sub-001/ses-1/anat/sub-001.nii.gz'
    }
