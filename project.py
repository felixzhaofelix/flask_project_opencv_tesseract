# Pillow, OpenCV, and Pytesseract

# Task: Write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza".
# 
# Size of images folder: ~200 MB
import zipfile
import os
import cv2 as cv
from cv2.data import haarcascades
from PIL import Image
import pytesseract
import numpy as np
import PIL
from PIL import ImageOps, ImageDraw


# loading the face detection classifier
face_cascade = cv.CascadeClassifier(haarcascades + "haarcascade_frontalface_default.xml")

proces_img = {} # a dictionary

# open every image save them in the dict proces_img under key proces_img[img]
small_zip = zipfile.ZipFile('static/zippedFiles/small_img.zip', 'r')
for member in small_zip.infolist():
    file = small_zip.open(member)
    image = Image.open(file).convert('RGB')
    proces_img[member.filename] = {'img': image}
# proces_img's data structure:
# proces_img = {"image1" : {'img' : image, 'text' : 'text_body', 'faces' : [PIL.Image.Image object of face]} , item_dictionary_2, ....}

#visualize the images that are converted np.array
# i=1
# for img in proces_img:
#     print(proces_img[img]['img'])
#     cv.imshow(f"img{i} in RGB", np.array(proces_img[img]['img']))
#     i+=1
#     cv2.waitKey(0)
# cv2.destroyAllWindows()
def run_small():
    proces_img = {}
    small_zip = zipfile.ZipFile('static/zippedFiles/small_img.zip', 'r')
    for member in small_zip.infolist():
        file = small_zip.open(member)
        image = Image.open(file).convert('RGB')
        proces_img[member.filename] = {'img': image}
    show_all_image(proces_img)


def show_all_image(proces_img):
    i = 1
    for img in proces_img:
        print(proces_img[img]['img'])
        cv.imshow(f"img{i} in RGB", np.array(proces_img[img]['img']))
        i += 1
        cv.waitKey(0)
    cv.destroyAllWindows()


# show_all_image(proces_img)


#run tessaract on every image for text recognition and save them in the dict proces_img under key proces_img[img]['text']
# for img in proces_img.keys():
#     text = pytesseract.image_to_string(proces_img[img]['img'])
#     proces_img[img]['text'] = text
#
#
#run openCV on every image for face recognition and save them in the dict proces_img under key proces_img[img]['face']
#img = proces_img['a-0.png']['img']
# for imgTitle in proces_img.keys():
#     cv_img = np.array(proces_img[imgTitle]['img']) #returns a ndarray from img in RGB mode
#     cv_img_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY) #convert the ndarray from RGB to grayscale
#     face_boxes = face_cascade.detectMultiScale(cv_img_gray, 1.3, 5)
#     proces_img[imgTitle]['faces'] = []
#     for x, y, w, h in face_boxes:
#         face = proces_img[imgTitle]['img'].crop((x, y, x+w, y+h))
#         proces_img[imgTitle]['faces'].append(face)
#
#


# make fake face img for testing
# image_test = Image.open('static/img/emoji1.png')
#
# # Assign the same image_test to all faces lists directly
# for img in proces_img:
#     proces_img[img]['faces'] = [image_test, image_test]  # Use a list containing the image_test

# open FINAL

directory = 'static/unzippedFiles/small/'
directory_text = 'static/unzippedFiles/small/small_text/'
directory_faces = 'static/unzippedFiles/small/small_faces/'
#
# Create the directory if it doesn't exist
os.makedirs(directory_faces, exist_ok=True)  # Handles cases where directory might already exist
os.makedirs(directory_text, exist_ok=True)

# store opencv result as files:
# f_title_num = 0
# for img_title in proces_img:
#     # Construct subdirectory path using string formatting
#     subdirectory = os.path.join(directory_faces, f"{img_title}")
#     os.makedirs(subdirectory, exist_ok=True)
#
#     f_face_num = 0
#     for face in proces_img[img_title]['faces']:
#         # Save face image with proper path construction
#         face.save(os.path.join(subdirectory, f"{img_title}_face_{f_face_num}.png"))
#         f_face_num += 1
#     f_title_num += 1

