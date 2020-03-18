import tkinter as tk
from PIL import ImageTk,Image
import json
import tkinter.messagebox

# 初始全局变量
global story_id
global dialogue_id
global story_num
global dialogue_num
global people_data
global story_data
global status
global select
global lb

story_id = 0
dialogue_id = 0
story_num = 0
dialogue_num = 0
people_data = {}
story_data = []
status = 'dialogue'

# 游戏数据
people_data = json.loads( open('people.json', 'r', encoding='utf-8').read() )

story_data = json.loads( open('story.json', 'r', encoding='utf-8').read() )


def get_img(image, box_w, box_h):
  w, h = image.size
  f1 = 1.0 * box_w / w # 1.0 forces float division in Python2  
  f2 = 1.0 * box_h / h
  factor = min([f1, f2])
  # use best down-sizing filter  
  width = int(w*factor)
  height = int(h*factor)
  image_resized = image.resize((width, height), Image.ANTIALIAS)
  return ImageTk.PhotoImage(image_resized)

def refresh() :
  global story_id
  global dialogue_id
  global dialogue_num
  global people_data
  global story_data
  print(dialogue_num)
  now_data = {
    'word': story_data[story_id]['dialogue'][dialogue_id]['word'],
    'name': people_data[story_data[story_id]['dialogue'][dialogue_id]['people']]['name'],
    'people_img': people_data[story_data[story_id]['dialogue'][dialogue_id]['people']]['img'],
    'bg_img': story_data[story_id]['bg']
  }
  print(json.dumps(now_data))
  content_word.set(now_data['word'])
  content_name.set(now_data['name'])

  background_img = get_img(Image.open(now_data['bg_img']), 1000, 450)
  background.config(image=background_img)  
  background.image=background_img #keep a reference

  people_img = get_img(Image.open(now_data['people_img']), 100, 150)
  people.config(image=people_img)
  people.image=people_img #keep a reference

def show_select() :
  global select
  global lb
  select = tk.Toplevel()
  select.geometry('300x200+430+230')
  select.minsize(300, 200)
  select.maxsize(300, 200)

  question = tk.Label(select, text='请选择：', anchor='w')
  question.pack()

  lb = tk.Listbox(select, height=4)
  for item in story_data[story_id]['options']:
    lb.insert('end',item['option'])
  lb.pack()
  
  name = tk.Button(select, text='确定', anchor='w', relief='raised', padx=10, command=hidden_select)
  name.pack()

  select.mainloop()

def next_dialogue():
  global status
  if status == 'dialogue' :
    global story_id
    global dialogue_id
    global story_num
    global dialogue_num
    global people_data
    global story_data
    if dialogue_id + 1 < dialogue_num :
      dialogue_id += 1
      refresh()
    else :
      if len(story_data[story_id]['options']) > 1 :
        show_select()
        status = 'select'
      elif len(story_data[story_id]['options']) == 1 :
        story_id = story_data[story_id]['options'][0]['to']
        dialogue_id = 0
        dialogue_num = len(story_data[story_id]['dialogue'])
        refresh()
      else :
        tkinter.messagebox.showinfo('结束','game over')

def hidden_select() :
  global select
  global lb
  global story_id
  global dialogue_id
  global dialogue_num
  #print( json.dumps(select) )
  print( lb.curselection() )
  if lb.curselection() :
    id = lb.curselection()[0]
    story_id = story_data[story_id]['options'][id]['to']
    dialogue_id = 0
    dialogue_num = len(story_data[story_id]['dialogue'])
    select.destroy()
    refresh()

# 设置主窗口
app = tk.Tk()
app.title('Welcome')
app.geometry('1000x600+80+30')
app.minsize(1000, 600)
app.maxsize(1000, 600)

# 初始化数据
story_num = len( story_data )
dialogue_num = len( story_data[story_id]['dialogue'] )

content_word = tk.StringVar()
content_name = tk.StringVar()

now_data = {
  'word': story_data[story_id]['dialogue'][dialogue_id]['word'],
  'name': people_data[story_data[story_id]['dialogue'][dialogue_id]['people']]['name'],
  'people_img': people_data[story_data[story_id]['dialogue'][dialogue_id]['people']]['img'],
  'bg_img': story_data[story_id]['bg']
}

content_word.set(now_data['word'])
content_name.set(now_data['name'])
background_img = get_img(Image.open(now_data['bg_img']), 1000, 450)
people_img = get_img(Image.open(now_data['people_img']), 100, 150)

#生成组件
body = tk.PanedWindow(app,showhandle = False,sashrelief = 'sunken',orient='vertical')

background = tk.Label(body,width=1000,height=450,compound='center',image=background_img)

box = tk.PanedWindow(body,showhandle = False,sashrelief = 'sunken',orient='horizontal')

people = tk.Label(box,width=100,height=150,compound='center',image=people_img)

dialogue_box = tk.Frame(box)

name = tk.Label(dialogue_box, textvariable =content_name, anchor='w', relief='groove', pady=5, padx=10)

next_btn = tk.Button(dialogue_box, text='→', anchor='w', relief='raised', padx=10, command=next_dialogue)

word = tk.Message(dialogue_box,width=800,textvariable =content_word, relief='sunken')

#组件布局
body.pack(fill='both', expand=1)

body.add(background)

body.add(box)

box.add(people)

box.add(dialogue_box)

name.place(x=10, y=10)

next_btn.place(x=750, y=10)

word.place(x=10, y=50, width=800, height=80)

app.mainloop()