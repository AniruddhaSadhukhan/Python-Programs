""" 
Python program to implement motion detector
		by Aniruddha
"""
# for webcam,give 0 as path 
# for external camera,give its index(1,2,...) as path
#or give other video path
vid_path = "http://192.168.42.129:8080/video"	

import cv2
from datetime import datetime
from bokeh.plotting import figure,output_file,show
import pandas as pd
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.models import Range1d,HoverTool,ColumnDataSource

vid = cv2.VideoCapture(vid_path)

base_frame = None
prev_sts = False
new_sts = False
static_frame = 0

start_time = []
end_time = []

df = pd.DataFrame(columns=["Start","End"])

try:
	cv2.namedWindow("Motion Detector",cv2.WINDOW_NORMAL)
	cv2.namedWindow("Threshold Camera",cv2.WINDOW_NORMAL)
	
	cv2.resizeWindow("Motion Detector",700,700)
	cv2.resizeWindow("Threshold Camera",700,700)
	
	cv2.moveWindow("Motion Detector",2,50)
	cv2.moveWindow("Threshold Camera",732,52)
	
	while True:
		frame = vid.read()[1]
		prev_sts = new_sts
		new_sts = False
		
		gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)
		
		
		if base_frame is None:
			base_frame = gray_frame
#			print("base_frame captured")
			continue
		
		delta_frame = cv2.absdiff(base_frame,gray_frame)
		
		threshold_frame = cv2.threshold(delta_frame,35,255,cv2.THRESH_BINARY)[1]
		
		threshold_frame = cv2.dilate(threshold_frame,None,iterations = 2)
			
		(_,cnts,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		
		for contour in cnts:
			if cv2.contourArea(contour) < 1000:
				continue
			(x,y,w,h) = cv2.boundingRect(contour)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
			new_sts = True
			
			
		if prev_sts==False and new_sts==True:
			start_time.append(datetime.now())
		elif prev_sts==True and new_sts==False:
			end_time.append(datetime.now())
		
		
		#print (new_sts)	
		if new_sts == False:
			static_frame += 1
#			print("Idle: ",static_frame)
			if static_frame>50:
				base_frame = gray_frame
#				print("base_frame updated")
				static_frame = 0
			
		cv2.imshow("Motion Detector",frame)
#		cv2.imshow("gray_Camera",gray_frame)
#		cv2.imshow("Difference_Camera",delta_frame)
		cv2.imshow("Threshold Camera",threshold_frame)
		key = cv2.waitKey(1)
		if key == ord('q'):
			if new_sts==True:
				end_time.append(datetime.now())
			break
except Exception as e:
	print(str(e))
vid.release()
cv2.destroyAllWindows()
for i,j in zip(start_time,end_time):
	df=df.append({"Start":i,"End":j},ignore_index=True)
#	print (i,"------",j)
df.to_csv("Recorded_data.csv")






df["Start_String"] = df["Start"].dt.strftime("%d/%m/%y %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%d/%m/%y %H:%M:%S")

cds = ColumnDataSource(df)
hover = HoverTool(tooltips=[("Start","@Start_String"),("End","@End_String")])


p=figure(x_axis_type = "datetime",sizing_mode='stretch_both',y_range=Range1d(-0.05,1.05,bounds="auto"),tools='pan,box_zoom,wheel_zoom,save,reset',logo = None)
p.title.text="Motion Detected"
p.title.align = "center"
p.title.text_font = 'helvetica'
p.title.text_font_size = '50pt'
p.title.text_font_style='italic'
p.add_tools(hover)
p.xaxis.axis_label = "Time ----->"
p.xaxis.axis_label_text_font_size = "20pt"
p.xaxis.major_label_text_font_size = "10pt"

p.xaxis.formatter = DatetimeTickFormatter(days = ["%e %b '%y"],
					seconds=["%H:%M:%S"],
					milliseconds=["%H:%M:%S:%3N"]
					)
p.quad(top = 1,left="Start",right="End",bottom=0,alpha = 0.5,source=cds)
p.yaxis.visible = False
p.ygrid[0].ticker.desired_num_ticks=1

show(p)




