from tkinter import *

def show():
	print("账号： %s"%e1.get())
	print("密码： %s"%e2.get())
	
def R2():
	root.quit
	



root= Tk()
#root.geometry('200x100')
root.title('登录')

e1=Entry(root)
e2=Entry(root,show='*')
text1=Label(root,text='账号:')
text2=Label(root,text='密码:')
B1=Button(root,text='注册',command=show,width=10)
B2=Button(root,text='登录',command=root.quit,width=10)

text1.grid(row=0,column=0)
text2.grid(row=1,column=0)

e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)


B1.grid(row=3,column=0,sticky=W,padx=10)
B2.grid(row=3,column=1,sticky=E,padx=10)

mainloop()