""" 
Program to batch resize images
	by Aniruddha

Store originals images in Images folder
Resized images will be stored in Resized_Image folder
"""

import cv2
import glob2
list = glob2.glob("Images/*.jpg")
#print(list[0][7:-4])
for file in list:
	img = cv2.imread(file,1)
	resized_image = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
	new_file = "Resized_Image/"+file[7:-4]+"_resized.jpg"
	print(new_file)
	cv2.imwrite(new_file,resized_image)
	cv2.imshow("Slideshow",resized_image)
	cv2.waitKey(1500)
	cv2.destroyAllWindows()


