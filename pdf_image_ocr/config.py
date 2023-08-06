import os
from pathlib import Path

import pytesseract
from dotenv import load_dotenv

from pdf_image_ocr.log_init import logger

load_dotenv()

class Config():
    doc_location = Path(os.getenv("DOC_LOCATION"))
    image_location = Path(os.getenv("TEMP_IMG_PATH"))
    if not image_location.exists():
        image_location.mkdir(parents=True, exist_ok=True)

    if os.name == 'nt':
        logger.info("Windows detected!")
        pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_LOCATION')


cfg = Config()

if __name__ == "__main__":
    logger.info("Doc location: %s", cfg.doc_location)
    logger.info("Image location: %s", cfg.image_location)