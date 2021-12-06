#!/usr/bin/env python3

import random
from master_thesis.image.MriImage import MriImage
from master_thesis.generator.ArtifactsGenerator import ArtifactsGenerator


mri_images_data = MriImage.load()
data = mri_images_data[100]

for j in range(60, 110):
    for i in range(5):
        # plain = random.randint(98, 105)
        data = mri_images_data[j]
        ag = ArtifactsGenerator(data)
        gen_image = ag.generate()
        file_name = "images/generated/" + "sub-001-image-" + str(j) + "-" + str(i) + ".png"
        gen_image.save(file_name)
