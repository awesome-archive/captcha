#!/usr/local/python3
#-*- encoding:utf-8 -*-

'''
    对于容易区分，没有干扰的数字和字母验证码，可以使用Tesseract识别

    psm:
        Page segmentation modes:
        0    Orientation and script detection (OSD) only.
        1    Automatic page segmentation with OSD.
        2    Automatic page segmentation, but no OSD, or OCR.
        3    Fully automatic page segmentation, but no OSD. (Default)
        4    Assume a single column of text of variable sizes.
        5    Assume a single uniform block of vertically aligned text.
        6    Assume a single uniform block of text.
        7    Treat the image as a single text line.
        8    Treat the image as a single word.
        9    Treat the image as a single word in a circle.
        10    Treat the image as a single character.
        11    Sparse text. Find as much text as possible in no particular order.
        12    Sparse text with OSD.
        13    Raw line. Treat the image as a single text line,
                                bypassing hacks that are Tesseract-specific.
    

'''
from pytesseract import *
from PIL import Image
import os

if __name__ == "__main__":
    image = Image.open(r'D://note//2.gif')
    image = image.convert('L')
    result = pytesseract.image_to_string(image,lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(result)