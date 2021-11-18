#!/usr/bin/env python3

import random
from master_thesis.image.MriImage import MriImage
from master_thesis.generator.ArtifactsGenerator import ArtifactsGenerator

# import matplotlib.pyplot as plt
from PIL import Image

mri_images_data = MriImage.load()
# data = mri_images_data[100]
# plt.imshow(data, cmap="gray", origin="lower")
# plt.plot((0,255),(127, 127),color="r", linewidth=2)
# plt.show()
for i in range(100):
    plain = random.randint(98, 105)
    data = mri_images_data[plain]
    ag = ArtifactsGenerator(data)
    gen_image = ag.generate_symmetrical_elipses()
    file_name = "images/generated/" + "sub-001-image-" + str(i) +".png"
    gen_image.save(file_name)

# data = mri_images_data[100]
# plt.imshow(data, cmap="gray", origin="lower")
# plt.plot((0,255),(127, 127),color="r", linewidth=2)
# plt.show()
# ag.generate_symmetrical_circles()
# ag.generate_symmetrical_circles()
# ag.generate_symmetrical_circles()

# MriImage.save(mri_images_data)
