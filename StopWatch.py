# -*- coding: utf-8 -*-
"""
Created on Sun August 24 15:23:17 2020

@author: online135
"""

import tkinter as tk
import tkinter.font as TkFont
from datetime import datetime

def run():
    global Lapse

    current_time = datetime.now()
    diff = current_time - start_time
    txt_var.set('%d.%02d' % (diff.seconds, diff.microseconds//10000))

    if Lapse:
        Lapse = False  # flag
        index = indexcheck()
        txt_var2[index].set('%d.%02d' % (diff.seconds, diff.microseconds//10000))
        timeLapseText[index] = txt_var2[index]  # store value in the new list, that each value will not interrupt with each other.
        tk.Label(root, textvariable=timeLapseText[index], font = fontStyle).pack(fill = 'x')
        
    if running:
        root.after(20,run) #to reschedule after 20ms

def indexcheck():
    global index
    
    if index < 4:
        index += 1
        return index
    
    else:
        index = 0
        return index

def start():
    global running
    global start_time
    global reflag

    if not running:
        running = True
        if reflag == False:
            start_time = datetime.now()
            reflag = True
        root.after(10,run)

def stop():
    global running
    running = False

def reset():
    global start_time
    global reflag

    start_time = datetime.now()
    reflag = False    

    if not running:
        txt_var.set('0.00')

def timeLapse():
    global Lapse
    Lapse = True
    root.after(10,run)

running = False
start_time = None
Lapse = False
index = -1
reflag = False

root = tk.Tk()
root.geometry("500x540") #width x height
root.title("StopWatch")

txt_var = tk.StringVar()
txt_var.set('0.00')
fontStyle = TkFont.Font(family="Lucida Grande", size = 50)
tk.Label(root, textvariable=txt_var, font = fontStyle).pack()


'''
Use list to store 5 Time Lapse Value, and rotate it

'''
timeLapseText = [None for i in range(5)]

txt_var2 = [tk.StringVar() for i in range(5)]  
for txt in txt_var2:
    txt.set('0.00')

tk.Button(root,text="Start",command = start).pack(fill = 'x')
tk.Button(root,text="Stop",command = stop).pack(fill = 'x')
tk.Button(root,text="Reset",command = reset).pack(fill = 'x')
tk.Button(root,text = "Time Lapse",command = timeLapse).pack(fill = 'x')

root.mainloop()
