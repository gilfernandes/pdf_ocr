# PDF Image OCR

Provides utilities to extract text from PDFs, converting them to image and then using the Python library pytesseract to extract text from them.

# Pre-requisites


```
conda create -n langchain_hr_image_ranker python=3.11
conda activate langchain_hr_image_ranker
conda install -c conda-forge poppler
pip install pdf2image

pip install --force-reinstall \\wsl.localhost\Ubuntu\home\gilf\chainlit\src\dist\chainlit-0.6.1.1-py3-none-any.whl
pip install -e .
pip install langchain
pip install opencv-python
pip install black
conda install -c conda-forge pytesseract

```

Please make sure that you install the pytesseract library using the right method depending on your system.

On Windows you will need to install tesseract.exe on your local system and then set the location of this file in the .env file, like so:

```
TESSERACT_LOCATION=C:/Program Files/Tesseract-OCR/tesseract.exe
```

For more installation instructions, please check:

```
https://pypi.org/project/pytesseract/
```

# Configuration via .env file

The .env file should look like this:

```
# Document location for test purposes. This can be ignored
DOC_LOCATION=C:/development/playground/langchain/hr_candidate_ranker/data
# Used as a temporary directory
TEMP_IMG_PATH=C:/tmp/hr_image_ranker
# Location of the OCR programme used internally. Important for Windows
TESSERACT_LOCATION=C:/Program Files/Tesseract-OCR/tesseract.exe
```

# Building a wheel file

```
pip wheel .
```