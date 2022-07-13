#!/ usr/bin/env python3
# -*- coding : utf -8 -*-

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
import sqlite3
from tkinter import Menu
#import pmw




#connecting to sqlite database

class getsong():
    def searchsong(self):
        pass
    def getsongs(self):
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()
        c.execute("""SELECT title FROM son""")
        output=c.fetchall()
        lbl=Text(window, height=33, width=170)
        lbl.place(x=0,y=110)
        scroll = Scrollbar(window, command=lbl.yview,bg='black')
        lbl.configure(yscrollcommand=scroll.set)
        lbl.columnconfigure(0, weight=1)
        lbl.rowconfigure(0, weight=1)
        scroll.grid(columnspan=40)
        scroll.place(x=1340, y=120,height=560,width=23)
        for ii in output:
            a=ii
            buttons=[]
            for i in a:
                button=Button(lbl,height= 5, width=170,text= i,command=lambda ii = ii :clicked(ii))
            lbl.window_create(END,align=TOP,window=button)
            buttons.append(button)
        conn.commit()



    def INDEXED(self):
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()
        c.execute("""SELECT id FROM son""")
        output = c.fetchall()
        lbl = Text(window, height=33, width=170,bg="MediumPurple4", fg = "white")
        lbl.place(x=0, y=110)
        scroll = Scrollbar(window,command=lbl.yview,bg='black')
        lbl.configure(yscrollcommand=scroll.set)
        lbl.columnconfigure(0, weight=1)
        lbl.rowconfigure(0, weight=1)
        scroll.grid(columnspan=40,sticky=N+E+W+S)
        scroll.place(x=1340, y=120, height=550, width=23)
        for ii in output:
            button2=[]
            button = Button(lbl, height=3,width=170,text=ii,command= lambda ii = ii :clicked1(ii))
            lbl.window_create(END, window=button)
            button2.append(button)
            for boobs in button2:
                boobs.bind('<ButtonPress>', lambda :prit())
        conn.commit()



    def FAVOURITE(self):
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()
        c.execute("""SELECT title FROM AddSongs""")
        output = c.fetchall()
        lbl = Text(window, height=33, width=170,bg='snow')
        lbl.place(x=0, y=110)
        lbl.columnconfigure(0,weight=1)
        lbl.rowconfigure(0,weight=1)
        scroll = Scrollbar(window, command=lbl.yview,bg='black')
        lbl.configure(yscrollcommand=scroll.set)
        scroll.grid(columnspan=40)
        scroll.place(x=1340, y=120,height=550,width=23)
        for ii in output:
            a = ii
            buttons = []
            for i in a:
                button = Button(lbl, height=5, width=170, text=i, command=lambda ii=ii: clicked(ii))
            lbl.window_create(END, align=TOP, window=button)
            buttons.append(button)


    def About(self):
        Pmw.initialise()
        Pmw.aboutversion('1.0')
        Pmw.aboutcopyright('Copyright SACRED SONGS AND SOLO 2021\nAll rights reserved')
        Pmw.aboutcontact(
            'For information about this application contact:\n' +
            ' Sales at Company Name\n' +
            ' Phone: (+234)093843137 or (+234)0854234958\n' +
            ' email: info@company_name.com'
        )
        about = Pmw.AboutDialog(window)

getingsongs=getsong()

window =Tk()
window.title("Sacred songs and solo")
h,w = window.winfo_screenheight(),window.winfo_screenwidth()
window.geometry(("%dx%d") % (w, h))

def clicked_id(a):
    try:
        if int(a) > 1200 :
            messagebox.showinfo("ERROR","Id out of Range  Limit 1200")
    except ValueError:
        pass
    try:
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()
        c.execute("""SELECT content FROM son WHERE id IS (?)""",(a,))
        out = c.fetchone()
        output = ''.join(out)
        lbl = Text(window, height=33, width=170)
        lbl.tag_configure('bold_italics', font=('tahoma', 26, 'bold'), justify=CENTER)
        lbl.place(x=0, y=110)
        scroll = Scrollbar(window, command=lbl.yview)
        scroll.grid(columnspan=40)
        scroll.place(x=1340, y=120, height=550, width=23)
        lbl.insert(END, output, 'bold_italics')
        lbl.configure(yscrollcommand=scroll.set, state=DISABLED)
    except TypeError:
        pass
def prit():
    print("right clicked")

