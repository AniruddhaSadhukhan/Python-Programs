""" 
Program to built a Face Detector Desktop application
	using OpenCV2 and Tkinter
(can detect faces in both single pictures and albums)
		by Aniruddha

"""

from tkinter import *
import glob2
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askdirectory
from PIL import ImageTk,Image
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

class Window:
	
	def __init__(self,window):
		self.win = window
		self.win.title("Face Detector by Aniruddha")
		self.win.geometry("629x469+399+188")
		
		#labels
		self.himg = ImageTk.PhotoImage(file = "Icon.png")
		h = Label(self.win,image = self.himg)
		h.grid(row=0,column=0,columnspan = 8)
		
		l1 = Label(self.win,text="Enter Path",font = ("Helvetica",12))
		l1.grid(row=1,column=1)

		l2 = Label(self.win,text="Scale Factor",font = ("Helvetica",12))
		l2.grid(row=3,column=1)

		l3 = Label(self.win,text="Image Showing Time (sec)\n[Only for Directories]",font = ("Helvetica",12))
		l3.grid(row=3,column=4)

		#entryboxes
		self.ePath = Entry(self.win,font = ("Helvetica",12))
		self.ePath.insert(0,"http://192.168.43.1:8080/videofeed")
		self.ePath.grid(row=1,column=2,columnspan = 4,sticky='ew')
		
		self.eScale = Entry(self.win,width = 5,font = ("Helvetica",12))
		self.eScale.insert(0,"1.1")
		self.eScale.grid(row=3,column=2)

		self.eTime = Entry(self.win,width = 5,font = ("Helvetica",12))
		self.eTime.insert(0,"2")
		self.eTime.grid(row=3,column=5)
		
		
		#buttons
		
		bBrowseImg = Button(self.win,text = "Browse Image/Video",font = ("Helvetica",12),width=15,command = self.browse_img)
		bBrowseImg.grid(row =2,column=2,columnspan=2)
		
		bBrowseDir = Button(self.win,text = "Browse Directories",font = ("Helvetica",12),width=15,command = self.browse_dir)
		bBrowseDir.grid(row =2,column=4,columnspan=2)
		
		bFaceImg = Button(self.win,text = "Detect Faces in Image",font = ("Helvetica",12),width=18,command = self.detect_img)
		bFaceImg.grid(row =4,column=2,columnspan=2)
		
		bFaceDir = Button(self.win,text = "Detect Faces in Directory",font = ("Helvetica",12),width=18,command = self.detect_dir)
		bFaceDir.grid(row =4,column=4,columnspan=2)
		
		bFaceVid = Button(self.win,text = "Detect Faces in Video",font = ("Helvetica",12),width=18,command = self.detect_vid)
		bFaceVid.grid(row =5,column=1,columnspan=7)
		
		bHelp = Button(self.win,text = "Help",width=8,font = ("Helvetica",12),command =self.help_cmd)
		bHelp.grid(row =6,column=1,columnspan=2)
		
		bExit = Button(self.win,text = "Exit",font = ("Helvetica",12),width=8,command = self.win.destroy)
		bExit.grid(row =6,column=4,columnspan=2)
		
		bTrainDir = Button(self.win,text = "Train Faces in Folders",font = ("Helvetica",12),width=18,command = self.training)
		bTrainDir.grid(row =7,column=2,columnspan=2)
		
		for r in range(8):
			self.win.grid_rowconfigure(r,minsize = 30,pad = 12)
		for c in range(7):
			self.win.grid_columnconfigure(c,minsize = 50)


	def browse_img(self):
		fname = askopenfilename(filetypes = (("Pictures",["*.jpg","*.jpeg","*.bmp","*.png"]),("Videos",["*.avi","*.mp4"]),("All files","*.*")) )
		if fname:
			try:
				self.ePath.delete(0,END)
				self.ePath.insert(0,fname)
			except:
				pass
	
	def browse_dir(self):
		
		dname = askdirectory(mustexist = True)
		if dname:
			try:
				self.ePath.delete(0,END)
				self.ePath.insert(0,dname)
			except:
				pass
	
	
	def find_face(self,image):
		img=image
		try:
			if img.shape[0]>750:
				x = img.shape[0]/750
				img = cv2.resize(img,(int(img.shape[1]/x),int(img.shape[0]/x)))
		except Exception as e:
			return
		grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		
		try:
			sf = float(self.eScale.get())
			if sf<=1:
				raise Exception
		except Exception as e:
			messagebox.showinfo("Alert", "Invalid Scale Factor\nMust be greater than 1\nUsing recommended Scale Factor of 1.05")
			sf = 1.1
			self.eScale.delete(0,END)
			self.eScale.insert(0,"1.1")
		
		try:
			faces = face_cascade.detectMultiScale(grey_img,
					scaleFactor = sf,
					minNeighbors = 5 )
		
			for x,y,w,h in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
				try:
					text=""
					face_grey = grey_img[y:y+h, x:x+h]
					face_recognizer.read("trained_data.xml")
					label,conf= face_recognizer.predict(face_grey)
					if conf < 100:
						text = face_recognizer.getLabelInfo(label)
				except:
					pass
			
			cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
			cv2.imshow("Detected Face",img)
			cv2.namedWindow("Detected Face",cv2.WINDOW_NORMAL)
			cv2.resizeWindow("Detected Face",750,750)
			cv2.moveWindow("Detected Face",300,50)
			return
		except Exception as e:
			print(str(e))
	
	def detect_img(self):
		try:
			img = cv2.imread(self.ePath.get(),1)
			if img is None:
				raise Exception
			self.find_face(img)
			while cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) > 0:
				if 27==cv2.waitKey(50):
					break
				
			cv2.destroyAllWindows()
		except Exception as e:
			messagebox.showinfo("Alert", "Invalid File Path")

	def detect_dir(self):
		try:
			try:
				time = int(float(self.eTime.get()) * 1000)
			except:
				raise ValueError
			import glob2
			list = []
			for ext in ("/*.jpg","/*.jpeg","/*.bmp","/*.png"):
				list.extend(glob2.glob(self.ePath.get()+ext))
			
			if not list :
				raise IndexError
				
			
			for file in list:
				img = cv2.imread(file,1)
				self.find_face(img)
				flag = False
				while cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) > 0:
					cv2.waitKey(time)
					if cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) < 1:
						return
					break
			cv2.destroyAllWindows()
		except ValueError:
			messagebox.showinfo("Alert", "Invalid Image Showing Time (sec)")
		except IndexError:
			messagebox.showinfo("Alert", "Invalid Directory Path")
			
	def detect_vid(self):
		try:

			vid = cv2.VideoCapture(str(self.ePath.get()))
			if not vid.read()[0]:
					raise ValueError
			while (vid.isOpened()):
				if not vid.read()[0]:
					raise IndexError
				self.find_face(vid.read()[1])
				while cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) > 0:
					cv2.waitKey(1)
					if cv2.getWindowProperty("Detected Face",cv2.WND_PROP_VISIBLE) < 1:
						raise IndexError
					break		
			cv2.destroyAllWindows()
		except ValueError:
			messagebox.showinfo("Alert", "Invalid Video Source")
		except IndexError:
			pass
		except Exception as e:
			print (str(e))
		finally:
			cv2.destroyAllWindows()
			vid.release()
	
	def help_cmd(self):
		
		self.hlp = Toplevel()
		self.hlp.title("Help")
		self.hlp.geometry("555x433+428+204")
		h = Label(self.hlp,image = self.himg).pack()
		str = """To detect faces in photos,give path to the desired photo
		      \nTo detect faces in all photos of a folder,give path to the desired Folder
		      \nTo detect faces in videos,give path to the desired video
		      \nTo detect faces in the webcam video,give 0 as path 
		      \nTo detect faces in the external camera video,give its index(1,2,...) as path""" 
		s = Label(self.hlp,text = str,justify=LEFT,padx = 20,pady = 20,font = ("Helvetica",12)).pack()
		Button(self.hlp,text = "Exit",font = ("Helvetica",12),width=8,command = self.hlp.destroy).pack()
		Label(self.hlp,text="",font = ("Helvetica",12)).pack()
		self.hlp.mainloop()
	
	
	def training(self):
		list = []
		for ext in ("/*.jpg","/*.jpeg","/*.bmp","/*.png"):
			list.extend(glob2.glob(self.ePath.get()+ext))
		
		if not list :
			raise IndexError
	
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
		
			
		
		
		for file in list:
			
			self.img = cv2.imread(file,1)
			self.grey_img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)

			self.faces.append(face_cascade.detectMultiScale(self.grey_img,
					scaleFactor = 1.05,
					minNeighbors = 5 ))
			self.cur_top = None
			def exec_cmd(x):
				def accept_cmd():
					all_faces.append(face_grey)
					if str(ebox.get()) not in all_names:
						all_names.append(str(ebox.get()))
					x = all_names.index(str(ebox.get()))
					all_labels.append(x)
					status = True
					exec_cmd(self.next_ind)
					print("Accepted")
			
		
				def cont_cmd():
					status = True
					exec_cmd(self.next_ind)
				self.next_ind = x+1
				print(self.next_ind," ? ",len(self.faces))
				if self.next_ind > len(self.faces):
					
					next_ind = 0
				if self.cur_top != None:
					print("Dest")
					self.cur_top.destroy()
					
				self.cur_top = Toplevel()	
				(x,y,w,h)= self.faces[x]
				face_grey = self.grey_img[y:y+h, x:x+h]
				face = self.img[y:y+h, x:x+h]
				print("looping2")
				status = False
				b,g,r = cv2.split(face)
				face = cv2.merge((r,g,b))
				
				# convert the images to PIL format...
				face_image = Image.fromarray(face)
				# ...and then to ImageTk format
				face_image = ImageTk.PhotoImage(face_image)
				face_panel = Label(self.cur_top,image = face_image)
				face_panel.grid(row=0,column=0,rowspan = 2)
		

				l1 = Label(self.cur_top,text="Name: ",font = ("Helvetica",12))
				l1.grid(row=0,column=1)
		
				ebox = Entry(self.cur_top)
				ebox.grid(row=0,column=2)
				
				bAccept = Button(self.cur_top,text = "Accept",command = accept_cmd)
				bAccept.grid(row =1,column=1)

				bReject = Button(self.cur_top,text = "Reject",command = cont_cmd)
				bReject.grid(row =1,column=2)
				print("looping1")
				
			exec_cmd(0)	
		print("bye bye")
		face_recognizer.update(all_faces,np.array(all_labels))
		for i in all_names:
			face_recognizer.setLabelInfo(all_names.index(i),i)
		face_recognizer.save("trained_data.xml")
				

win = Tk()
Window(win)

win.mainloop()
