from tkinter import *
from PIL import Image, ImageTk

class Vehicle:
    def __init__(self,x,y,img,v=1):
        self.x, self.y, self.v, self.img = x, y, v, img

    def move(self):
        if (self.x > 800):
            self.x = 0
        if (self.x < 0):
            self.x = 800
        self.x += self.v

class River (Vehicle):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)

    #def ondrift()

class Log (River):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)
        #self.img = PhotoImage(file = 'log.png')
    
    def display(self,window):
        window.create_image(self.x, self.y, image=self.img, anchor='ne')

class Turtle (River):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)
        self.w, self.h = 30, 20

    def display(self,window):
        window.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill="green")

class Road (Vehicle):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)

class Car (Road):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)
        self.w, self.h = 50, 30

    def display(self,window):
        window.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill="red")

class Truck (Road):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)
        self.w, self.h = 60, 30

    def display(self,window):
        window.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill="blue")

class Trailer (Road):
    def __init__(self, x, y, img, v=1):
        super().__init__(x, y, img, v)
        self.w, self.h = 100, 30

    def display(self,window):
        window.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill="yellow")