# #read tesseract results from files
# t_num = 0
# for img in proces_img:
#     with open (os.path.join(directory_text, f'small_text_{t_num}'), 'r') as f:
#         proces_img[img]['text'] = f.read()
#         print(list(proces_img.keys())[t_num] + ': ' + proces_img[img]['text'][:10])
#     t_num += 1
#
# # #store tessaract result as files:
# t_num = 0
# for img_title in proces_img:
#     with open (os.path.join(directory_text, f'small_text_{t_num}'), 'w') as f:
#         f.write(proces_img[img_title]['text'])
#     t_num += 1
# close FINAL

# #resize all faces to a 100x100 size with Image.thumbnail
# for img_title in proces_img:
#     for face in proces_img[img_title]['faces']:
#         face.thumbnail((100, 100))
#
#
# # In[18]:
#
#
# #define make contact sheet function
# def make_cs(img_list):
#     img_num = len(img_list)
#     if img_num%5 == 0:
#         h = (int(img_num/5))*img_list[0].height
#     else:
#         h = (int(img_num/5)+1)*img_list[0].height
#     w = img_list[0].width*5
#     contact_sheet = Image.new(img_list[0].mode, (w, h))
#     x = 0
#     y = 0
#     for img in img_list:
#         contact_sheet.paste(img, (x, y))
#         if x + img_list[0].width == contact_sheet.width:
#             x = 0
#             y = y + img_list[0].height
#         else:
#             x = x + img_list[0].width
#     return contact_sheet
#
#
#
# # In[40]:
#
#
# #add a title key for items in dictionary
# num = 0
# for img_title in proces_img:
#     proces_img[img_title]['title'] = list(proces_img.items())[num][0]
#     num += 1
#
#
# # In[53]:
#
#
# #define search function
# def search(kwd):
#     img_list = []
#     rslt_str = 'Results found in file '
#     no_str = 'But there were no faces in that file!'
#     for img_title in proces_img:
#         if kwd in proces_img[img_title]['text'] and len(proces_img[img_title]['faces']) != 0:
#             print(rslt_str + proces_img[img_title]['title'])
#             display(make_cs(proces_img[img_title]['faces']))
#         elif kwd in proces_img[img_title]['text']:
#             print(rslt_str + proces_img[img_title]['title'])
#             print(no_str)
#
#
#
# # In[ ]:
#
#
# #proces_img has 4 keys: img_title
# #each img_title has 4 dict: 'img' and 'text' and 'faces' and 'title'
# #each 'title' key stores the filename as string
# #each 'img' key stores one image in RGB, <'class 'PIL.Image.Image'>
# #each 'text' key stores a string of all text extracted from the image
# #each 'faces'key stores a list of RGB PIL Image of faces of each image in the 'img' key under the same img_title
#
#
# # In[48]:
#
#
# search('Christopher') #in small_img.zip
#
#
# # In[50]:
#
#
# #open every image save them in the dict proces_img under key proces_img[img]
# small_zip = zippedFiles.ZipFile('readonly/images.zip', 'r')
# for member in small_zip.infolist():
#     file = small_zip.open(member)
#     image = Image.open(file).convert('RGB')
#     proces_img[member.filename] = {'img': image}
# #run tesseract on every image for text recognition and save them in the dict proces_img under key proces_img[img]['text']
# for img in proces_img.keys():
#     text = pytesseract.image_to_string(proces_img[img]['img'])
#     proces_img[img]['text'] = text
#
#
#
#
# #run openCV on every image for face recognition and save them in the dict proces_img under key proces_img[img]['face']
# for imgTitle in proces_img.keys():
#     cv_img = np.array(proces_img[imgTitle]['img']) #returns a ndarray from img in RGB mode
#     cv_img_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY) #convert the ndarray from RGB to grayscale
#     face_boxes = face_cascade.detectMultiScale(cv_img_gray, 1.3, 5)
#     proces_img[imgTitle]['faces'] = []
#     for x, y, w, h in face_boxes:
#         face = proces_img[imgTitle]['img'].crop((x, y, x+w, y+h))
#         proces_img[imgTitle]['faces'].append(face)
# #resize all faces to a 100x100 size with Image.thumbnail
# for img_title in proces_img:
#     for face in proces_img[img_title]['faces']:
#         face.thumbnail((100, 100))
# #add a title key for items in dictionary
# num = 0
# for img_title in proces_img:
#     proces_img[img_title]['title'] = list(proces_img.items())[num][0]
#     num += 1
#
#
#
#
# search('Mark') #in images.zip

