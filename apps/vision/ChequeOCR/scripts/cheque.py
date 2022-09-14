# import cv2
# import shutil
# import imutils
# from imutils import contours
# from PIL import Image
# import numpy as np
# import os
# # import tesserocr as tr
# import pytesseract as tr 
# import re 
# import os 
# import io 
# from google.cloud import vision 
# from matplotlib import pyplot as plt 
# import pandas as pd 
# from skimage.segmentation import clear_border
# from imutils import contours
# from keras.models import load_model
# #from .ext_ocr_details import *

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./../grand-sweep-361419-b243ddbf7782.json'
# print(cv2. __version__)
# def detect_text(path):
#     """Detects text in the file."""
#     from google.cloud import vision
#     import io
#     client = vision.ImageAnnotatorClient()

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.Image(content=content)

#     # en-t-i0-handwrit, mul-Latn-t-i0-handwrit

#     handwritten_image_context = vision.ImageContext(language_hints=['en-t-i0-handwrit'])


#     image_context = vision.ImageContext(language_hints=["en"])
#     response = client.document_text_detection(image=image, image_context=handwritten_image_context)
#     texts = response.text_annotations
#     print('Texts:')
#     # print(texts)
#     for text in texts:
#         print('\n"{}"'.format(text.description))

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])

#         print('bounds: {}'.format(','.join(vertices)))

#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))


# # detect_text('./../feilds/ac_no.jpg')
# detect_text('./../feilds/payee.jpg')

for i in range(10):
    print(i)
    if i==4:
        break