#!/usr/bin/python
# image processing library
from PIL import Image
# for using operating system
# for providing various function of system
import os, sys

# path of folder enter to resize
path = "C:\\Users\\HP\\Desktop\\Aksh\\Extra\\New folder\\my_practice_one\\hookups\\boys\\"

dirs = os.listdir( path )

# function to resize
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            # properties as we want from our image
            imResize = im.resize((400,400), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()