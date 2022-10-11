"Singleton class definition and basic configuration."

class Singleton(type):
    "Metaclass with the Singleton pattern."
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Config(metaclass=Singleton):
    MRI_IMAGES = {
        'PATHS': ['MRI_MSC_Dataset/sub-001/ses-1/anat/image-001.nii.gz',
         'MRI_MSC_Dataset/sub-002/ses-1/anat/image-002.nii.gz',
         'MRI_MSC_Dataset/sub-003/ses-1/anat/image-003.nii.gz',
         'MRI_MSC_Dataset/sub-004/ses-1/anat/image-004.nii.gz'],
        'EXTENTION': '.png',
        'PREFIX': 'sub-001-image-',
        'ORGINAL_DIR': 'images/orginal/sub-001/',
        'GENERATED_DIR': 'images/generated/',
    }

    ARTIFACTS = {
        'SEED': 32,
        'ROTATION': [0, 6.28]
    }

    ARTIFACTS_ELIPSE_BOTTOM = {
        'MIN_RADIUS': [1.5, 1.9],
        'MAX_RADIUS': [4.5, 5.1],
        'POS_X': [125.0, 135.0],
        'POS_Y': [137.0, 145.0],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_ELIPSE_TOP = {
        'MIN_RADIUS': [1.5, 1.9],
        'MAX_RADIUS': [4.5, 5.1],
        'POS_X': [125.0, 135.0],
        'POS_Y': [111.0, 119.0],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_NORD_ARM = {
        'MIN_HIGH': [3.5, 5],
        'MAX_HIGH': [10, 12],
        'ALPHA': [80, 75],
        'BETA': [105, 100],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_NORD_EAST_ARM = {
        'MIN_HIGH': [3.4, 5],
        'MAX_HIGH': [4, 5],
        'ALPHA': [155, 150],
        'BETA': [180, 170],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_SOUTH_EAST_ARM = {
        'MIN_HIGH': [3.5, 5],
        'MAX_HIGH': [10, 12],
        'ALPHA': [225, 220],
        'BETA': [250, 245],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_SOUTH_WEST_ARM = {
        'MIN_HIGH': [3.5, 5],
        'MAX_HIGH': [5, 8],
        'ALPHA': [295, 290],
        'BETA': [325, 320],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_NORD_WEST_ARM = {
        'MIN_HIGH': [3.5, 5],
        'MAX_HIGH': [10, 12],
        'ALPHA': [365, 360],
        'BETA': [395, 390],
        'GRADIENT_RANGE': [115, 255],
        'TRANSPARENCY': 255,
        'LEVELS': 15
    }

    ARTIFACTS_STRIPES_BOTTOM = {
        'INTENSITY': 11,
        'MAX_HIGH': [92, 89],
        'MIN_HIGH': [25, 20],
        'DEGREE': [308, 292],
        'D_DEGREE': 0.2,
        'J': 10,
        'I': 8,
    }

    ARTIFACTS_STRIPES_TOP = {
        'INTENSITY': 11,
        'MAX_HIGH': [92, 89],
        'MIN_HIGH': [25, 20],
        'DEGREE': [268, 252],
        'D_DEGREE': 0.2,
        'J': 10,
        'I': 8,
    }
