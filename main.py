#!/usr/bin/env python3

import random
from master_thesis.image.MriImage import MriImage
from master_thesis.generator.ArtifactsGenerator import ArtifactsGenerator


mri_images_data = MriImage.load()
# Save clear data
MriImage.save(mri_images_data)

# Save generated data
for j, data in enumerate(mri_images_data):
    for i in range(1):
        ag = ArtifactsGenerator(data)
        gen_image = ag.generate()
        file_name = "images/generated/" + "sub-001-image-" + str(j) + "-" + "0" + ".png"
        gen_image.save(file_name)
