# first we have to resize image in folder then

# used to return all file paths that match a specific pattern
import glob
# used to convert the image into hash code
import imagehash
# Python Imaging Library (expansion of PIL) is image processing package.
# It incorporates lightweight image processing tools that aids in editing, creating and saving images.
from PIL import Image
# import cv2
# im = cv2.imread('boy(7).jpg')

# to open the image
my_img_url = open(r'C:\Users\HP\Desktop\Aksh\Extra\New folder\my_practice_one\hookups\boys\boy (11).jpg', 'rb')
# my_img_url = 'boy(7).jpg'
# used to convert image into hash code
my_hash = imagehash.average_hash(Image.open(my_img_url))

# to extract the multiple files of same pattern
girls = glob.glob('./girls/*.jpg')

selected = girls[0]
# the difference accepted between two images
accepted_diff = 1000
# to extract all image files in folder
for girl in girls:
    # used to convert the images into hash code in folder
    girl_hash = imagehash.average_hash(Image.open(girl))
    diff = girl_hash - my_hash
    # checking the condition
    if diff < accepted_diff:
        selected = girl
        accepted_diff = diff
# to open the image
bf_img = Image.open(my_img_url)
gf_img = Image.open(selected)
# couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height + gf_img.height))
# to form a new image with some paremeters
couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
# used to paste the image into new frame
couple_img.paste(bf_img, (0, 0))
couple_img.paste(gf_img, (bf_img.width, 0))
# save thet image with this name in running directory
couple_img.save('my_valentine_day_date.jpg')
# used to show the image
couple_img.show()
