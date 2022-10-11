import os
from typing import List
import matplotlib.pyplot as plt
import numpy as np

import nibabel as nib

from config import Config

MRI_IMAGE_PATH = Config.MRI_IMAGES["PATHS"][0]
EXTENTION = Config.MRI_IMAGES["EXTENTION"]
PREFIX = Config.MRI_IMAGES["PREFIX"]
ORGINAL_DIR = Config.MRI_IMAGES["ORGINAL_DIR"]


class MriImage:

    @staticmethod
    def load(mri_path: str = MRI_IMAGE_PATH) -> np.ndarray:
        """
        Load a MRI image from the given path.
        Returns a np.ndarray data.

        Args:
            mri_path (str, optional): Path to the MRI image.
                Defaults to MRI_MSC_Dataset/sub-001/ses-1/anat/image-001.nii.gz.

        Returns:
            np.ndarray: MRI image data.
        """        
        
        mmri_image = nib.load(mri_path)
        mri_data = mmri_image.get_fdata()
        return mri_data

    @staticmethod
    def slice(mri_data: np.ndarray, axis: int = 2) -> List[np.ndarray]:
        """
        Slice the MRI data into images in a given plane.

        Args:
            mri_data (np.ndarray): MRI image data.
            axis (int, optional): The axis to be rolled.
                The positions of the other axes do not change
                relative to one another. Defaults to 2.

        Returns:
            List[np.array]: List of mri image slices.
        """   
        
        mri_image_slices = []
        for image_data in np.rollaxis(mri_data, 2):
                image_uint8 = MriImage._convert(image_data)
                mri_image_slices.append(image_uint8)
        return mri_image_slices

    @staticmethod
    def _convert(img_float64: np.ndarray, type_min: int = 0,
                 type_max: int = 255, target_type: np.dtype = np.uint8) -> np.ndarray:
        """
        Convert narray from np.float64 to the np.unit8.

        Args:
            img_float64 (np.ndarray): MRI image slice represented as numpy array.
            type_min (int, optional): Min normalization value. Defaults to 0.
            type_max (int, optional): Max normalization value. Defaults to 255.
            target_type (np.uint8, optional): Dtype of narray. Defaults to np.uint8.

        Returns:
            np.narray: New  MRI image slice represented as numpy array with Dtype uint8.
        """
        imin = img_float64.min()
        imax = img_float64.max()

        a = (type_max - type_min) / (imax - imin)
        b = type_max - a * imax
        new_img_uint8 = (a * img_float64 + b).astype(target_type)
        return new_img_uint8

    @staticmethod
    def save(mri_image_slices: List[np.ndarray], output_dir: str = ORGINAL_DIR,
             prefix: str = PREFIX, extention: str = EXTENTION) -> None:
        """
        Args:
            mri_image_slices ( List[np.ndarray]): List of mri image slices 
                represented as numpy array with Dtype uint8. 
            output_dir (str, optional): Path to the directory where the
                images will be saved. Defaults to 'images/orginal/sub-001'.
            prefix (str, orginal): Prefix for  filename.
                Defaults to "sub-001-image-".
            extention (str, .png): Image extention. Defaults to '.png'.
        """
        for indx, data in enumerate(mri_image_slices):
            path = os.path.join(
                output_dir, f"{prefix}{str(indx)}{extention}" )
            plt.imsave(path, data, cmap="gray", origin="lower")


if __name__ == "__main__":
    a = MriImage.load()
    print(a.shape)
    b = MriImage.slice(a)
    for i in b:
        print(i.shape)
    MriImage.save(b)
