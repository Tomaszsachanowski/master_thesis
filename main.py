#!/usr/bin/env python3

import random
from master_thesis.image.MriImage import MriImage
from master_thesis.generator.ArtifactsGenerator import ArtifactsGenerator
import numpy as np

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

mri_images_data = MriImage.load()
data = mri_images_data[100]
# print(np.info(data))
# img = Image.fromarray(data).convert("LA")

# # print(np.array(img))
# # img.save('my.png')
# img.show()

# plt.imshow(data)
# # plt.plot((0,255),(127, 127),color="r", linewidth=2)
# plt.show()

# # for i in range(100):
# #     plain = random.randint(98, 105)
# #     data = mri_images_data[plain]
ag = ArtifactsGenerator(data)
gen_image = ag.generate_symmetrical_elipses()
# #     file_name = "images/generated/" + "sub-001-image-" + str(i) +".png"
# #     gen_image.save(file_name)


# color = (255, 255, 255, 255)

# image = Image.new('RGBA', (200, 200))
# draw = ImageDraw.Draw(image)
# draw.ellipse((20, 20, 180, 180), fill = color, outline =color)

# image.show()