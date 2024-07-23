import zipfile
import os
import cv2 as cv
from cv2.data import haarcascades
from PIL import Image
import pytesseract
import numpy as np
import PIL
from PIL import ImageOps, ImageDraw
import utils
import matplotlib.pyplot as plt


# open single image manipulation module
# loading the face detection classifier
# face_cascade = cv.CascadeClassifier(haarcascades + "haarcascade_frontalface_default.xml")

example_src = "static/img/sample-newspaper.png"

def extract_example(src): #src is an img
    face_cascade = cv.CascadeClassifier(haarcascades + "haarcascade_frontalface_default.xml")
    example_img = Image.open(src).convert('RGB')
    example_d = {'title': example_src, 'img': example_img, 'faces': [], 'text': ''}
    # example_d = {'title : example_src, 'img' : example_img, 'faces' : [img_face_1, img_face_2, ..], 'text': ['some text'}
    example_d['text'] = pytesseract.image_to_string(example_d['img'])
    img_np_array = np.array(example_d['img'])
    img_np_array_grey = cv.cvtColor(img_np_array, cv.COLOR_BGR2GRAY)
    face_boxes = face_cascade.detectMultiScale(img_np_array_grey, 1.3, 5)
    for x, y, w, h in face_boxes:
        face = example_d['img'].crop((x, y, x + w, y + h))
        example_d['faces'].append(face)
    return example_d
def make_cs_by_size(img_list, img_row_num, img_col_num): #specify appropriate size in multiple of img size, assuming len(img_list) is known
    for face in img_list:
        face.thumbnail((100, 100))
    h = img_list[0].height*img_row_num
    w = img_list[0].width*img_col_num
    contact_sheet = Image.new(img_list[0].mode, (w, h))
    x = 0
    y = 0
    for img in img_list:
        contact_sheet.paste(img, (x, y))
        if x + img_list[0].width == contact_sheet.width:
            x = 0
            y = y + img_list[0].height
        else:
            x = x + img_list[0].width
    return contact_sheet


def open_file_to_extract_text(src):
    with open(src, 'r') as f:
        return f.read()

# close single image manipulation module

# open zip file verification module
# close zip file verification module
# src_zip = (zipfile.ZipFile(example_src))
# def checkZipFile(usr, src): # src is a zipfile of .png or .jpg or .npy or .npy, usr is user id as str
#     UPLOAD_FOLDER = 'static/unzippedFiles'
#     current_usr_path = usr
#     usr_directory = os.path.join(os.path.join(UPLOAD_FOLDER, current_usr_path))
#     os.makedirs(usr_directory, exist_ok=True)
#     zip = zipfile.ZipFile(src, 'r')
#     zipFile_name = zip.filename
#     zip.


def make_dir_if_not_exist(username):
    current_dir = os.path.join('static/unzippedFiles', username)
    if not os.path.exists(current_dir):
        os.makedirs(current_dir, exist_ok=True)









