import keyboard
from Vehicle import *
from tkinter import *
from PIL import Image, ImageTk

class Frog:
    # tindrem la posicio (x,y), alçada(h), amplada(w), velocitat(v)
    def __init__(self,x,y,w,h):
        self.x, self.y = x, y
        self.w, self.h = 40, 33
        self.img = PhotoImage(file = 'frog1.png')

    def move(self):
        if keyboard.is_pressed("right arrow"):
            if (self.x < 612-30):
                self.x += 30
        if keyboard.is_pressed("up arrow"):
            if (120 < self.y < 360):
                if (self.y > 90):
                    self.y -= 60
            else:
                if (self.y > 90):
                    self.y -= 30
        if keyboard.is_pressed("left arrow"):
            if (self.x - 40 > 20):
                self.x -= 30
        if keyboard.is_pressed("down arrow"):
            if (100 < self.y < 360):
                if (self.y + 33 < 750):
                    self.y += 60
            else:
                if (self.y + 33 < 750):
                    self.y += 30

    def paint(self,window):
        window.create_image(self.x,self.y,image=self.img,anchor='ne')
    
    def crash(self,car):
        if (car.x - car.w < self.x < car.x + self.w) and (car.y - car.h < self.y < car.y + self.h):
            return 1
        else: return 0

    def drown(self,drifts):
        if (330 < self.y or self.y < 100): return 0
        aux = 0
        for d in drifts:
            if ((d.x - d.w + self.w < self.x < d.x) and (d.y < self.y < d.y + d.h - self.h)):
                aux = 1
    
        if (aux == 1): return 0
        else: return 1

