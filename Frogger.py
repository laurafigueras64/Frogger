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
game_time = 0
wich_frog = 0

root = Tk() # creem un objecte Tkinter
window = Canvas(root, width=600, height=780)
window.pack() # ho mostrem
bg = ImageTk.PhotoImage(Image.open("background.png"))

def pressbutt():
    global pressed
    pressed = not pressed

window.create_text(300,200,text="INICI")
button = Button(root,text="<>",command=pressbutt)
button.pack()
button.place(x=300,y=580,anchor="n")

# pantalla inicial
while not pressed:
    window.update()

window.delete("all")

button.place_forget()
button.pack_forget()
window.update()

# frog images for the menu
frog_small = []
frog_big = []
for i in range(6):
    frog_imag = Image.open("b.frog"+str(i+1)+".png")
    resized = frog_imag.resize((70,58))
    frog_small.append(ImageTk.PhotoImage(resized))
    frog_big.append(PhotoImage(file="b.frog"+str(i+1)+".png"))

def frog_l():
    global wich_frog
    wich_frog = (wich_frog - 1) % 6

def frog_r():
    global wich_frog
    wich_frog = (wich_frog + 1) % 6

window.create_text(300,200,text="FROG")
button.pack()
button.place(x=300,y=580,anchor="center")
btt_lft = Button(root,text="<-",command=frog_l)
btt_lft.pack()
btt_lft.place(x=50,y=390,anchor="center")
frog_str = "frog " + str(wich_frog)
window.create_text(300,390,text=frog_str,anchor="center")
btt_rght = Button(root,text="->",command=frog_r)
btt_rght.pack()
btt_rght.place(x=550,y=390,anchor="center")


# pantalla tria frog
while pressed:
    window.create_text(300,200,text="FROG")
    frog_str = "frog " + str(wich_frog + 1)
    window.create_text(300,390,text=frog_str,anchor="center")
    frg_l = Label(root, image=frog_small[(wich_frog - 1) % 6])
    frg_l.pack()
    frg_l.place(x=150,y=390,anchor="center")
    frg_r = Label(root, image=frog_small[(wich_frog + 1) % 6])
    frg_r.pack()
    frg_r.place(x=450,y=390,anchor="center")
    frg = Label(root, image=frog_big[wich_frog])
    frg.pack()
    frg.place(x=300,y=390,anchor="center")
    window.update()
    window.delete("all")
    frg.pack_forget()
    frg.place_forget()
    frg_l.pack_forget()
    frg_l.place_forget()
    frg_r.pack_forget()
    frg_r.place_forget()

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

frog = Frog(320,734,wich_frog)

while True:
    window.delete("all")
    window.create_image(600,0,image=bg,anchor='ne')
    min = int(game_time // 60)
    seg = int(game_time - min*60)
    time_str = str(min) + ":" + str(seg)
    window.create_text(300,370,text=time_str)

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
    game_time = game_time + 0.091

button.pack()
button.place(x=300,y=580,anchor="n")

while not pressed:
    if keyboard.is_pressed("esc"):
        break
    window.create_image(600,0,image=bg,anchor='ne')
    for c in cars:
        c.display(window)
    for r in river:
        r.display(window)
    frog.paint(window)

    #scoreboard

    window.update()