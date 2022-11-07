# as here for automation library
import pywhatkit
# for opening image from location
my_img_url = open(r'C:\Users\HP\Desktop\Aksh\Extra\New folder\my_practice_one\hookups\girls\girl (9).jpg', 'rb')
# to convert image into ascii art
pywhatkit.image_to_ascii_art(my_img_url, 'girl_art1')