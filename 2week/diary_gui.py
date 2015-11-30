# -*- coding:utf-8 -*-
import Tkinter

root = Tkinter.Tk()

myLabel = Tkinter.Label(root, text = "Hello World")
myLabel.pack()

message = Tkinter.Entry(root) # 添加Entry组件
message.pack()

root.mainloop()