# first we have to resize image in folder then

import glob
import imagehash
from PIL import Image
import cv2


# import cv2
# im = cv2.imread('boy(7).jpg')

print("Enter 1 for Male.")
print("Enter 2 for female.")
choice = int(input("Please enter your gender:"))


if choice == 1:
    n = int(input("Please enter the serial number of your image you want to enter:"))
    boys = glob.glob('./boys/*.jpg')

    image_list = []
    for filename in glob.glob('./boys/*.jpg'):
        im = Image.open(filename)
        image_list.append(im)

    final_image = image_list[n+1]
    cv2.imshow("Image req", final_image)

    # my_img_url = open(r'C:\Users\HP\Desktop\Aksh\Extra\New folder\my_practice_one\hookups\boys\boy (7).jpg).jpg', 'rb')
# my_img_url = 'boy(7).jpg'
    my_hash = imagehash.average_hash(Image.open(final_image))

    girls = glob.glob('./girls/*.jpg')
    selected = girls[0]
    accepted_diff = 1000
    for girl in girls:
        girl_hash = imagehash.average_hash(Image.open(girl))
        diff = girl_hash - my_hash
        if diff < accepted_diff:
            selected = girl
            accepted_diff = diff

    bf_img = Image.open(final_image)
    gf_img = Image.open(selected)
    # couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height + gf_img.height))
    couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
    couple_img.paste(bf_img, (0, 0))
    couple_img.paste(gf_img, (bf_img.width, 0))
    couple_img.save('my_valentine_day_date.jpg')
    couple_img.show()




elif choice == 2:
    n = int(input("Please enter the serial number of your image you want to enter:"))
    my_img_url = open(r'C:\Users\HP\Desktop\Aksh\Extra\New folder\my_practice_one\hookups\girls\girl (n).jpg', 'rb')
    # my_img_url = 'boy(7).jpg'
    my_hash = imagehash.average_hash(Image.open(my_img_url))

    boys = glob.glob('./boys/*.jpg')
    selected = boys[0]
    accepted_diff = 1000
    for boy in boys:
        boy_hash = imagehash.average_hash(Image.open(boy))
        diff = boy_hash - my_hash
        if diff < accepted_diff:
            selected = boy
            accepted_diff = diff

    gf_img = Image.open(my_img_url)
    bf_img = Image.open(selected)
# couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height + gf_img.height))
    couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
    couple_img.paste(gf_img, (0, 0))
    couple_img.paste(bf_img, (gf_img.width, 0))
    couple_img.save('my_valentine_day_date.jpg')
    couple_img.show()





