from pathlib import Path
from typing import List

from pdf_image_ocr.pdf2image_converter import convert_image, convert_to_cv2_image

import pytesseract
from PIL import PpmImagePlugin


def convert_img_to_text(pdf_file: Path) -> str:
    image_list: List[PpmImagePlugin.PpmImageFile] = convert_image(pdf_file)
    str_result = ""
    for image in image_list:
        nd_array = convert_to_cv2_image(image)
        str_result += pytesseract.image_to_string(nd_array)
        str_result += "\n\n"
    return str_result


if __name__ == "__main__":
    from pdf_image_ocr.config import cfg
    from pdf_image_ocr.log_init import logger
    for doc in cfg.doc_location.glob("*"):
        logger.info(doc)
        converted_text = convert_img_to_text(doc)
        logger.info(converted_text)
        logger.info("")
        break