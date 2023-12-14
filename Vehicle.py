import random
from tkinter import *
from PIL import Image, ImageTk

class Vehicle:
    def __init__(self,x,y,v=1):
        self.x, self.y, self.v = x, y, v

    def move(self):
        if (self.x > 800):
            self.x = 0
        if (self.x < 0):
            self.x = 800
        self.x += self.v

class River (Vehicle):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)


class Log_s (River):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)
        self.img = PhotoImage(file = 'small_log.png')
        self.w, self.h = 146, 45

    def on_drift(self, frog):
        if ((self.x - self.w + frog.w < frog.x < self.x) and (self.y < frog.y < self.y + self.h - frog.h)):
            return 1
        else:
            return 0

    def drift(self,frog):
        if (self.on_drift(frog)):
            frog.x += self.v
    
    def display(self,window):
        window.create_image(self.x, self.y, image=self.img, anchor='ne')

class Log_l (River):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)
        self.img = PhotoImage(file = 'large_log.png')
        self.w, self.h = 202, 45

    def on_drift(self, frog):
        if ((self.x - self.w + frog.w < frog.x < self.x) and (self.y < frog.y < self.y + self.h - frog.h)):
            return 1
        else:
            return 0

    def drift(self,frog):
        if (self.on_drift(frog)):
            frog.x += self.v
    
    def display(self,window):
        window.create_image(self.x, self.y, image=self.img, anchor='ne')

class Turtle (River):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)
        if (v < 0):
            self.img = PhotoImage(file = 'turtle_left.png')
        else:
            self.img = PhotoImage(file = 'turtle_right.png')
        self.w, self.h = 52, 45

    def on_drift(self, frog):
        if ((self.x - self.w + frog.w -10 < frog.x < self.x + 10) and (self.y < frog.y < self.y + self.h - frog.h)):
            return 1
        else:
            return 0

    def drift(self,frog):
        if (self.on_drift(frog)):
            frog.x += self.v

    def display(self,window):
        window.create_image(self.x, self.y, image=self.img, anchor='ne')

class Road (Vehicle):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)

class Car (Road):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)
        if (v < 0):
            cars = ["car1_left.png", "car2_left.png", "car3_left.png", "car4_left.png", "car5_left.png"]
        else:
            cars = ["car1_right.png", "car2_right.png", "car3_right.png", "car4_right.png", "car5_right.png"]
        car = random.choice(cars)
        self.img = PhotoImage(file = car)
        self.w, self.h = 59, 40

    def display(self,window):
        window.create_image(self.x, self.y, image=self.img, anchor='ne')

class Truck (Road):
    def __init__(self, x, y, v=1):
        super().__init__(x, y, v)
        self.w, self.h = 119, 50
        if (v < 0):
            trucks = ["truck1_left.png", "truck2_left.png"]
        else:
            trucks = ["truck1_right.png", "truck2_right.png"]
        truck = random.choice(trucks)
        self.img = PhotoImage(file = truck)

    def display(self,window):
        window.create_image(self.x, self.y, image=self.img, anchor='ne')
