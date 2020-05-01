# from PIL import Image
# import sys
# import os



# arg1 = sys.argv[1]
# arg2 = sys.argv[2]

# if not os.path.exists(arg2):
# 	os.makedirs(arg2)

# for file in os.listdir(arg1):
# 	img = Image.open(f'{arg1}{file}','r')
# 	filename = os.path.splitext(file)[0]
# 	img.save(f'{arg2}{filename}.png','png')
# 	print('all done')
from tkinter import *
from PIL import Image

def convert():
	img = Image.open(e1_value.get(),'r')
	img.save('astro.png','png')
	

window = Tk()

l1 = Label(window,text = 'Input Image Path')
l1.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0,column = 1)

b1 = Button(window,text = 'Convert',height = 1,width = 17,command = convert)
b1.grid(row = 1,column = 1)

l1 = Label(window,text = 'Note:Converted images with store in same folder where this file .exe file is')
l1.grid(row = 2, column = 0)




window.mainloop()

