import pytesseract
from PIL import Image
from typing import Optional
from fastapi import FastAPI


# def return_text(image_path):
#     pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract'
#     result = pytesseract.image_to_string(image_path)
#     return result


app = FastAPI()


@app.get("/scan_image/{image_path}")
async def read_item(image_path: str):
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract'

    print(image_path)
    print('_________________')
    img = Image.open(image_path.replace('\\', '/'))
    result = pytesseract.image_to_string(img)
    print(result)
    return {"Menu": result}