import tkinter as tk
from PIL import ImageTk,Image

def resize(w, h, w_box, h_box, pil_image):  
  ''' 
  resize a pil_image object so it will fit into 
  a box of size w_box times h_box, but retain aspect ratio 
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例 
  '''  
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
  f2 = 1.0*h_box/h  
  factor = min([f1, f2])  
  #print(f1, f2, factor) # test  
  # use best down-sizing filter  
  width = int(w*factor)  
  height = int(h*factor)  
  return pil_image.resize((width, height), Image.ANTIALIAS)

app = tk.Tk()
app.title("Welcome")
app.geometry("1000x600+80+30")
app.minsize(1000, 600)
app.maxsize(1000, 600)


body = tk.PanedWindow(app,showhandle = False,sashrelief = 'sunken',orient='vertical')
body.pack(fill="both", expand=1)

image = Image.open('picture//1.jpg')
w, h = image.size 
image_resized = resize(w, h, 1000, 450, image) 
im = ImageTk.PhotoImage(image_resized)
body_img = tk.Canvas(app,width=1000,height=450)
body_img.create_image(500,225,image = im)
body.add(body_img)

box = tk.PanedWindow(body,showhandle = False,sashrelief = 'sunken',orient="horizontal")
body.add(box)

image = Image.open('picture//2.jpg')
hw, hh = image.size 
himage_resized = resize(hw,hh, 100, 150, image) 
him = ImageTk.PhotoImage(himage_resized)
head_img = tk.Label(box,width=100,height=150,compound='center',image= him)
box.add(head_img)

m_box = tk.Frame(box)
box.add(m_box)

name = tk.Label(m_box, text="小老鼠", anchor='w', relief='groove', pady=5, padx=10)
name.place(x=10, y=10)

message_content = tk.StringVar()
message_content.set('喵喵喵~喵喵喵~喵喵喵~喵喵喵~喵喵喵~喵喵喵~喵喵喵~喵喵喵~喵喵喵~')

def next():
  message_content.set('吱吱吱~吱吱吱~吱吱吱~吱吱吱~吱吱吱~吱吱吱~吱吱吱~吱吱吱~吱吱吱~')

  img_open = Image.open('picture//4.jpg')
  nw, nh = img_open.size 
  nimage_resized = resize(nw,nh, 100, 150, img_open) 
  nim = ImageTk.PhotoImage(nimage_resized)
  head_img.config(image=nim)  
  head_img.image=nim #keep a reference

  select = tk.Toplevel()
  select.geometry("300x200+430+230")
  select.minsize(300, 200)
  select.maxsize(300, 200)
  question = tk.Label(select, text="请选择：", anchor='w')
  question.pack()
  lb = tk.Listbox(select, height=4)
  for item in ['python','tkinter','widget']:
    lb.insert('end',item)
  lb.pack()
  select.mainloop()

name = tk.Button(m_box, text="→", anchor='w', relief='raised', padx=10, command=next)
name.place(x=750, y=10)

message = tk.Message(m_box,width=800,textvariable =message_content, relief='sunken')
message.place(x=10, y=50, width=800, height=80)
app.mainloop()
