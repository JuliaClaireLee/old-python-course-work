# ------------------------------------------------------
#        Name: Julia Lee AND Yolanda Chigiji
#    Filename: Aquarium.py
#        Date: 11/14/2018
#      Description: Fish Tank
# ------------------------------------------------------
from graphics import *
from random import randint
import random
import webbrowser
class Fish:

    def __init__(self, loc, deltaX, deltaY, Direction):
        """ Takes in a Point(x,y) for loc """
        self.Position = loc
        self.direction = Direction
        self.deltaY = deltaY
        self.deltaX = deltaX
        if self.direction == "LEFT":
            self.body = Oval(Point(loc.getX() - 40, loc.getY() - 20),
                         Point(loc.getX() + 40, loc.getY() + 20))
            self.body.setFill(color_rgb(100, 255, 150))
            self.tail = Oval(Point(loc.getX() + 30, loc.getY() - 30),
                         Point(loc.getX() + 50, loc.getY() + 30))
            self.tail.setFill("red")
            self.eye = Circle(Point(loc.getX() - 20, loc.getY() - 5) , 5)
            self.eye.setFill(color_rgb(0,0,0))
        else:
            self.body = Oval(Point(loc.getX() +40, loc.getY() + 20),
                         Point(loc.getX() - 40, loc.getY() - 20))
            self.body.setFill(color_rgb(100, 255, 150))
            self.tail = Oval(Point(loc.getX() - 30, loc.getY() + 30),
                         Point(loc.getX() - 50, loc.getY() - 30))
            self.tail.setFill("red")
            self.eye = Circle(Point(loc.getX() + 20, loc.getY() + 5) , 5)
            self.eye.setFill(color_rgb(0,0,0))
            self.fin = Polygon([Point(self.Position.getX(),self.body.getCenter().getY()+40),
                        Point(self.body.getCenter().getX()+15, self.body.getCenter().getY()+20),
                         Point(self.body.getCenter().getX()-15, self.body.getCenter().getY()+20)])
            self.fin.setFill("red")
    def draw(self, win):
         self.tail.draw(win)
         self.body.draw(win)
         self.eye.draw(win)

    def move(self):
        self.body.move(self.deltaX, self.deltaY)
        self.tail.move(self.deltaX, self.deltaY)
        self.eye.move(self.deltaX, self.deltaY)
        if (self.eye.getCenter().getX() + 40>  700 - 40 or  self.eye.getCenter().getX()-40< 40):
            self.deltaX = self.deltaX * -1
        if (self.eye.getCenter().getY()+20  >  517 - 20 or self.eye.getCenter().getY()-20  < 20):
            self.deltaY = self.deltaY * -1
class RoundFish(Fish):
  def __init__(self, position, deltaX, deltaY):
       self.deltaY = deltaY
       self.deltaX = deltaX
       red = randint(0,255)
       green = randint(0,255)
       blue = randint(0,255)
       p1 = Point(position.getX()-40, position.getY()-20)
       p2 = Point(position.getX()+40, position.getY()+20)
       self.body = Circle(position, 40)
       self.body.setFill(color_rgb(red, green, blue))
       p1 = Point(position.getX()+30, position.getY()-30)
       p2 = Point(position.getX()+50, position.getY()+30)
       self.tail = Polygon([Point(position.getX()+30, position.getY()),
                          Point(position.getX()+70, position.getY()+30),
                           Point(position.getX()+70, position.getY()-20)])
       self.tail.setFill(color_rgb(red, green, blue))
       center2 = Point(position.getX()-15, position.getY()-5 )
       self.eye = Circle( center2, 5 )
       self.eye.setFill( "black" )
       self.fin = Polygon([Point(self.body.getCenter().getX(),self.body.getCenter().getY()+65),
                        Point(self.body.getCenter().getX()+20, self.body.getCenter().getY()+30),
                         Point(self.body.getCenter().getX()-20, self.body.getCenter().getY()+30)])
       self.fin.setFill(color_rgb(red, green, blue))
  def draw( self, win ):
      self.fin.draw( win )
      self.tail.draw( win )
      self.body.draw( win )
      self.eye.draw( win )
  def move(self):
     self.body.move(self.deltaX, self.deltaY)
     self.tail.move(self.deltaX, self.deltaY)
     self.eye.move(self.deltaX, self.deltaY)
     self.fin.move(self.deltaX, self.deltaY)
     if (self.body.getCenter().getX() >  700 - 40 or self.body.getCenter().getX() < 40):
           self.deltaX = self.deltaX * -1
     if (self.body.getCenter().getY() >  517 - 20 or self.body.getCenter().getY() < 20):
         self.deltaY = self.deltaY * -1
  def Clicked(self, Point):
     x1= self.eye.getCenter().getX() - 30
     x2= self.eye.getCenter().getX() + 30
     y1= self.eye.getCenter().getY() - 30
     y2= self.eye.getCenter().getY() + 30
 
     if Point.getX() >  x1 and Point.getX() < x2 and Point.getY() >  y1 and Point.getY() < y2:
         self.fin.undraw()
         self.tail.undraw( )
         self.body.undraw()
         self.eye.undraw()
         return True
     else:
         return False
class TriFish(Fish):
    def __init__(self, position, deltaX, deltaY):
        self.Position = position 
        self.deltaY = deltaY
        self.deltaX = deltaX
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        self.body = Polygon([Point(position.getX(), position.getY()),
                          Point(position.getX()+50, position.getY()+60),
                           Point(position.getX()+50, position.getY()-60)])
        self.body.setFill(color_rgb(red, green, blue))
        self.tail = Polygon([Point(position.getX()+30, position.getY()),
                          Point(position.getX()+70, position.getY()+30),
                           Point(position.getX()+70, position.getY()-20)])
        self.tail.setFill(color_rgb(red, green, blue))
        self.eye = Circle( Point(position.getX()+15, position.getY()+7),5)
        self.eye.setFill( "black" )       
def main():
    BackGround = Image(Point(350,258), "Tank2.gif")
    win = GraphWin("Fish Tank", 700, 517)
    BackGround.draw(win)
    Pressedkey = win.getKey()
    fishies = []
    Roundfish = []
    Trifish = []
    option = ["RIGHT", "LEFT"]
    clickedPt = win.checkMouse()
    removed = False
    for i in range (randint(1,5)):
        clickedPt = win.getMouse()
        fishies.append(Fish(clickedPt, randint(-10,15),randint(-10,10), random.choice(option)))
        fishies[i].draw(win)
        fishies[i].move()
    for i  in  range (randint(1,3)):
        clickedPt = win.getMouse()
        Roundfish.append(RoundFish(clickedPt, randint(2, 5), randint(1,5)))
        Roundfish[i].draw(win)
    for i in range (randint(1,2)):
        clickedPt = win.getMouse()
        Trifish.append(TriFish(clickedPt, randint(-10,15), randint(1,11)))
        Trifish[i].draw(win)
        Trifish[i].move()
           

    Pressedkey = win.getKey()
    webbrowser.open("https://www.youtube.com/watch?v=MyqVv30dcVI") 
    while(Pressedkey == "space"):
        for fish in Trifish:
              fish.move()
        for fish in fishies:
            fish.move()
        for fish in Roundfish:
            fish.move()
        
                 

if __name__ == "__main__":
    main()
