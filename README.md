# Hook ups

## Discription

This is the system in which we search for a match for an image. We select a game for a person by using hash coding. We check the hash code difference between the two images. Image with a minimum contrast gets selected and finally shown.

##  Library used

**OS**: for using an operating system.

**Sys**: for providing various functions of the system.

**Glob**: used to return all file paths that match a specific pattern.

**Imagehash**: used to convert the Image into hash code.

**PIL**: Python Imaging Library (expansion of PIL) is an image processing package. It incorporates lightweight image processing tools that aid in editing, creating, and saving images.

## Execution Steps:


**Firstly, we run a file named resized1.py (that we used to resize all our images in a folder and change them into one extension like here it is .jpg).**

1.	Import the libraries.
2.	Give a path of a directory to a program.
3.	We use listdir to get the list of all files and directories in the specified directory.
4.	We make a function named resize () in which we run a for loop, and one by one, we select Image from the directory.
5.	In that, I use if loop, open that Image, and use the method splitext to split a string into text.
6.	Then, using the resize method, we resize our Image by giving the dimension we require (here, it is 400X400). (Here, one parameter given in resize is Image.ANTIALIAS that a technique used in digital imaging to reduce the visual defects that occur when high-resolution images are present in a lower resolution.)
7.	Here we are done and get our final resized Image in that directory.

**Secondly, we run our main program that is match.py, after resizing all our images.**

1.	Import the libraries.
2.	To open the Image (that we want to search for a perfect match for), we give a path of our directory to a program.
3.	We use the average_hash method from the image hash to get the hashcode of our Image.
4.	To extract the multiple files of the same pattern, we use glob. glob.
5.	We make a list named girls [0] and a variable named accepted_difference = 1000.
6.	Then we run a for loop to extract Images from a directory and get their hash code.
7.	We make a difference between the hashcode of the Image (that we want to search for a perfect match) and the images (in the directory we are finding).
8.	Then we use an if loop inside for loop and check the condition if (diff< accepted_diff) then that Image has been selected.
9.	Then we create a new frame to open both images and save them with a specific name (here, it is my_valentine_dat_date.jpg).
10.	Finally, we use img. show () to show or open that, Image.

</br>
</br>
</br>
</br>

<p align="center"><img width="493" alt="image" src="https://user-images.githubusercontent.com/72460920/186567929-fb1f2de0-9387-4132-8789-e2351f2a20e5.png"></p>
<p align="center"><img width="482" alt="image" src="https://user-images.githubusercontent.com/72460920/186567956-66647b19-3ee8-4ca2-bd42-78a69a0a71e7.png"></p>
<p align="center"><img width="474" alt="image" src="https://user-images.githubusercontent.com/72460920/186568406-2fb41642-2636-4f11-802e-f7203f20820b.png"></p>
<p align="center"><img width="474" alt="image" src="https://user-images.githubusercontent.com/72460920/186568551-d6e24bd8-76e1-48fb-b214-1d39e25f653f.png"></p>
<p align="center"><img width="478" alt="image" src="https://user-images.githubusercontent.com/72460920/186568805-87fe3d1c-2ab6-45f5-81a5-d864bcdfe11e.png"></p>
<p align="center"><img width="487" alt="image" src="https://user-images.githubusercontent.com/72460920/186568886-3d4a14dd-91e2-4bf2-9a94-f8e52cb663db.png"></p>
<p align="center"><img width="472" alt="image" src="https://user-images.githubusercontent.com/72460920/186568946-f70ef1e4-642a-4951-be57-d829213639ed.png"></p>
<p align="center"><img width="500" alt="image" src="https://user-images.githubusercontent.com/72460920/186568972-f61e82c3-f888-4af6-96b6-0928f6155f33.png"></p>



</br>
</br>

## Result

![my_valentine_day_date](https://user-images.githubusercontent.com/72460920/186495450-8e497f54-d9a3-46d8-aa24-6751197ce564.jpg)


</br>
</br>


https://user-images.githubusercontent.com/72460920/186495479-f58edaf9-29f2-4cb9-a1f8-102ddb9be2a0.mp4




