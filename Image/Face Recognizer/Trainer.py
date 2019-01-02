import cv2
import glob2
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askdirectory


path = ""

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

def training(dir_path):
	train_list = glob2.glob(dir_path)
	
	all_names=[]
	try:
		face_recognizer.read("trained_data.xml")
		
		dict = {}
		for i in face_recognizer.getLabels():
			dict[i[0]]=face_recognizer.getLabelInfo(i[0])
			
		print("dict is:",dict)
		for key in dict:
			all_names.append(dict[key])
		print("all_names is:",all_names)
	except:
		pass
	all_faces = []
	all_labels = []
	def accept_cmd():
		all_faces.append(face_grey)
		if str(ebox.get()) not in all_names:
			all_names.append(str(ebox.get()))
		x = all_names.index(str(ebox.get()))
		all_labels.append(x)
		win.destroy()
		
	def cont_cmd():
		win.destroy()
		

	for file in train_list:
	
			img = cv2.imread(file,1)
			grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
			faces = face_cascade.detectMultiScale(grey_img,
					scaleFactor = 1.05,
					minNeighbors = 5 )

			for x,y,w,h in faces:
				face_grey = grey_img[y:y+h, x:x+h]
				face = img[y:y+h, x:x+h]
				
				win = Tk()
				win.geometry("+250+250")
				b,g,r = cv2.split(face)
				face = cv2.merge((r,g,b))
				
				# convert the images to PIL format...
				face_image = Image.fromarray(face)
				# ...and then to ImageTk format
				face_image = ImageTk.PhotoImage(face_image)
				face_panel = Label(win,image = face_image)
				face_panel.grid(row=0,column=0,rowspan = 2)
				
		
				l1 = Label(win,text="Name: ",font = ("Helvetica",12))
				l1.grid(row=0,column=1)
				
				ebox = Entry(win)
				ebox.grid(row=0,column=2)
				
				bAccept = Button(win,text = "Accept",command = accept_cmd)
				bAccept.grid(row =1,column=1)
		
				bReject = Button(win,text = "Reject",command = cont_cmd)
				bReject.grid(row =1,column=2)
				
				win.mainloop()
				
			face_recognizer.update(all_faces,np.array(all_labels))
			for i in all_names:
				face_recognizer.setLabelInfo(all_names.index(i),i)
			face_recognizer.save("trained_data.xml")

def find_face(image):
	img=image
	try:
		if img.shape[0]>750:
			x = img.shape[0]/750
			img = cv2.resize(img,(int(img.shape[1]/x),int(img.shape[0]/x)))
	except Exception as e:
		return
	grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	try:
		faces = face_cascade.detectMultiScale(grey_img,
				scaleFactor = 1.1,
				minNeighbors = 5 )
	
		for x,y,w,h in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
	
		cv2.imshow("Detected Face",img)
		cv2.namedWindow("Detected Face",cv2.WINDOW_NORMAL)
		cv2.resizeWindow("Detected Face",750,750)
		cv2.moveWindow("Detected Face",300,50)
		return
	except Exception as e:
		print(str(e))


def train_faces(image):
	img=image
	
	all_names=[]
	try:
		face_recognizer.read("trained_data.xml")
		#print(face_recognizer.getLabels())
		dict = {}
		for i in face_recognizer.getLabels():
			dict[i[0]]=face_recognizer.getLabelInfo(i[0])
			
		print("dict is:",dict)
		for key in dict:
			all_names.append(dict[key])
		print("all_names is:",all_names)
	except:
		pass
	
	
	all_faces = []
	all_labels = []
	def accept_cmd():
		all_faces.append(face_grey)
		if str(ebox.get()) not in all_names:
			all_names.append(str(ebox.get()))
		x = all_names.index(str(ebox.get()))
		all_labels.append(x)
		win.destroy()
		
	def cont_cmd():
		win.destroy()
	try:
		if img.shape[0]>750:
			x = img.shape[0]/750
			img = cv2.resize(img,(int(img.shape[1]/x),int(img.shape[0]/x)))
	except Exception as e:
		return
	grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	try:
		faces = face_cascade.detectMultiScale(grey_img,
				scaleFactor=1.1,
				minNeighbors = 5 )
	
		for x,y,w,h in faces:
			face_grey = grey_img[y:y+h, x:x+h]
			face = img[y:y+h, x:x+h]
			
			win = Tk()
			win.geometry("+250+250")
			b,g,r = cv2.split(face)
			face = cv2.merge((r,g,b))
			
			# convert the images to PIL format...
			face_image = Image.fromarray(face)
			# ...and then to ImageTk format
			face_image = ImageTk.PhotoImage(face_image)
			face_panel = Label(win,image = face_image)
			face_panel.grid(row=0,column=0,rowspan = 2)
			
	
			l1 = Label(win,text="Name: ",font = ("Helvetica",12))
			l1.grid(row=0,column=1)
			
			ebox = Entry(win)
			ebox.grid(row=0,column=2)
			
			bAccept = Button(win,text = "Accept",command = accept_cmd)
			bAccept.grid(row =1,column=1)
	
			bReject = Button(win,text = "Reject",command = cont_cmd)
			bReject.grid(row =1,column=2)
			
			win.mainloop()
			
		face_recognizer.update(all_faces,np.array(all_labels))
		for i in all_names:
			face_recognizer.setLabelInfo(all_names.index(i),i)
		face_recognizer.save("trained_data.xml")
	except Exception as e:
		print (str(e))


