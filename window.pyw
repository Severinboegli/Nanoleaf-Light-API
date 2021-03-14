from tkinter.constants import COMMAND, RIDGE
from nanoleafapi import nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
import time
import tkinter as tk
from tkinter import Canvas, Frame, Label, filedialog, Text
import os

nl = nanoleaf.Nanoleaf("192.168.1.117")
root = tk.Tk()
root.resizable(height=True, width=True)
#root.minsize(height=600, width=900)
root.geometry("1000x600")
root.title("Nanoleaf Light API")


"""
========================================
Funktionen
========================================
"""

print(nl.get_power())


def light_switch():
    if nl.get_power() == False:
        nl.power_on()
        print("Licht an")
    else:
        nl.power_off()
        print("Licht aus")


def orange():
    nl.set_color(ORANGE)
    print("Licht ist auf Orange eingestellt.")


def rot():
    nl.set_color(RED)
    print("Licht ist auf Rot eingestellt.")


def dark_orange():
    nl.set_color((255, 81, 35))


def yellow():
    nl.set_color(YELLOW)
    print("Licht ist auf Gelb eingestellt.")


def light_retro():
    nl.set_effect("Retro")


def sunset_dynamic():
    nl.set_effect("Sunset Dynamic")


def Goldfox():
    nl.set_effect("Goldfox")


def Be_Productive():
    nl.set_effect("Be Productive")


def pluszehn():
    nl.increment_brightness(10)


def minuszehn():
    nl.increment_brightness(-10)


def plusvierzig():
    nl.increment_brightness(40)


def minusvierzig():
    nl.increment_brightness(-40)


"""
========================================
Haupt und Unterseiten
========================================
"""

window = tk.Frame(root, bg="#202020")
window.place(relheight=1, relwidth=1)

main = tk.Frame(window, bg="white")
main.place(relheight=0.9, relwidth=0.95, relx=0.025, rely=0.05)


"""
========================================
Titleleiste
========================================
"""

title = tk.Frame(main)
title.place(relheight=0.10, relwidth=0.95, relx=0.025, rely=0.075)

switch = tk.Button(title, text="On / Off", command=light_switch,
                   bg="#c4c4c4", font=('aris', 12, 'bold'))
switch.place(relheight=1, relwidth=0.2, relx=0)

titletext = tk.Label(title, text="Nanoleaf API",
                     bg="#efefef", font=('aris', 18, 'bold'))
titletext.place(relheight=1, relwidth=0.4, relx=0.3)

schliessen = tk.Button(title, text="Exit", command=root.destroy,
                       bg="#c4c4c4", font=('aris', 12, 'bold'))
schliessen.place(relheight=1, relwidth=0.2, relx=0.8)


"""
========================================
Box1
========================================
"""

box1 = tk.Frame(main, bg="#202020")
box1.place(relheight=0.2, relwidth=0.95, relx=0.025, rely=0.225)

effekte = tk.Label(box1, bg="#202020", fg="#c4c4c4",
                   text="Effekte", font=('aris', 15, 'bold'))
effekte.place(relheight=0.35, relwidth=0.6, relx=0.2, rely=0.05)

box11 = tk.Frame(box1, bg="#202020")
box11.place(relheight=0.5, relwidth=1, rely=0.5)

box1button1 = tk.Button(box11, bg="#c4c4c4", command=light_retro,
                        text="Retro", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.008)

box1button1 = tk.Button(box11, bg="#c4c4c4", command=sunset_dynamic,
                        text="Sunset Dynamic", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.256)

box1button1 = tk.Button(box11, bg="#c4c4c4", command=Goldfox,
                        text="Goldfox", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.504)

box1button1 = tk.Button(box11, bg="#c4c4c4", command=Be_Productive,
                        text="Be Productive", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.752)
"""
========================================
Box2
========================================
"""

box2 = tk.Frame(main, bg="#202020")
box2.place(relheight=0.2, relwidth=0.95, relx=0.025, rely=0.475)

Brightnesse = tk.Label(box2, bg="#202020", fg="#c4c4c4",
                       text="Brightnesse", font=('aris', 15, 'bold'))
Brightnesse.place(relheight=0.35, relwidth=0.6, relx=0.2, rely=0.05)

box21 = tk.Frame(box2, bg="#202020")
box21.place(relheight=0.5, relwidth=1, rely=0.5)

box1button1 = tk.Button(box21, bg="#c4c4c4", command=minusvierzig,
                        text="-40%", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.008)

box1button1 = tk.Button(box21, bg="#c4c4c4", command=minuszehn,
                        text="-10%", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.256)

box1button1 = tk.Button(box21, bg="#c4c4c4", command=pluszehn,
                        text="+10%", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.504)

box1button1 = tk.Button(box21, bg="#c4c4c4", command=plusvierzig,
                        text="+40%", font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.752)

"""
========================================
Box3
========================================
"""

box3 = tk.Frame(main, bg="#202020")
box3.place(relheight=0.2, relwidth=0.95, relx=0.025, rely=0.725)

Farbe = tk.Label(box3, bg="#202020", fg="#c4c4c4",
                 text="Farbe", font=('aris', 15, 'bold'))
Farbe.place(relheight=0.35, relwidth=0.6, relx=0.2, rely=0.05)


box31 = tk.Frame(box3, bg="#202020")
box31.place(relheight=0.5, relwidth=1, rely=0.5)

box1button1 = tk.Button(box31, bg="#c4c4c4", text="Gelb", command=yellow,
                        font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.008)

box1button1 = tk.Button(box31, bg="#c4c4c4", text="Orange", command=orange,
                        font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.256)

box1button1 = tk.Button(box31, bg="#c4c4c4", text="Dunkel-Orange", command=dark_orange,
                        font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.504)

box1button1 = tk.Button(box31, bg="#c4c4c4", text="Rot", command=rot,
                        font=('aris', 10, 'bold'))
box1button1.place(relheight=0.8, relwidth=0.24, relx=0.752)


root.mainloop()
