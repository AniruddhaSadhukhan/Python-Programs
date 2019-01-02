import cv2

vid = cv2.VideoCapture("http://192.168.43.1:8080/videofeed")


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def face_video():
	
	while True:
		check,img = vid.read()
		grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		#time.sleep(3)
		faces = face_cascade.detectMultiScale(grey_img,
					scaleFactor = 1.1,
					minNeighbors = 5 )
		for x,y,w,h in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
		cv2.imshow("Detected Face",img)
		cv2.namedWindow("Detected Face",cv2.WINDOW_NORMAL)
		cv2.resizeWindow("Detected Face",750,750)
		cv2.moveWindow("Detected Face",300,50)

		while cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) > 0:
			cv2.waitKey(1)
			if cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) < 1:
				return
			break		
	cv2.destroyAllWindows()
		
face_video()
vid.release()
