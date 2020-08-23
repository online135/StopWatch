# -*- coding: utf-8 -*-
"""
Created on Sun August 23 19:43:06 2020

@author: online135
"""

import tkinter as tk
import tkinter.font as TkFont
from datetime import datetime

def run():
    global Lapse
    global index
    current_time = datetime.now()
    diff = current_time - start_time
    txt_var.set('%d.%02d' % (diff.seconds, diff.microseconds//10000))

    if Lapse:
        print(index)
        Lapse = False
        txt_var2[index].set('%d.%02d' % (diff.seconds, diff.microseconds//10000))
        timeLapseText[index] = txt_var2[index]
        tk.Label(root, textvariable=timeLapseText[index], font = fontStyle).pack(fill = 'x')
        index += 1     # there still have a bug at here, don't click Button timeLapse more than 5 times
        
    if running:
        root.after(20,run) #to reschedule after 20ms

def start():
    global running
    global start_time

    if not running:
        running = True
        start_time = datetime.now()
        root.after(10,run)

def stop():
    global running
    running = False

def reset():
    global start_time
    start_time = datetime.now()

    if not running:
        txt_var.set('0.00')

def timeLapse():
    global Lapse
    Lapse = True
    root.after(10,run)

running = False
start_time = None
Lapse = False
index = 0

root = tk.Tk()
root.geometry("500x2000") #width x height
root.title("StopWatch")

txt_var = tk.StringVar()
txt_var.set('0.00')
fontStyle = TkFont.Font(family="Lucida Grande", size = 50)
tk.Label(root, textvariable=txt_var, font = fontStyle).pack()

timeLapseText = [None for i in range(5)]

txt_var2 = [tk.StringVar() for i in range(5)]
for txt in txt_var2:
    txt.set('0.00')

tk.Button(root,text="Start",command = start).pack(fill = 'x')
tk.Button(root,text="Stop",command = stop).pack(fill = 'x')
tk.Button(root,text="Reset",command = reset).pack(fill = 'x')
tk.Button(root,text = "Time Lapse",command = timeLapse).pack(fill = 'x')

root.mainloop()
