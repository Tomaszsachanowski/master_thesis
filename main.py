#!/usr/bin/env python3

from master_thesis.image.MriImage import MriImage
import matplotlib.pyplot as plt
from PIL import Image

mri_images_data = MriImage.load()
data = mri_images_data[100]
plt.imshow(data, cmap="gray", origin="lower")
plt.plot((0,255),(127, 127),color="r", linewidth=2)
plt.show()
# MriImage.save(mri_images_data)
