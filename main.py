
from tkinter import *
from PIL import ImageTk,Image

class Picture():
	def __init__(self):
		image1 =Image.open('picture//1.jpg')
		self.background_image = ImageTk.PhotoImage(image1)
		self.w = self.background_image.width()
		self.h = self.background_image.height()
		app.geometry('%dx%d+0+0' % (self.w,self.h)) 
		self.canvas = Canvas(app, width=self.w, height=self.h,bg='pink')
		self.canvas.pack()	
	
	def showpicture(self,num):
		image1 =Image.open('picture//'+str(num)+'.jpg')
		self.background_image = ImageTk.PhotoImage(image1)
		
		self.canvas.create_image(0,0,anchor=NW, image=self.background_image)
	
	def showtext(self,str):
		titleFont = ('微软雅黑', 20, 'bold')
		self.canvas.create_text(self.w/2, 0.75*(self.h), text=str,font = titleFont)
	def showchoice(self,str1,str2):
		titleFont = ('微软雅黑', 10, 'bold')
		self.canvas.create_text(0.3*(self.w), 0.8*(self.h), text=str1,font = titleFont)
		self.canvas.create_text(0.7*(self.w), 0.8*(self.h), text=str2,font = titleFont)


def callback3(event):
	if (event.y>700)and(event.y<750):
		if event.x<280:
			pic.showpicture(3)
			pic.showtext('这是第三张图')
		else:
			pic.showpicture(4)
			pic.showtext('这是第四张图')

def callback2(event):

	pic.showpicture(2)
	pic.showtext('这是第二张图')
	pic.showchoice('三','四')
	pic.canvas.bind("<Button-1>", callback3)


app = Tk()
app.title("Welcome")
pic= Picture()
pic.canvas.bind("<Button-1>", callback2)
pic.showpicture(1)
pic.showtext('这是第一张图')

app.mainloop()