#button click event
def clicked1(a):
    for i in a:
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()
        c.execute("""SELECT content FROM son WHERE id IS (?)""",(i,))
        out = c.fetchone()
        output = ''.join(out)
        lbl = Text(window, height=33, width=170)
        lbl.tag_configure('bold_italics', font=('tahoma', 26, 'bold'), justify=CENTER)
        lbl.place(x=0, y=110)
        scroll = Scrollbar(window, command=lbl.yview)
        scroll.grid(columnspan=40)
        scroll.place(x=1340, y=120, height=550, width=23)
        lbl.insert(END, output, 'bold_italics')
        lbl.configure(yscrollcommand=scroll.set, state=DISABLED)

def clicked(a):
    for i in a:
        conn = sqlite3.connect('songs.db')
        c = conn.cursor()
        c.execute("""SELECT content FROM son WHERE title IS (?)""",(i,))
        out = c.fetchone()
        output = ''.join(out)
        lbl = Text(window, height=33, width=170)
        lbl.tag_configure('bold_italics', font=('tahoma', 26, 'bold'), justify=CENTER)
        lbl.place(x=0, y=110)
        scroll = Scrollbar(window, command=lbl.yview)
        scroll.grid(columnspan=40)
        scroll.place(x=1340, y=120, height=550, width=23)
        lbl.insert(END, output, 'bold_italics')
        lbl.configure(yscrollcommand=scroll.set,state=DISABLED)

def click(a):
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()
    c.execute("""SELECT content FROM son WHERE title LIKE (?)""",('%'+a+'%',))
    out = c.fetchone()
    output = ''.join(out)
    lbl = Text(window, height=33, width=170)
    lbl.tag_configure('bold_italics', font=('tahoma', 26, 'bold'), justify=CENTER)
    lbl.place(x=0, y=110)
    scroll = Scrollbar(window, command=lbl.yview)
    scroll.grid(columnspan=40)
    scroll.place(x=1340, y=120, height=550, width=23)
    lbl.insert(END, output, 'bold_italics')
    lbl.configure(yscrollcommand=scroll.set,state=DISABLED)


#Adding buttons to window

btn11=Button(window, text = "Search by text ", bg="black", fg = "white", command=lambda:click(txt.get()), font=("Arial",20))
btn11.grid(column =0,row=0,sticky=NW)
btn22=Button(window, text = "Search by Id", bg="black", fg = "white", command=lambda:clicked_id(txt2.get()), font=("Arial",20))
btn22.grid(column =0,row=0,sticky=NW)
btn22.place(x=560,y=0)


#tab buttons
ALL=Button(window, text = "ALL", bg="MediumPurple4", fg = "white", command=lambda:getingsongs.getsongs(), font=("Tahoma",20,'bold'),width=20)
ALL.grid(column=0,row =2,columnspan=1,padx=3,sticky=N+S)
ALL.place(y=70)
INDEX=Button(window, text = "INDEX", bg="MediumPurple4", fg = "white", command=lambda:getingsongs.INDEXED(), font=("Tahoma",20,'bold'),width=20)
INDEX.grid(column=2,row=2,columnspan=2,)
INDEX.place(x=450,y=70)
FAVOURITE=Button(window, text = "FAVOURITE", bg="MediumPurple4", fg = "white", command=lambda:getingsongs.FAVOURITE(), font=("Tahoma",20,'bold'),width=20)
FAVOURITE.grid(column=4,row=2)
FAVOURITE.place(x=900,y=70)

#adding search bar
txt = Entry(window, width=120)
txt.grid(column=2, row=0)
txt.place(x=220, y=13,width=250,height = 30)
txt.focus()

txt2 = Entry(window, width=120)
txt2.grid(column=2, row=0)
txt2.place(x=760, y=13,width=250,height = 30)
txt2.focus()
txt2.get()


#adding the scroll bar

scrollY = Scrollbar (window, orient=VERTICAL)



# adding a menu bar
menu= Menu(window)
new_item = Menu(menu)
new_item1 = Menu(menu)
new_item2=Menu(menu)
new_item2.add_command(label="Help")
new_item.add_command(label='Support')
new_item1.add_command(label='About',command=lambda :getingsongs.About())

#adding menus
menu.add_cascade(label='Support', menu=new_item)
menu.add_cascade(label='About',menu=new_item1)
menu.add_cascade(label='Help',menu=new_item2)
window.config(menu=menu)

window.mainloop()
