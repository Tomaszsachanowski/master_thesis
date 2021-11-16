#!/usr/bin/env python3

from master_thesis.image.ImageLoader import ImageLoader
import matplotlib.pyplot as plt
from PIL import Image

mri_images_data = ImageLoader.load()

for indx, data in enumerate(mri_images_data):
    filename = "sub001-" +str(indx)
    plt.imsave(filename, data, cmap="gray", origin="lower", format="png")
# fig, ax = plt.subplots()
# ax.imshow(mri_images_data[0], cmap="gray", origin="lower")
# plt.show()
