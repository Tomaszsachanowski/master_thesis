#!/usr/bin/env python3

import random
from master_thesis.image.MriImage import MriImage
from master_thesis.generator.ArtifactsGenerator import ArtifactsGenerator


mri_images_data = MriImage.load()
data = mri_images_data[100]

for i in range(100):
    plain = random.randint(98, 105)
    data = mri_images_data[plain]
    ag = ArtifactsGenerator(data)
    gen_image = ag.generate_symmetrical_stars()
    file_name = "images/generated/" + "sub-001-image-" + str(i) + ".png"
    gen_image.save(file_name)
