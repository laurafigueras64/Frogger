from tkinter import *
import time
import keyboard
from PIL import Image, ImageTk
from Vehicle import *
from Frog import *
TK_SILENCE_DEPRECATION=1

# Global variables
state = 1   # 1 alive, 0 dead, 3 win
pressed = True
game_time = 0
wich_frog = 0
diff = 1

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
button.place(x=300,y=700,anchor="n")

# frog images for the menu
frog_small = []
frog_big = []
for i in range(6):
    frog_small.append(ImageTk.PhotoImage(Image.open("s.frog"+str(i+1)+".png")))
    frog_big.append(ImageTk.PhotoImage(Image.open("b.frog"+str(i+1)+".png")))

def frog_l():
    global wich_frog
    wich_frog = (wich_frog - 1) % 6

def frog_r():
    global wich_frog
    wich_frog = (wich_frog + 1) % 6

def diff_f():
    global diff
    diff = 0.75

def diff_n():
    global diff
    diff = 1

def diff_d():
    global diff
    diff = 1.75

window.create_text(300,200,text="FROG")
button.pack()
button.place(x=300,y=700,anchor="center")
btt_lft = Button(root,text="<-",command=frog_l)
btt_lft.pack()
btt_lft.place(x=50,y=390,anchor="center")
frog_str = "frog " + str(wich_frog)
window.create_text(300,390,text=frog_str,anchor="center")
btt_rght = Button(root,text="->",command=frog_r)
btt_rght.pack()
btt_rght.place(x=550,y=390,anchor="center")
btt_diff_f = Button(root, text="easy", command=diff_f)
btt_diff_f.pack()
btt_diff_f.place(x=300,y=550,anchor="center")
btt_diff_n = Button(root, text="normal", command=diff_n)
btt_diff_n.pack()
btt_diff_n.place(x=300,y=580,anchor="center")
btt_diff_d = Button(root, text="dificult", command=diff_d)
btt_diff_d.pack()
btt_diff_d.place(x=300,y=610,anchor="center")


# pantalla tria frog
while pressed:
    window.create_image(600,0,image=bg,anchor='ne')
    window.create_text(300,220,text="CHOOSE YOUR FROG",font="Chalkduster 40 bold")
    frog_str = "frog " + str(wich_frog + 1)
    window.create_image(150,390,image=frog_small[(wich_frog - 1) % 6],anchor="center")
    window.create_image(300,390,image=frog_big[(wich_frog) % 6],anchor="center")
    window.create_image(450,390,image=frog_small[(wich_frog + 1) % 6],anchor="center")
    window.update()
    window.delete("all")

window.delete("all")
button.place_forget()
button.pack_forget()
btt_rght.place_forget()
btt_rght.pack_forget()
btt_lft.place_forget()
btt_lft.pack_forget()
btt_diff_d.pack_forget()
btt_diff_d.place_forget()
btt_diff_f.pack_forget()
btt_diff_f.place_forget()
btt_diff_n.pack_forget()
btt_diff_n.place_forget()
window.update()

# part 0: inicialitzar el joc: crear carrils, cotxes, etc.
cars = []
cars.append(Car(30, 670, diff, 5))
cars.append(Car(300, 670, diff, 5))
cars.append(Car(590, 670, diff, 5))
cars.append(Truck(300, 610, diff, 3))
cars.append(Car(140, 610, diff, 3))
cars.append(Car(70, 610, diff, 3))
cars.append(Car(500, 610, diff, 3))
cars.append(Car(30, 550, diff, -10))
cars.append(Car(400, 550, diff, -10))
cars.append(Car(500, 550, diff, -10))
cars.append(Car(500, 490, diff, -5))
cars.append(Car(430, 490, diff, -5))
cars.append(Truck(310, 490, diff, -5))
cars.append(Car(20, 490,diff, -5))
cars.append(Car(0, 430,diff, -3))
cars.append(Car(370, 430,diff, -3))
cars.append(Car(500, 430,diff, -3))
cars.append(Car(570, 430,diff, -3))
river = []
river.append(Log_s(40, 280,diff, 5))
river.append(Turtle(200, 280,diff, 5))
river.append(Turtle(260, 280,diff, 5))
river.append(Turtle(320, 280,diff, 5))
river.append(Log_l(550, 280,diff, 5))
river.append(Log_s(60, 220,diff, -4))
river.append(Log_s(210, 220,diff, -4))
river.append(Log_s(360, 220,diff, -4))
river.append(Log_s(600, 220,diff, -4))
river.append(Log_l(40, 160,diff, 7))
river.append(Log_l(340, 160,diff, 7))
river.append(Turtle(500, 160,diff, 7))
river.append(Log_l(40, 100,diff, -6))
river.append(Log_s(250, 100,diff, -6))
river.append(Log_s(400, 100,diff, -6))
frog = Frog(320,734,wich_frog)

while True:
    window.delete("all")
    window.create_image(600,0,image=bg,anchor='ne')
    window.create_text(300,380,text=str(int(game_time)), font="Chalkduster 50 bold", fill="black")
    window.create_text(300,30,text="100    250    500    750    1000", font="Chalkduster 30 bold", fill="black")

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
        
    if (frog.drown(river)):
        state = 0
    else:
        for r in river:
            r.drift(frog)

    if (frog.y < 100):
        state = 3

    if state != 1:
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
    if state == 3:
        if (frog.x < 90):
            str_score = str(100-int(game_time))
        elif (frog.x < 220):
            str_score = str(250-int(game_time))
        elif (frog.x < 340):
            str_score = str(500-int(game_time))
        elif (frog.x < 460):
            str_score = str(750-int(game_time))
        elif (frog.x < 590):
            str_score = str(1000-int(game_time))
        window.create_text(300,220,text="VICTORY!",font="Chalkduster 70 bold")
        window.create_text(300,380,text="YOUR SCORE: "+str_score,font="Chalkduster 40 bold")

    if state == 0:
        window.create_text(300,220,text="DEFEAT!",font="Chalkduster 70 bold")

    window.update()