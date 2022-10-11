#!/usr/bin/env python3
import os

from config import Config
from master_thesis.image.MriImage import MriImage
from master_thesis.generator.artifacts_generator import ArtifactsGenerator


MRI_IMAGE_PATH = Config.MRI_IMAGES["PATHS"][0]
EXTENTION = Config.MRI_IMAGES["EXTENTION"]
PREFIX = Config.MRI_IMAGES["PREFIX"]
GENERATED_DIR = Config.MRI_IMAGES["GENERATED_DIR"]


if __name__ == '__main__':
    a = MriImage.load(MRI_IMAGE_PATH)
    b = MriImage.slice(a)
    for j in range(60, 110):
        for i in range(5):
            data = b[j]
            ag = ArtifactsGenerator(data)
            gen_image = ag.generate()
            file_name = os.path.join(
                GENERATED_DIR, f"{PREFIX}{str(j)}-{str(i)}{EXTENTION}" )
            gen_image.save(file_name)
