from tkinter import *
import time
import keyboard
from PIL import Image, ImageTk
from Vehicle import *
from Frog import *
TK_SILENCE_DEPRECATION=1

root = Tk() # creem un objecte Tkinter
window = Canvas(root, width=600, height=780)
window.pack() # ho mostrem
img = PhotoImage(file = 'frog1.png') 
log = PhotoImage(file = 'log.png') 
bg = ImageTk.PhotoImage(Image.open("background.png"))

# part 0: inicialitzar el joc: crear carrils, cotxes, etc.
cars = []
cars.append(Car(30, 670,log))
cars.append(Truck(30, 610,log, 5))
cars.append(Trailer(30, 550,log, 3))
cars.append(Car(30, 490,log, 2))
cars.append(Trailer(30, 430,log, 3))
river = []
river.append(Log(40, 280, log, 5))
river.append(Log(60, 220, log, -4))
river.append(Log(40, 160, log, 5))
river.append(Log(40, 100, log, 2))
frog = Frog(320,734, 20, 20)

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
        frog.crash(window, c)
    for r in river:
        frog.ondrift(r)

    # part 4: pintar pantalla: cotxes carrils, granota, etc.
    for c in cars:
        c.display(window)
    for r in river:
        r.display(window)
    frog.paint(window,img)
    window.update()  # necessari per repintar la pantalla

    time.sleep(50/1000) # 50 milisegons

