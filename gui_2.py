import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import sys
import subprocess
import os
from tkinter import Tk, Label, StringVar, Button, Entry, Frame, Text, Toplevel, filedialog, LEFT, END

from math import *

def text_window():
    s_lst=['acos','asin','atan','atan2','ceil','cos','cosh','degrees','e','exp','fabs','floor','fmod','frexp','hypot','ldexp','log','log10',
            'modf','pi','pow','radians','sin','sinh','sqrt','tan','tanh']

    e1=entryText1.get()
    e2=entryText2.get()
    e3=entryText3.get()
    e4=entryText4.get()
    e5=entryText5.get()
    e6=entryText6.get()

    filename=open(entryText8.get(),"w",encoding="utf-8")
    filename.write(e1+" "+e2+" "+e3+" "+e4+" "+e5+" "+e6)
    filename.close()

    subprocess.run([entryText7.get()])
    getlastfile=max(os.listdir(),key=os.path.getctime)

    if getlastfile.split('.')[1]=="txt":
        fout=open(getlastfile,"r",encoding="utf-8")
        data=fout.read()
        fout.close()
    else:
        data="Error"
    
    window2 = Toplevel(window)
    window2.title("Solution")
    window2.geometry("500x500+120+120")
    window2.resizable(False, False)
  
    T = Text(window2, height = 30, width = 60)
    T.place(x=10,y=10)
    T.insert(END,data)

    #################
    window3 = Toplevel(window)
    window3.title("Plot")
    window3.geometry("500x500+120+120")
   
    fig = Figure(figsize = (5, 5),dpi = 100)

    x1 = []
    y1 = []

    y2=[]
    data=data.split("\n")
    s_dict=dict([(k,locals().get(k,None)) for k in s_lst])
    s_dict['pi']=pi
    s_dict['exp']=exp
    s_dict['abs']=fabs
    s_dict['sin']=sin
    s_dict['cos']=cos
    s_dict['tan']=tan
    s_dict['log']=log
    s_dict['log10']=log10
    s_dict['tan']=tan
    s_dict['sqrt']=sqrt
    s_dict['asin']=asin
    
    for line in data:
        line=line.split(" ")
        if len(line)>1:
            x1.append(float(line[0]))
            y1.append(float(line[1]))

            if (entryText9.get()!=""):
                f=entryText9.get()
                s_dict['x']=float(line[0])
                a=eval(f,s_dict)
                y2.append(float(a))
                

    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(x1, y1, label = "line 1")

    if len(y2)>0:
        plot1.plot(x1, y2, 'r-o',label = "line 2")
  
    canvas = FigureCanvasTkAgg(fig,master = window3)  
    canvas.draw()
  
    canvas.get_tk_widget().pack()
  
    toolbar = NavigationToolbar2Tk(canvas,
                                   window3)
    toolbar.update()
  
    canvas.get_tk_widget().pack()

    

def ask_window():
    fp=filedialog.askopenfilename()
    e7.insert(END,fp)
        
window = Tk()
window.title("Ode v1.0")
window.geometry("700x150+120+120")
window.resizable(False, False)

entryText1 = tk.StringVar()
e1=Entry(window, textvariable=entryText1, font=("Arial",12), width=10)
e1.place(x=50,y=20)
entryText1.set( "a=" )


entryText2 = tk.StringVar()
e2=Entry(window, textvariable=entryText2, font=("Arial",12), width=10)
e2.place(x=150,y=20)
entryText2.set( "b=" )


entryText3 = tk.StringVar()
e3=Entry(window, textvariable=entryText3, font=("Arial",12), width=10)
e3.place(x=250,y=20)
entryText3.set( "f(a)=" )


entryText4 = tk.StringVar()
e4=Entry(window, textvariable=entryText4, font=("Arial",12), width=10)
e4.place(x=350,y=20)
entryText4.set( "f(b)=" )


entryText5 = tk.StringVar()
e5=Entry(window, textvariable=entryText5, font=("Arial",12), width=10)
e5.place(x=450,y=20)
entryText5.set( "eps=" )


entryText6 = tk.StringVar()
e6=Entry(window, textvariable=entryText6, font=("Arial",12), width=10)
e6.place(x=550,y=20)
entryText6.set( "n=" )


entryText7 = tk.StringVar()
e7=Entry(window, textvariable=entryText7, font=("Arial",12), width=20)
e7.place(x=50,y=100)

button0= Button(window,text="Choose exe",  width=10, command=ask_window)
button0.place(x=250,y=100)

entryText8 = tk.StringVar()
e8=Entry(window, textvariable=entryText8, font=("Arial",12), width=20)
e8.place(x=350,y=100)
e8.insert(END,"datin.txt")

button1= Button(window,text="Get solution",  width=10, command=text_window)
button1.place(x=550,y=100)

l9=Label(window, text="Solution function")
l9.place(x=50, y=60)
entryText9 = tk.StringVar()
e9=Entry(window, textvariable=entryText9, font=("Arial",12), width=50)
e9.place(x=150,y=60)


window.mainloop()

