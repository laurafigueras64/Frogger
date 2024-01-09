from tkinter import *
import time
import keyboard
from PIL import Image, ImageTk
from Vehicle import *
from Frog import *
TK_SILENCE_DEPRECATION=1

# Global variables
state = 1
pressed = False

root = Tk() # creem un objecte Tkinter
window = Canvas(root, width=600, height=780)
window.pack() # ho mostrem
bg = ImageTk.PhotoImage(Image.open("background.png"))

def pressbutt():
    global pressed
    pressed = not pressed

window.create_text(300,390,text="INICI")
button = Button(root,text="<>",command=pressbutt)
button.pack()
button.place(x=300,y=500,anchor="n")

# pantalla inicial
while not pressed:
    window.update()

window.delete("all")

button.place_forget()
button.pack_forget()
window.update()

window.create_text(300,390,text="MENU")
button.pack()
button.place(x=300,y=700,anchor="n")
btt1 = Button(root,text="btt1")
btt1.pack()
btt1.place(x=300,y=500,anchor="n")
btt2 = Button(root,text="btt2")
btt2.pack()
btt2.place(x=300,y=550,anchor="n")
btt3 = Button(root,text="btt3")
btt3.pack()
btt3.place(x=300,y=600,anchor="n")

while pressed:
    window.update()

window.delete("all")
button.place_forget()
button.pack_forget()
btt1.place_forget()
btt1.pack_forget()
btt2.place_forget()
btt2.pack_forget()
btt3.place_forget()
btt3.pack_forget()
window.update()

window.create_text(300,390,text="FROG")
button.pack()
button.place(x=300,y=700,anchor="n")
btt_lft = Button(root,text="<-")
btt_lft.pack()
btt_lft.place(x=100,y=500,anchor="n")
btt_rght = Button(root,text="->")
btt_rght.pack()
btt_rght.place(x=500,y=500,anchor="n")


# pantalla tria frog
while not pressed:
    window.update()

window.delete("all")
button.place_forget()
button.pack_forget()
btt_rght.place_forget()
btt_rght.pack_forget()
btt_lft.place_forget()
btt_lft.pack_forget()
window.update()

# part 0: inicialitzar el joc: crear carrils, cotxes, etc.
cars = []
cars.append(Car(30, 670, 5))
cars.append(Car(100, 670, 5))
cars.append(Car(300, 670, 5))
cars.append(Car(590, 670, 5))
cars.append(Truck(300, 610, 3))
cars.append(Car(140, 610, 3))
cars.append(Car(70, 610, 3))
cars.append(Car(500, 610, 3))
cars.append(Car(30, 550, -10))
cars.append(Car(400, 550, -10))
cars.append(Car(500, 550, -10))
cars.append(Car(500, 490, -5))
cars.append(Car(430, 490, -5))
cars.append(Truck(310, 490, -5))
cars.append(Car(20, 490, -5))
cars.append(Car(0, 430, -3))
cars.append(Car(100, 430, -3))
cars.append(Car(370, 430, -3))
cars.append(Car(500, 430, -3))
cars.append(Car(570, 430, -3))
river = []
river.append(Log_s(40, 280, 5))
river.append(Turtle(200, 280, 5))
river.append(Turtle(260, 280, 5))
river.append(Turtle(320, 280, 5))
river.append(Log_l(550, 280, 5))
river.append(Log_s(60, 220, -4))
river.append(Log_s(210, 220, -4))
river.append(Log_s(360, 220, -4))
river.append(Log_s(600, 220, -4))
river.append(Log_l(40, 160, 7))
river.append(Log_l(340, 160, 7))
river.append(Turtle(500, 160, 7))
river.append(Log_l(40, 100, -6))
river.append(Log_s(250, 100, -6))
river.append(Log_s(400, 100, -6))

frog = Frog(320,734, 40, 33)

while True:
    window.delete("all")
    window.create_image(600,0,image=bg,anchor='ne')

    # part 1: detecció de tecles pitjades
    if keyboard.is_pressed("esc"):
        break

    # part 2: moure els elements del joc
    for c in cars:
        c.move()
    for r in river:
        r.move()
    frog.move()

    # part 3: detecció de xocs o navegacions
    for c in cars:
        if (frog.crash(c)):
            state = 0
            window.create_oval(200,200,300,300, fill="red")
        
    if (frog.drown(river)):
        window.create_oval(200,200,300,300, fill="red")
        state = 0
    else:
        for r in river:
            r.drift(frog)

    if state == 0:
        break

    # part 4: pintar pantalla: cotxes carrils, granota, etc.
    for c in cars:
        c.display(window)
    for r in river:
        r.display(window)
    frog.paint(window)
    window.update()  # necessari per repintar la pantalla

    time.sleep(50/1000) # 50 milisegons

button.pack()
button.place(x=300,y=700,anchor="n")

while pressed:
    if keyboard.is_pressed("esc"):
        break
    window.create_image(600,0,image=bg,anchor='ne')
    for c in cars:
        c.display(window)
    for r in river:
        r.display(window)
    frog.paint(window)
    window.update()