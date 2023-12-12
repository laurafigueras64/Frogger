import keyboard
from Vehicle import *

class Frog:
    # tindrem la posicio (x,y), alçada(h), amplada(w), velocitat(v)
    def __init__(self,x,y,w,h):
        self.x, self.y, self.w, self.h = x, y, w, h

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
            if (120 < self.y < 360):
                if (self.y + 33 < 750):
                    self.y += 60
            else:
                if (self.y + 33 < 750):
                    self.y += 30

    def paint(self,window,img):
        window.create_image(self.x,self.y,image=img,anchor='ne')
        #window.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.h,fill="green")
    
    def crash(self,window,car):
        if (self.x < car.x + car.w) & (self.x + self.w > car.x) & (self.y < car.y + car.h) & (self.y + self.h > car.y):
            window.create_oval(200,200,300,300, fill="red")

    #def drown(self,drift):

    def ondrift(self,drift):
        if (isinstance(drift,Log)):
            if ((drift.x - 163 < self.x < drift.x) and (drift.y < self.y < drift.y + 5)):
                self.x += drift.v
        #elif (drift is Turtle):
            #if ((drift.x - 163 < self.x < drift.x) and (drift.y < self.y < drift.y + 5)):
            #   self.x += drift.v
