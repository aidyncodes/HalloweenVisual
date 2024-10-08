from graphics import *
import time
import math

# Name: <Aidyn Somerville>
# greetingfinal.py
# This program gives the user two choices. Trick or treat.
# The user can either click the candy box above the kid's head,
#   or they can refuse to interact + get an alternate ending.
#  This homework was fun.

# I certify that this lab is my own work, but I discussed it with
#   <Oscar> in CSL.

def main():

#window settings
     winLength = 600
     winWidth = 750
     win = GraphWin("trick or treat", winLength,winWidth)
     win.setBackground(color_rgb(100,0,0))

#background + doorframe
     door = Rectangle(Point(80,70), Point(520,750))
     door.setFill("black")
     door.setWidth(20)
     door.setOutline("brown")
     door.draw(win)

#feet
     leftFoot = Oval(Point(250,680),Point(290,720))
     rightFoot = Oval(Point(310,680),Point(350,720))
     leftFoot.setFill(color_rgb(250,225,200))
     leftFoot.setOutline(color_rgb(250,225,200))
     rightFoot.setFill(color_rgb(250,225,200))
     rightFoot.setOutline(color_rgb(250,225,200))
     leftFoot.draw(win)
     rightFoot.draw(win)

#dress
     dress = Polygon(Point(winLength/2,400),Point(200,700), Point(400,700))
     dress.setFill("red")
     dress.setOutline("red")
     dress.draw(win)


#head + horns
     head = Circle(Point(winLength/2, winWidth-350), 75)
     head.setFill(color_rgb(250,225,200))
     head.setWidth(20)
     head.setOutline("red")
     head.draw(win)

     horn1 = Polygon(Point(350,350),Point(370,300),Point(375,365))
     horn1.setFill("red")
     horn1.setOutline("red")
     horn1.draw(win)

     horn2 = Polygon(Point(250,350),Point(230,300),Point(225,365))
     horn2.setFill("red")
     horn2.setOutline("red")
     horn2.draw(win)
#eyes
     eyeL = Circle(Point(winLength/2 - 30, winWidth-350), 20)
     eyeL.setFill("white")
     eyeL.setWidth(1)
     eyeL.setOutline("white")
     eyeL.draw(win)

     eyeR = Circle(Point(winLength/2 + 30, winWidth-350), 20)
     eyeR.setFill("white")
     eyeR.setWidth(1)
     eyeR.setOutline("white")
     eyeR.draw(win)

     pupil1 = Circle(Point(winLength/2 + 30, winWidth-350), 7)
     pupil1.setFill("black")
     pupil1.setWidth(1)
     pupil1.setOutline("white")
     pupil1.draw(win)

     pupil2 = Circle(Point(winLength/2 - 30, winWidth-350), 7)
     pupil2.setFill("black")
     pupil2.setWidth(1)
     pupil2.setOutline("white")
     pupil2.draw(win)
     
#setting future background change
     colors = ["red2","green2","purple2","yellow2","magenta3"]

#define text
     textPt = Point(winLength/2,winWidth - 720)
     words = Text(textPt, "trick or treat!")
     words.setTextColor("yellow")
     words.setFace("courier")
     words.setSize(20)
     words.draw(win)
     time.sleep(3)
     
#define choice
     words.setText("Click the candy to give her candy...or else.")
     boxPt1 = (Point(winLength/2-50,winWidth-650))
     boxPt2 = (Point(winLength/2+50,winWidth-600))
     box = Rectangle(boxPt1,boxPt2)
     box.setFill("red")
     box.draw(win)
     lCorner = Polygon(Point(250,125),Point(220,100),Point(220,150))
     lCorner.setFill("red")
     lCorner.draw(win)
     rCorner = Polygon(Point(350,125),Point(380,100),Point(380,150))
     rCorner.setFill("red")
     rCorner.draw(win)
     time.sleep(5)
     
#candy bowl - choice 1
     candyBowl = Image(Point(winLength/2,570),"candy2.png")
     candy = Circle(Point(winLength/2,winWidth-625), 10)
     candy.setFill("purple")
     
#gets last point user clicked
#set x+y, set up loop that offers an if else option.
#if variable pt exists then loop wont run + code continues, but if clicked
#  loop will run "else".
#define existence with "none"
#set filler call so loop will run
#nested loop x with x, y with y

     user = win.checkMouse()
     if user == None:
          call = 7
     else:
          x = user.getX()
          y = user.getY()
          if x>250 and x<350:
               if y>100 and y<150:
                    box.undraw()
                    rCorner.undraw()
                    lCorner.undraw()
                    candyBowl.draw(win)
                    words.setText("happy halloween!!")
                    smile = Polygon(Point(280,430),Point(300,450),Point(320,430))
                    smile.setFill("pink")
                    smile.draw(win)
                    time.sleep(4)
                    win.close()

#monster - choice 2
     box.undraw()
     rCorner.undraw()
     lCorner.undraw()
     
#eyebrows
     leftEyebrow = Line(Point(260,330),Point(300,360))
     leftEyebrow.setWidth(5)
     rightEyebrow = Line(Point(300,360),Point(340,330))
     rightEyebrow.setWidth(5)

#option 2 text
     words.setText("hello...?")
     time.sleep(2)
     words.setText("hand it over.")
     time.sleep(2)

     total = 2

#set width total so it recognizes eye
#loop for countdown + color change + eyes
#eye size change must count with i, but i gets smaller with each loop
#  instead set total count to replace i, setWidth(total)
     for i in range(5, 0, -1):
          words.setText(i)
          time.sleep(1)
          eyeLarge = Circle(Point(winLength/2 - 30, winWidth-350), 20)
          eyeLarge.setFill("white")
          eyeLarge.setWidth(total)
          eyeLarge.setOutline("white")
          eyeLarge.draw(win)
          eyeRage = Circle(Point(winLength/2 + 30, winWidth-350), 20)
          eyeRage.setFill("white")
          eyeRage.setWidth(total)
          eyeRage.setOutline("white")
          eyeRage.draw(win)
          pupil1 = Circle(Point(winLength/2 + 30, winWidth-350), 7)
          pupil1.setFill("red3")
          pupil1.setWidth(1)
          pupil1.setOutline("red")
          pupil1.draw(win)
          pupil2 = Circle(Point(winLength/2 - 30, winWidth-350), 7)
          pupil2.setFill("red3")
          pupil2.setWidth(1)
          pupil2.setOutline("red")
          pupil2.draw(win)
          total = total + 10
          for color in colors:
               win.setBackground(color)
               time.sleep(.1)
     rightEyebrow.draw(win)
     leftEyebrow.draw(win)
     head.setFill("green3")
     leftFoot.setFill("green3")
     rightFoot.setFill("green3")
     rightFoot.setOutline("green3")
     leftFoot.setOutline("green3")
     win.setBackground("brown")
     words.setText("run... click to exit.")
     textPt = win.getMouse()
     win.close()



     
main()
