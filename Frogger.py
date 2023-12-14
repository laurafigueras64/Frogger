from tkinter import *
import time
import keyboard
from PIL import Image, ImageTk
from Vehicle import *
from Frog import *
TK_SILENCE_DEPRECATION=1

state = 1

root = Tk() # creem un objecte Tkinter
window = Canvas(root, width=600, height=780)
window.pack() # ho mostrem
bg = ImageTk.PhotoImage(Image.open("background.png"))

# part 0: inicialitzar el joc: crear carrils, cotxes, etc.
cars = []
cars.append(Car(30, 670, 5))
cars.append(Car(100, 670, 5))
cars.append(Car(300, 670, 5))
cars.append(Car(500, 670, 5))
cars.append(Car(590, 670, 5))
cars.append(Truck(300, 610, 3))
cars.append(Car(140, 610, 3))
cars.append(Car(70, 610, 3))
cars.append(Car(0, 610, 3))
cars.append(Car(500, 610, 3))
cars.append(Car(30, 550, -10))
cars.append(Car(100, 550, -10))
cars.append(Car(400, 550, -10))
cars.append(Car(500, 550, -10))
cars.append(Car(500, 490, -5))
cars.append(Car(430, 490, -5))
cars.append(Truck(310, 490, -5))
cars.append(Car(50, 490, -5))
cars.append(Car(30, 430, -3))
cars.append(Car(100, 430, -3))
cars.append(Car(300, 430, -3))
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
    else:
        for r in river:
            r.drift(frog)
    

    # part 4: pintar pantalla: cotxes carrils, granota, etc.
    for c in cars:
        c.display(window)
    for r in river:
        r.display(window)
    frog.paint(window)
    window.update()  # necessari per repintar la pantalla

    time.sleep(50/1000) # 50 milisegons

