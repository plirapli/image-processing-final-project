import cv2
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.model_selection import GridSearchCV

# Load Gambar 
def import_image(file) :
    image = cv2.imread(file)
    return image

# Equalizing (Normalisasi)
def equalizing(img):
    img = cv2.equalizeHist(img)
    return img

# Grayscaling using luminosity method
def grayscaling(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

def unsharpMaskingAndHighboostFiltering(img):
    k = 8
    img = img.reshape(img.shape[0], img.shape[1], 1)
    # Kedua, ini ceritanya diblur pake gaussian blur
    blur = cv2.GaussianBlur(img, (5,5), 0)
    blur = blur.reshape(blur.shape[0], blur.shape[1], 1)
    # Ketiga, hasil gambar blur tadi dipake buat ngurangin gambar asli
    mask = img - blur
    # Terakhir, gambar original tadi ditambah sama gambar hasil pengurangannya
    final = img + k * mask
    return final

def prep_image(image, save_path=None):
    img = grayscaling(image)
    # img = equalizing(img)
    # img = high_boost(img)
    img = cv2.GaussianBlur(img, (5,5), 0)
    img = unsharpMaskingAndHighboostFiltering(img)
    img = cv2.medianBlur(img, 5)

    # Save the processed image
    if save_path:
        cv2.imwrite(save_path, img)
    return img

def prep_image_1(image, save_path=None):
    img = grayscaling(image)

    # Save the processed image
    if save_path:
        cv2.imwrite(save_path, img)
    return img

def prep_image_2(image, save_path=None):
    img = cv2.GaussianBlur(image, (5,5), 0)

    # Save the processed image
    if save_path:
        cv2.imwrite(save_path, img)
    return img

def prep_image_3(image, save_path=None):
    img = unsharpMaskingAndHighboostFiltering(image)

    # Save the processed image
    if save_path:
        cv2.imwrite(save_path, img)
    return img

def prep_image_4(image, save_path=None):
    img = cv2.medianBlur(image, 5)

    # Save the processed image
    if save_path:
        cv2.imwrite(save_path, img)
    return img
