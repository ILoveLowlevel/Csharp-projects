import pygame as py
import random as rnd
from pygame.locals import *
py.init()
screen = py.display.set_mode((1000, 600))
clock = py.time.Clock()
MousePos_X = 0
MousePos_Y = 0
SizeX,SizeY = 10,10
RectLast_X = MousePos_X + SizeX
RectLast_Y = MousePos_Y + SizeY
Rects = []
def DrawRectLine(sizex,sizey):
    SizeX = sizex
    SizeY = sizey
    RectLast_X = MousePos_X + SizeX
    RectLast_Y = MousePos_Y + SizeY
    new = py.rect(0,0,100,100)
Rnd_int = rnd.randint(0,255)
Rects.append(py.draw.rect(screen,(255,0,0),(10,10,300,100)))
Rects.append(py.draw.rect(screen,(0,255,0),(10,10,200,50)))
Rects.append(py.draw.rect(screen,(0,0,255),(10,10,100,50)))
Rects.append(py.draw.rect(screen,(Rnd_int,Rnd_int,Rnd_int),(Rnd_int,Rnd_int,Rnd_int,Rnd_int)))
AllRectCoordinates = []
def RainbowTiles():
    x1,y1 = 0,0
    x2,y2 = 10,10
    while y2 < 600:
        while x2 < 1000:
            Rnd_int = rnd.randint(0,255)
            Rnd_int2 = rnd.randint(0,255)
            Rnd_int3 = rnd.randint(0,255)
            AllRectCoordinates.append((x1,y1,x2,y2))
            Rects.append(py.draw.rect(screen,(Rnd_int,Rnd_int2,Rnd_int3),(x1,y1,x2,y2)))
            x1 = x1 + 10
            x2 = x2 + 10
        x1,x2 = 0,10
        y1 = y1 + 10
        y2 = y2 + 10

Entities = []
class RainbowTilesEnity():

    def __init__(self):
        self.ItsCoordinat = ()
        x1,y1 = 0,0
        x2,y2 = 10,10
        while y2 < 600:
            while x2 < 1000:
                Rnd_int = rnd.randint(0,255)
                Rnd_int2 = rnd.randint(0,255)
                Rnd_int3 = rnd.randint(0,255)
                AllRectCoordinates.append((x1,y1,x2,y2))
                Rects.append(py.draw.rect(screen,(Rnd_int,Rnd_int2,Rnd_int3),(x1,y1,x2,y2)))
                x1 = x1 + 10
                x2 = x2 + 10
            x1,x2 = 0,10
            y1 = y1 + 10
            y2 = y2 + 10
    def MouseOver(self):
        for rect in Rects:
            if rect.collidepoint(py.mouse.get_pos()):
                self.ItsCoordinat = (rect.topleft,rect.bottomright)
                (a,b) = rect.size
                a = a + 100
                b = b + 100
                rect.size = (a,b)
        return self.ItsCoordinat


newRainbowTilesEntity = RainbowTilesEnity()
Entities.append(newRainbowTilesEntity)



def main():
   global newrects
   newrects = (0,0,0,0)

   while True:
      rect = py.Rect(10, 10, 100, 60)
      for event in py.event.get():
            if event.type == QUIT:
               py.quit()
               return
            if event.type == py.MOUSEBUTTONUP:
                pos = py.mouse.get_pos()

      ChangedOverRideRect=newRainbowTilesEntity.MouseOver()
      print(ChangedOverRideRect)
    #  py.draw.rect(screen,(255,0,0),ChangedOverRideRect)


      MousePos_X , MousePos_Y = py.mouse.get_pos()
      print(f"X = {MousePos_X} , Y = {MousePos_Y}")
      left, middle, right = py.mouse.get_pressed()
      if left:
          Rnd_int = rnd.randint(0,255)
          Rnd_int2 = rnd.randint(0,255)
          Rnd_int3 = rnd.randint(0,255)
          newrects = (MousePos_X +10 ,MousePos_Y+10 ,MousePos_X ,MousePos_Y )
      for rect in Rects:
        rect
      py.display.flip()
      py.display.update()
      clock.tick(60)

# Execute game:
main()