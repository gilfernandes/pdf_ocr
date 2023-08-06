
from pathlib import Path
from typing import List

from pdf2image import convert_from_path

from hr_image_ranker.config import cfg
from hr_image_ranker.log_init import logger
import cv2
import numpy as np

from PIL import PpmImagePlugin

def convert_image(pdf_file: Path) -> List[PpmImagePlugin.PpmImageFile]:
    images_from_path = convert_from_path(pdf_file, output_folder=cfg.image_location)
    return images_from_path


def save_image(im: PpmImagePlugin.PpmImageFile, target_path: Path):
    rgb_im = im.convert('RGB')
    rgb_im.save(target_path)


def convert_to_cv2_image(im: PpmImagePlugin.PpmImageFile) -> np.ndarray:
    pil_image = im.convert('RGB') 
    # Convert RGB to BGR 
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    

if __name__ == "__main__":
    for pdf in cfg.doc_location.glob("*.pdf"):
        logger.info("File: %s", pdf)
        images_from_path = convert_image(pdf)
        logger.info("Images: %s", type(images_from_path))
        logger.info("Images: %s", type(images_from_path[0]))
        for i, im in enumerate(images_from_path):
            save_image(im, cfg.image_location/f"{pdf.stem}_{i}.jpg")
            logger.info(type(convert_to_cv2_image(im)))