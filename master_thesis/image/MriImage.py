import numpy as np

import nibabel as nib
import matplotlib.pyplot as plt

from config import Config

PATHS_MRI_IMAGE = Config.MRI_IMAGES["PATHS"]
FORMAT = Config.MRI_IMAGES["FORMAT"]
PREFIX = Config.MRI_IMAGES["PREFIX"]
ORGINAL_DIR = Config.MRI_IMAGES["ORGINAL_DIR"]


class MriImage:

    @staticmethod
    def load(paths=PATHS_MRI_IMAGE):
        """
        Method load all mri images from nifti files.

        Args:
            paths (list): Paths to the nifti files. Defaults to PATHS_MRI_IMAGE.

        Returns:
            list: List of nupy narray unit8 two dimention. 
        """        
        all_mri_images = []
        for path in paths:
            nifti1_image = nib.load(path)
            number_images = nifti1_image.shape[2] 
            nifiti_data =  nifti1_image.get_fdata()
            for i in range(number_images):
                image_float64 =  nifiti_data[:,:,i]
                image_uint8 = MriImage._convert(image_float64)
                all_mri_images.append(image_uint8)
        return all_mri_images

    @staticmethod
    def _convert(img_float64, type_min=0, type_max=255, target_type=np.uint8):
        """Convert narray from np.float64 to the np.unit8

        Args:
            img_float64 (np.narray): MRI image represented as numpy array
            type_min (int, optional): Min normalization value. Defaults to 0.
            type_max (int, optional): Max normalization value. Defaults to 255.
            target_type (np.uint8, optional): Dtype of narray. Defaults to np.uint8.

        Returns:
            np.narray: New narray with Dtype uint8
        """        
        imin = img_float64.min()
        imax = img_float64.max()

        a = (type_max - type_min) / (imax - imin)
        b = type_max - a * imax
        new_img_uint8 = (a * img_float64 + b).astype(target_type)
        return new_img_uint8

    @staticmethod
    def save(mri_images, images_dir=ORGINAL_DIR,
             prefix= PREFIX, format=FORMAT):
        """[summary]

        Args:
            mri_images (list): List of numpy narray unit8 two dimention. 
            images_dir (str, "images/orginal"): Path to the directory where the images will be saved. Defaults to ORGINAL_DIR.
            prefix (str, /sub-001/sub-001-image-): Prefix image filename. Defaults to PREFIX.
            format (str, .png): Image format. Defaults to FORMAT.
        """             
        for indx, data in enumerate(mri_images):
            file_path = images_dir + prefix + str(indx) + format
            plt.imsave(file_path, data, cmap="gray", origin="lower")
