#!/usr/bin/env python3

from master_thesis.image.MriImage import MriImage
import matplotlib.pyplot as plt
from PIL import Image

mri_images_data = MriImage.load()
MriImage.save(mri_images_data)