def training_video(vid_path):
	try:

		vid = cv2.VideoCapture(vid_path)
		if not vid.read()[0]:
				raise ValueError
		while (vid.isOpened()):
			if not vid.read()[0]:
				raise IndexError
			image = vid.read()[1]
			find_face(image)
			while cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) > 0:
				key = cv2.waitKey(1)
				if key == ord('c'):
					raise KeyError
				if cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) < 1:
					raise IndexError
				break		
		cv2.destroyAllWindows()
	except ValueError:
		messagebox.showinfo("Alert", "Invalid Video Source")
	except IndexError:
		pass
	except KeyError:
		cv2.destroyAllWindows()
		train_faces(image)
	except Exception as e:
		print (str(e))
	finally:
		cv2.destroyAllWindows()
		vid.release()

def main():
	win = Tk()
	win.title("Face Trainer by Aniruddha")
	win.geometry("463x323+392+263")

	def browse_img():
		fname = askopenfilename(filetypes = (("Pictures",["*.jpg","*.jpeg","*.bmp","*.png"]),("Videos",["*.avi","*.mp4"]),("All files","*.*")) )
		if fname:
			try:
				ePath.delete(0,END)
				ePath.insert(0,fname)
			except:
				pass
	
	def browse_dir():
	
		dname = askdirectory(mustexist = True)
		if dname:
			try:
				ePath.delete(0,END)
				ePath.insert(0,dname)
			except:
				pass

	def detect_dir():
		path = ePath.get()
		win.destroy()
		training(path+"/*.jpg")

	def detect_vid():
		path = ePath.get()
		win.destroy()
		training_video(path)

	def detect_img():	
		path = ePath.get()
		image = cv2.imread(ePath.get(),1)
		win.destroy()
		train_faces(image)
	
	def back_cmd():	
		win.destroy()
		import Face_Recognizer
	
	def exit_cmd():
		sys.exit()

	l1 = Label(win,text="Enter Path",font = ("Helvetica",12))
	l1.grid(row=1,column=1)
	ePath = Entry(win,font = ("Helvetica",12),width=28)
	ePath.grid(row=1,column=2,columnspan = 5)
	bBrowseImg = Button(win,text = "Browse Image/Video",font = ("Helvetica",12),width=15,command = browse_img)
	bBrowseImg.grid(row =2,column=1,columnspan=3)

	bBrowseDir = Button(win,text = "Browse Directories",font = ("Helvetica",12),width=15,command = browse_dir)
	bBrowseDir.grid(row =2,column=4,columnspan=2)

	bFaceDir = Button(win,text = "Train Faces in Directory",font = ("Helvetica",12),width=18,command = detect_dir)
	bFaceDir.grid(row =4,column=2,columnspan=3)

	bFaceVid = Button(win,text = "Train Faces in Videos",font = ("Helvetica",12),width=18,command = detect_vid)
	bFaceVid.grid(row =5,column=2,columnspan=3)

	bFaceImg = Button(win,text = "Train Faces in Images",font = ("Helvetica",12),width=18,command = detect_img)
	bFaceImg.grid(row =3,column=2,columnspan=3)

	bBack = Button(win,text = "Back",width=8,font = ("Helvetica",12),command =back_cmd)
	bBack.grid(row =6,column=1,columnspan=2)

	bExit = Button(win,text = "Exit",font = ("Helvetica",12),width=8,command = exit_cmd)
	bExit.grid(row =6,column=4,columnspan=3)

	for r in range(7):
		win.grid_rowconfigure(r,minsize = 30,pad = 12)
	for c in range(7):
		win.grid_columnconfigure(c,minsize = 50)
	
	win.mainloop()
