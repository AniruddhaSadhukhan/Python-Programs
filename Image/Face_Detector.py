import cv2
import glob2
list = glob2.glob("Images/*.jpg")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
#leye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")
#reye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")
#eyeglass_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
cv2.namedWindow("Detected Face",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Detected Face",750,750)
cv2.moveWindow("Detected Face",300,50)

for file in list:
	
	img = cv2.imread(file,1)
	grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(grey_img,
			scaleFactor = 1.05,
			minNeighbors = 5 )
			
	for x,y,w,h in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
		
		face_grey = grey_img[y:y+h, x:x+h]
		face = img[y:y+h, x:x+h]
		
#	eyes = eye_cascade.detectMultiScale(grey_img,1.05,3)
#	for ex,ey,ew,eh in eyes:
#		cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(3,0,0),1)

		
		
	cv2.imshow("Detected Face",img)
	cv2.waitKey(1000)
cv2.destroyAllWindows()
