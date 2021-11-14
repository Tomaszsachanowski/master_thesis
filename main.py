from nibabel.nifti1 import load
from config import Config
from master_thesis.image.ImageLoader import ImageLoader
# PATHS_MRI_IMAGE = Config.MRI_IMAGES["PATHS"]


ImageLoader.load()
