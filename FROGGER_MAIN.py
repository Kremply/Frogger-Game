from tkinter import *
from math import *
from time import *
from random import*


width_main = 830
height_main = 950
root = Tk()
root.title("Frogger")
s = Canvas(root, width= width_main ,height= height_main, background="white")
s.pack()


####Import Images####
def imports():
    global frogUp1, frogUp2, frogDown1, frogDown2, frogLeft1, frogLeft2, frogRight1, frogRight2, frogUp, frogDown, frogLeft, frogRight, lives, death
    global carRight, carRight2, truck, carLeft, carLeft2
    global Log1, Log2, Log3, turtle1, turtle2,turtle3
    
    #Frog
    frogUp1 = PhotoImage(file="FrogUp1.gif")
    frogUp2 = PhotoImage(file="FrogUp2.gif")
    frogDown1 = PhotoImage(file="FrogDown1.gif")
    frogDown2 = PhotoImage(file="FrogDown2.gif")
    frogLeft1 = PhotoImage(file="FrogLeft1.gif")
    frogLeft2 = PhotoImage(file="FrogLeft2.gif")
    frogRight1 = PhotoImage(file="FrogRight1.gif")
    frogRight2 = PhotoImage(file="FrogRight2.gif")

    lives = PhotoImage(file="lives.gif")
    death = PhotoImage(file="death.gif")


    #Moving pieces
    carRight= PhotoImage(file="carRight.gif")
    carLeft=PhotoImage(file="car2Left.gif")
    carLeft2= PhotoImage(file="carLeft.gif")
    truck= PhotoImage(file="truckRight.gif")
    carRight2 = PhotoImage(file="carRight2.gif")
    Log1 = PhotoImage(file="Log.gif")
    Log2 = PhotoImage(file="Log2.gif")
    Log3 = PhotoImage(file="Log3.gif")
    turtle1 = PhotoImage(file = "turtle.gif")
    turtle2 = PhotoImage(file="Turtle2.gif")
    turtle3 = PhotoImage(file="Turtle3.gif")

####Create Background####    
def drawBackground():
    #road
    s.create_rectangle(0,0,width_main,height_main, fill = "black")
    #water
    s.create_rectangle(0,0,width_main,(height_main/2)+10, fill = "midnightblue")
    #scoreboard
    s.create_rectangle(0,height_main-75,width_main,height_main, fill = "grey")
    #Grass
    s.create_rectangle(0,height_main-145,width_main,height_main-75, fill = "purple")
    s.create_rectangle(0,height_main-528,width_main,height_main-458, fill = "purple")

    #GoalBorder
    s.create_rectangle(0,0,width_main,40,fill="green", outline="green")
    s.create_rectangle(0,0,144.5,100,fill="green", outline="green")
    s.create_rectangle(228.5,0,373,100,fill="green", outline="green")
    s.create_rectangle(457,0,601.5,100,fill="green", outline="green")
    s.create_rectangle(685.5,0,width_main,100,fill="green", outline="green")

####Set Initial game Values####
def setInitialValues():
    global xfrog, yfrog, xSpeed, ySpeed
    global jumpingFrog, jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight, frogUp, frogDown, frogLeft, frogRight
    global frogAtTopEdge, frogAtBottomEdge, frogAtLeftEdge, frogAtRightEdge
    global timeTotal, timeStart, timeBar
    global xCar1, xCar1b, xCar1c, xCar2, xCar2b, xCar2c, xCar2d, xCar3, xCar3b, xCar4, xCar4b, xCar5, xCar5b, rightCars, LeftCars
    global xLog1, xLog2, xLog3, xLog4, xLog5, xLog6, xLog7, log1Speed, log2Speed, log3Speed, onPlatform
    global xTurtle1, xTurtle2, xTurtle3, xTurtle4, xTurtle5, turtle1Speed, turtle2Speed
    global winner, score, beenHere, currentLives, dead, goal1, goal2, goal3
    global escapePressed, keyDown
    
    #Frog Values
    jumpingFrogUp = 0
    jumpingFrogDown = 0
    jumpingFrogLeft = 0
    jumpingFrogRight = 0
    xfrog = width_main/2
    yfrog = height_main-110
    xSpeed = 64
    ySpeed = 64
    frogAtTopEdge = False
    frogAtBottomEdge = False
    frogAtLeftEdge = False
    frogAtRightEdge = False

    jumpingFrog = s.create_image(xfrog,yfrog,image=frogUp1)
    frogUp = [frogUp1,frogUp2]
    frogDown = [frogDown1,frogDown2]
    frogLeft = [frogLeft1,frogLeft2]
    frogRight = [frogRight1,frogRight2]
    
    #System
    keyDown = False
    escapePressed = False
    
    #Timer Values
    timeTotal = 180
    timeStart = time()
    timeBar = 610
    
    #Car Values
    xCar1 = 0
    xCar1b = -300
    xCar1c = -600   
    xCar2 = 0
    xCar2b = -232
    xCar2c = -452
    xCar2d = -672 
    xCar3 = -100
    xCar3b = -550   
    xCar4 = width_main
    xCar4b = width_main+450   
    xCar5 = width_main+50
    xCar5b = width_main+500
    #Log values
    onPlatform = False
    xLog1 = -100
    xLog2 = -350
    xLog3 = -800
    xLog4 = 0
    xLog5 = -700
    xLog6 = width_main+100
    xLog7 = width_main+500
    xTurtle1 = width_main+100
    xTurtle2 = width_main+600
    xTurtle3 = width_main+100
    xTurtle4 = width_main+400
    xTurtle5 = width_main+800
    log1Speed = 11
    log2Speed = 6
    log3Speed = 10
    turtle1Speed = 5
    turtle2Speed = 9

    #GAME VALUES#
    winner = 0
    score = 0
    beenHere = []
    currentLives = 3
    dead = False
    goal1 = True
    goal2 = True
    goal3 = True
    
####Create Game Displays####
##Timer##
def timeDisplay():
    global barDisplay,backBar,timeTag
    backBar = s.create_rectangle(110,height_main-25,610,height_main-45, fill = "black")
    timeTag = s.create_text(55,height_main-33,text="TIME", anchor=CENTER, fill = "yellow",font="Times 30")
    barDisplay = s.create_rectangle(110,height_main-25,timeBar,height_main-45, fill = "green")
##Score and Lives##
def currentScoreAndLives():
    global scoreText, scoreDisplay, lifeVisual, lifeDisplay
    #Score Text
    scoreText = s.create_text(55,20,text="SCORE:", anchor=CENTER, fill = "white",font="Times 20")
    #Score Display
    scoreDisplay = s.create_text(150,20,text=score, anchor=CENTER, fill = "white",font="Times 20")
    #Life Frog
    lifeVisual = s.create_image(width_main-90,height_main-50, image = lives)
    #Life Number Indicator
    lifeDisplay = s.create_text(width_main-50,height_main-50,text="x "+str(currentLives), anchor=CENTER, fill = "white",font="Times 20")
    
####Check if the Frog is in the Goal####
def goalReached():
    global xfrog, yfrog, score, jumpingFrogUp, goal1, goal1Reached, beenHere, winner
    if xfrog >=144.5 and xfrog <=228.5 and yfrog <136:
        s.delete(jumpingFrogUp)
        s.create_image(186.5,yfrog, image=frogUp[0])
        goal1 = False
        xfrog = width_main/2
        yfrog = height_main-110
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[0])
        score += 500
        winner += 1
        beenHere = []
    elif xfrog >=373 and xfrog <=457 and yfrog <136:
        s.delete(jumpingFrogUp)
        s.create_image(415,yfrog, image=frogUp[0])
        goal2 = False
        xfrog = width_main/2
        yfrog = height_main-110
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[0])
        score += 500
        winner += 1
        beenHere = []
    elif xfrog >=601.5 and xfrog <=685.5 and yfrog <136:
        s.delete(jumpingFrogUp)
        s.create_image(643.5,yfrog, image=frogUp[0])
        goal3 = False
        xfrog = width_main/2
        yfrog = height_main-110
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[0])
        score += 500
        winner +=1
        beenHere = []
        
####Draw Cars and Update Car positions####
def createCars():
    global carImage1, carImage1b, carImage1c, carImage2, carImage2b, carImage2c, carImage2d, carImage2, carImage3, carImage3b, carImage4, carImage4b, carImage5, carImage5b, xCar1, xCar1b, xCar1c, xCar2, xCar2b, xCar2c, xCar2d, xCar3, xCar3b, xCar4, xCar4b, xCar5, xCar5b       
###Lane2###
    #Car1
    if xCar1 >= width_main+50:
        xCar1 = -50
    else:
        carImage1 = s.create_image(xCar1,584,image=carRight)
        xCar1+=20
    #Car2
    if xCar1b >= width_main+50:
        xCar1b = -50
    else:
        carImage1b = s.create_image(xCar1b,584,image=carRight)
        xCar1b+=20
    #Car3
    if xCar1c >= width_main+50:
        xCar1c = -50
    else:
        carImage1c = s.create_image(xCar1c,584,image=carRight)
        xCar1c+=20
        
###Lane4###
    #Car1
    if xCar2 >= width_main+50:
        xCar2 = 0
    else:
        carImage2 = s.create_image(xCar2,648, image=carRight2)
        xCar2+=10
    #Car2
    if xCar2b >= width_main+50:
        xCar2b = 0
    else:
        carImage2b = s.create_image(xCar2b,648, image=carRight2)
        xCar2b+=10
    #Car3
    if xCar2c >= width_main+50:
        xCar2c = 0
    else:
        carImage2c = s.create_image(xCar2c,648, image=carRight2)
        xCar2c+=10
    #Car4
    if xCar2d >= width_main+50:
        xCar2d = 0
    else:
        carImage2d = s.create_image(xCar2d,648, image=carRight2)
        xCar2d+=10
        
###Lane1###
    #Car1
    if xCar3 >= width_main+100:
        xCar3 = -100
    else:
        carImage3 = s.create_image(xCar3,525,image=truck)
        xCar3+=10
    #Car2
    if xCar3b >= width_main+100:
        xCar3b = -100
    else:
        carImage3b = s.create_image(xCar3b,525,image=truck)
        xCar3b+=10

###Lane3###
    #Car1
    if xCar4 <= -50:
        xCar4 = width_main+50
    else:
        carImage4 = s.create_image(xCar4,648,image=carLeft)
        xCar4-=30
    #Car2
    if xCar4b <= -50:
        xCar4b = width_main+50
    else:
        carImage4b = s.create_image(xCar4b,648,image=carLeft)
        xCar4b-=30

###Lane5###
    #Car1
    if xCar5 <= -50:
        xCar5 = width_main
    else:
        carImage5 = s.create_image(xCar5,767,image=carLeft2)
        xCar5-=8
    #Car2
    if xCar5b <= -50:
        xCar5b = width_main
    else:
        carImage5b = s.create_image(xCar5b,767,image=carLeft2)
        xCar5b-=8
        
####Check if Frog has Been hit by a Car####
def collisionIndicator():
    global dead
    ##Lane5
    if yfrog == 776 and xfrog < (xCar5)+60 and xfrog > (xCar5)-50:
      dead = True
    if yfrog == 776 and xfrog < (xCar5b)+60 and xfrog > (xCar5b)-50:
        dead = True
    #Lane4
    if yfrog == 712 and xfrog < (xCar2)+50 and xfrog > (xCar2)-50:
        dead = True
    if yfrog == 712 and xfrog < (xCar2b)+50 and xfrog > (xCar2b)-50:
        dead = True
    if yfrog == 712 and xfrog < (xCar2c)+50 and xfrog > (xCar2c)-50:
        dead = True
    if yfrog == 712 and xfrog < (xCar2d)+50 and xfrog > (xCar2d)-50:
        dead = True
    #Lane3
    if yfrog == 648 and xfrog < (xCar4)+60 and xfrog > (xCar4)-40:
        dead = True
    if yfrog == 648 and xfrog < (xCar4b)+60 and xfrog > (xCar4b)-40:
        dead = True
    #Lane2
    if yfrog == 584 and xfrog < (xCar1)+45 and xfrog > (xCar1)-50:
        dead = True
    if yfrog == 584 and xfrog < (xCar1b)+45 and xfrog > (xCar1b)-50:
        dead = True
    if yfrog == 584 and xfrog < (xCar1c)+45 and xfrog > (xCar1c)-50:
        dead = True
    #Lane1
    if yfrog == 520 and xfrog < (xCar3)+65 and xfrog > (xCar3)-80:
        dead = True
    if yfrog == 520 and xfrog < (xCar3b)+65 and xfrog > (xCar3b)-80:
        dead = True

####Create Logs and Turltes####
def createPlatforms():
    global log1, xLog1, log2, xLog2, log3, xLog3, log4, xLog4, log5, xLog5, log6, xLog6, log7, xLog7, turtlea, turtleb, turtlec, turtled, turtlee, xTurtle1, xTurtle2, xTurtle3, xTurtle4, xTurtle5
###LOGS###
##Row2##
    #Log1
    log1=s.create_image(xLog1,325,image = Log1)
    xLog1+=log1Speed
    if xLog1 >= width_main+100:
        xLog1 = -100
    #Log2
    log2=s.create_image(xLog2,325,image = Log1)
    xLog2+=log1Speed
    if xLog2 >= width_main+100:
        xLog2 = -100
    #Log3
    log3=s.create_image(xLog3,325,image = Log1)
    xLog3+=log1Speed
    if xLog3 >= width_main+100:
        xLog3 = -100
##Row3##
    #Log1
    log4=s.create_image(xLog4,268,image = Log2)
    xLog4+=log2Speed
    if xLog4 >= width_main+300:
        xLog4 = -400
    #Log2

    log5=s.create_image(xLog5,268,image = Log2)
    xLog5+=log2Speed
    if xLog5 >= width_main+300:
        xLog5 = -400

##Row5##
    #Log1
    log6=s.create_image(xLog6,130,image = Log3)
    xLog6-=log3Speed
    if xLog6 <= -100:
        xLog6 = width_main+300
    #Log2
    log7=s.create_image(xLog7,130,image = Log3)
    xLog7-=log3Speed
    if xLog7 <= -100:
        xLog7 = width_main+300
###TURTLES###
##Row1##
    #Turtle1
    turtlea=s.create_image(xTurtle1,200,image=turtle1)
    xTurtle1 -= turtle1Speed
    if xTurtle1<=-100:
        xTurtle1 = width_main+100
    #Turtle2
    turtleb=s.create_image(xTurtle2,200,image=turtle1)
    xTurtle2 -= turtle1Speed
    if xTurtle2<=-100:
        xTurtle2 = width_main+100
##Row5##
    #Turtle3
    turtlec=s.create_image(xTurtle3,392,image=turtle2)
    xTurtle3 -= turtle2Speed
    if xTurtle3<=-100:
        xTurtle3 = width_main+100
    #Turtle4
    turtled=s.create_image(xTurtle4,392,image=turtle2)
    xTurtle4 -= turtle2Speed
    if xTurtle4<=-100:
        xTurtle4 = width_main+100
    #Turtle4
    turtlee=s.create_image(xTurtle5,392,image=turtle3)
    xTurtle5 -= turtle2Speed
    if xTurtle5<=-100:
        xTurtle5 = width_main+100

####On Platform####        
def platformCheck():
    global onPlatform
    ##Frog on Log##    
    if yfrog == 328 and xfrog < (xLog1)+65 and xfrog > (xLog1)-87:
        onPlatform = True
    elif yfrog == 328 and xfrog < (xLog2)+65 and xfrog > (xLog2)-87:
        onPlatform = True
    elif yfrog == 328 and xfrog < (xLog3)+65 and xfrog > (xLog3)-87:
        onPlatform = True
    elif yfrog == 264 and xfrog < (xLog4)+150 and xfrog > (xLog4)-264:
        onPlatform = True
    elif yfrog == 264 and xfrog < (xLog5)+150 and xfrog > (xLog5)-264:
        onPlatform = True
    elif yfrog == 136 and xfrog < (xLog6)+30 and xfrog > (xLog6)-250:
        onPlatform = True
    elif yfrog == 136 and xfrog < (xLog7)+30 and xfrog > (xLog7)-250:
        onPlatform = True
    ##Frog on Turtle
    elif yfrog == 200 and xfrog < (xTurtle1)+90 and xfrog > (xTurtle1)-70:
        onPlatform = True
    elif yfrog == 200 and xfrog < (xTurtle2)+90 and xfrog > (xTurtle2)-70:
        onPlatform = True
    elif yfrog == 392 and xfrog < (xTurtle3)+30 and xfrog > (xTurtle3)-75:
        onPlatform = True
    elif yfrog == 392 and xfrog < (xTurtle4)+30 and xfrog > (xTurtle4)-75:
        onPlatform = True
    elif yfrog == 392 and xfrog < (xTurtle5)-23 and xfrog > (xTurtle5)-75:
        onPlatform = True
    ##Not on Platform##  
    else:
        onPlatform = False

####Meets Edge####
##Edge Collision##
def meetsTopEdge():
    global frogAtTopEdge
    ##Check if the Frog is in the goal##
    if ((yfrog-32) - ySpeed) <= 50 and xfrog >=144.5 and xfrog <=228.5 and goal1 == True:
        frogAtTopEdge = False
    elif ((yfrog-32) - ySpeed) <= 50 and xfrog >=373 and xfrog <=457 and goal2 == True:
        frogAtTopEdge = False
    elif ((yfrog-32) - ySpeed) <= 50 and xfrog >=601.5 and xfrog <=685.5 and goal3 == True:
        frogAtTopEdge = False
    elif ((yfrog-32) - ySpeed) <= 100:
        frogAtTopEdge = True
    else:
        frogAtTopEdge = False
##Edge Collision##       
def meetsBottomEdge():
    global frogAtBottomEdge
    if ((yfrog+100) + ySpeed) >= height_main:
        frogAtBottomEdge = True
    else:
        frogAtBottomEdge = False
##Edge Collision##
def meetsLeftEdge ():
    global frogAtLeftEdge
    if ((xfrog-25) - xSpeed) <= 0 and yfrog > 392:
        frogAtLeftEdge = True
    else:
        frogAtLeftEdge = False
##Edge Collision##        
def meetsRightEdge ():
    global frogAtRightEdge
    if ((xfrog+25) + xSpeed) >= width_main and yfrog > 392:
        frogAtRightEdge = True
    else:
        frogAtRightEdge = False
        
####Animating the Frog's Movements####
def drawFrogUp():
    global jumpingFrogUp, yfrog
    ##Redraw at New Position##
    if frogAtTopEdge == False:
        s.delete(jumpingFrog,jumpingFrogUp,jumpingFrogDown,jumpingFrogLeft,jumpingFrogRight)
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogUp)
        yfrog -=ySpeed
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[0])
    ##Redraw at Old Position##    
    else:
        s.delete(jumpingFrog,jumpingFrogUp,jumpingFrogDown,jumpingFrogLeft,jumpingFrogRight)
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogUp)
        jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[0])
    
def drawFrogDown():
    global jumpingFrogDown, yfrog, frogAtBottomEdge
    ##Redraw at New Position##
    if frogAtBottomEdge == False:
        s.delete(jumpingFrog,jumpingFrogDown,jumpingFrogUp,jumpingFrogLeft,jumpingFrogRight)
        jumpingFrogDown=s.create_image(xfrog,yfrog,image=frogDown[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogDown)
        yfrog +=ySpeed
        jumpingFrogDown=s.create_image(xfrog,yfrog,image=frogDown[0])
    ##Redraw at Old Position##
    else:
        s.delete(jumpingFrog,jumpingFrogDown,jumpingFrogUp,jumpingFrogLeft,jumpingFrogRight)
        jumpingFrogDown=s.create_image(xfrog,yfrog,image=frogDown[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogDown)
        jumpingFrogDown=s.create_image(xfrog,yfrog,image=frogDown[0])

        
def drawFrogLeft():
    global jumpingFrogLeft, xfrog, frogAtLeftEdge
    ##Redraw at New Position##
    if frogAtLeftEdge == False:
        s.delete(jumpingFrog,jumpingFrogLeft,jumpingFrogUp,jumpingFrogDown,jumpingFrogRight)
        jumpingFrogLeft=s.create_image(xfrog,yfrog,image=frogLeft[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogLeft)
        xfrog -=xSpeed
        jumpingFrogLeft=s.create_image(xfrog,yfrog,image=frogLeft[0])
    ##Redraw at Old Position##
    else:
        s.delete(jumpingFrog,jumpingFrogLeft,jumpingFrogUp,jumpingFrogDown,jumpingFrogRight)
        jumpingFrogLeft=s.create_image(xfrog,yfrog,image=frogLeft[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogLeft)
        jumpingFrogLeft=s.create_image(xfrog,yfrog,image=frogLeft[0])

def drawFrogRight():
    global jumpingFrogRight, xfrog, frogAtRightEdge
    ##Redraw at New Position##
    if frogAtRightEdge == False:
        s.delete(jumpingFrog,jumpingFrogRight,jumpingFrogUp,jumpingFrogDown,jumpingFrogLeft)
        jumpingFrogRight=s.create_image(xfrog,yfrog,image=frogRight[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogRight)
        xfrog +=xSpeed
        jumpingFrogRight=s.create_image(xfrog,yfrog,image=frogRight[0])
    ##Redraw at Old Position##
    else:
        s.delete(jumpingFrog,jumpingFrogRight,jumpingFrogUp,jumpingFrogDown,jumpingFrogLeft)
        jumpingFrogRight=s.create_image(xfrog,yfrog,image=frogRight[1])
        s.update()
        sleep(0.05)
        s.delete(jumpingFrogRight)
        jumpingFrogRight=s.create_image(xfrog,yfrog,image=frogRight[0])   
    
####Key Bindings####
    ##If the Mouse is Clicked##  
def mouseDownHandler(event):
    global click, inGame, inWinnerScreen
    click = True
    if event.x > width_main/2-150 and event.x < width_main/2+150 and event.y > 750 and event.y < 900 and inGame == False and click == True:
        click = False
        inGame = True
        createCountdown()
    ##If you've lost the game or Quit##
    elif event.x > 215 and event.x < 615 and event.y > 500 and event.y < 650 and inReplay == True:
        createCountdown()
    elif event.x > 215 and event.x < 615 and event.y > 700 and event.y < 850 and inReplay == True:
        end()
    ##If you've won the Game##
    elif event.x > 215 and event.x < 615 and event.y > 500 and event.y < 650 and inWinnerScreen == False:
        createCountdown()
    elif event.x > 215 and event.x < 615 and event.y > 700 and event.y < 850 and inWinnerScreen == True:
        end()

#Movement#
def keyDownHandler(event):
    global keyDown, keyPressed
    global xfrog,yfrog,escapePressed

    if event.keysym == "Up":
        if keyDown == False:
            drawFrogUp()
        keyDown = True
        keyPressed = "Up"
    elif event.keysym == "Down":
        if keyDown == False:
            drawFrogDown()
        keyDown = True
        keyPressed = "Down"        
    elif event.keysym == "Left":
        if keyDown == False:
            drawFrogLeft()
        keyDown = True
        keyPressed = "Left"        
    elif event.keysym == "Right":
        if keyDown == False:
            drawFrogRight()
        keyDown = True
        keyPressed = "Right"        
    elif event.keysym == "Escape":
        escapePressed = True
        
##Make Sure Key is not Being Held Down##
def keyUpHandler(event):
    global keyDown
    if event.keysym == "Up":
        keyDown = False
    elif event.keysym == "Down":
        keyDown = False
    elif event.keysym == "Left":
        keyDown = False
    elif event.keysym == "Right":
        keyDown = False
        
##Countdown Before Game Start##
def createCountdown():
    s.delete(BG1, BG2, line1, line2,  line3, line4, line5, line6, line7, line8, line9, line10)
    countDown3 = s.create_rectangle(0,0,width_main,height_main, fill = "Black")
    countDown3a = s.create_text(width_main/2,height_main/2,text="3", anchor=CENTER, fill = "white",font="tinytype 100 bold")
    s.update()
    sleep(1)
    s.delete(countDown3,countDown3a)
    countDown2 = s.create_rectangle(0,0,width_main,height_main, fill = "Black")
    countDown2a = s.create_text(width_main/2,height_main/2,text="2", anchor=CENTER, fill = "white",font="tinytype 100 bold")
    s.update()
    sleep(1)
    s.delete(countDown2,countDown2a)
    countDown1 = s.create_rectangle(0,0,width_main,height_main, fill = "Black")
    countDown1a = s.create_text(width_main/2,height_main/2,text="1", anchor=CENTER, fill = "white",font="tinytype 100 bold")
    s.update()
    sleep(1)
    s.delete(countDown1,countDown1a)
    drawBackground()
    imports()
    setInitialValues()
    runGame()
    

##Set Start Values before Initial Game Values Are Set##
def startMenuValues():
    global click, inGame, inReplay, inWinnerScreen
    click = False
    inGame = False
    inReplay = False
    inWinnerScreen = False
    startMenu()

####Opening Screen####
def startMenu():
    global  inGame, BG1, BG2, line1, line2,  line3, line4, line5, line6, line7, line8, line9, line10
    BG1=s.create_rectangle(0,0,width_main,425,fill = "midnightblue")
    BG2=s.create_rectangle(0,425,width_main,height_main,fill = "black")
    line1=s.create_text(width_main/2,215,text="FROGGER", anchor=CENTER, fill = "Green",font="tinytype 100 bold")
    line2=s.create_text(25,320,text="MOVE FROG VERTICALLY OR HORIZONTALLY", fill = "white", anchor = "w", font="tinytype 25 bold")
    line3=s.create_text(25,350,text="BY USING THE ARROW KEYS", fill = "white", anchor= "w", font="tinytype 25 bold")
    line4=s.create_text(25,380,text="PRESS ESCAPE TO EXIT WHILE IN GAME", fill = "white", anchor= "w", font="tinytype 25 bold")

    line5=s.create_text(25,470,text="OBJECT IS TO SAFELY MANEUVER 3 FROGS", fill = "red", anchor= "w", font="tinytype 25 bold")
    line6=s.create_text(25,500,text="TO THEIR HOMES WITHIN ALLOTTED TIME", fill = "red", anchor= "w", font="tinytype 25 bold")
    line7=s.create_text(width_main/2,550,text="--180 TICKS ON THE TIMER--", fill = "red", anchor= CENTER, font="tinytype 35 bold")

    line8=s.create_text(25,640,text="CROSS HIGHWAY WITHOUT GETTING RUN OVER", fill = "cyan", anchor= "w", font="tinytype 25 bold")
    line9=s.create_text(25,670,text="AND", fill = "cyan", anchor= "w", font="tinytype 25 bold")
    line10=s.create_text(25,700,text="CROSS RIVER WITHOUT FALLING IN", fill = "cyan", anchor= "w", font="tinytype 25 bold")

    button1=s.create_rectangle(width_main/2-150,750,width_main/2+150,900,fill = "yellow")
    button2=s.create_text(415,825,text="PLAY", fill = "BLACK", anchor= CENTER, font="tinytype 50 bold")

####End Game####
#Game Quit#
def end():
    s.create_rectangle(0,0,width_main,height_main, fill="black")
    s.update()
    sleep(1)
    s.create_text(width_main/2,height_main/2,text="THANK YOU FOR PLAYING FROGGER", anchor=CENTER, fill = "green",font="tinytype 30 bold")
    s.create_text(width_main/2,height_main/2+100,text="SEE YOU NEXT TIME", anchor=CENTER, fill = "green",font="tinytype 30 bold")
    s.update()
    sleep(2)
    root.destroy()
##If The Player Loses or Quits the Game, Ask if They Want to Play Again##
def replay():
    global inReplay
    inReplay = True
    s.delete(carImage1,carImage1b,carImage1c,carImage2,carImage2b,carImage2c,carImage2d,carImage3,carImage3b,carImage4,carImage4b,carImage5,carImage5b,log1,log2,log3,log4,log5,log6,log7,turtlea,turtleb,turtlec,turtled,turtlee,barDisplay,backBar,timeTag,scoreText,scoreDisplay, lifeVisual, lifeDisplay)
    s.create_rectangle(0,0,width_main,height_main,fill = "black")
    s.create_text(width_main/2,300,text="GAMEOVER", fill = "green", anchor= CENTER, font="tinytype 60 bold")
    s.create_text(width_main/2,375,text="FINAL SCORE: " + str(score) , fill = "white", anchor= CENTER, font="tinytype 45 bold")
    s.create_rectangle(width_main/2-200,500,width_main/2+200,650,fill = "cyan")
    s.create_text(width_main/2,575,text="PLAY AGAIN", fill = "blue", anchor= CENTER, font="tinytype 35 bold")
    s.create_rectangle(width_main/2-200,700,width_main/2+200,850,fill = "yellow")
    s.create_text(width_main/2,775,text="QUIT", fill = "black", anchor= CENTER, font="tinytype 35 bold")

##If the Player gets all 3 Frogs to their Homes##
def winnerScreen():
    global inWinnerScreen, score
    inWinnerScreen = True
    score+=(200*currentLives) + (3*timeTotal)
    newScore = int(round(score))
    s.delete(carImage1,carImage1b,carImage1c,carImage2,carImage2b,carImage2c,carImage2d,carImage3,carImage3b,carImage4,carImage4b,carImage5,carImage5b,log1,log2,log3,log4,log5,log6,log7,turtlea,turtleb,turtlec,turtled,turtlee,barDisplay,backBar,timeTag,scoreText,scoreDisplay, lifeVisual, lifeDisplay)
    s.create_rectangle(0,0,width_main,height_main, fill = "green")
    s.create_text(width_main/2,150,text="CONGRATULATIONS!", fill = "cyan", anchor= CENTER, font="tinytype 55 bold")
    s.create_text(width_main/2,300,text="YOU HAVE COMPLETED FROGGER", fill = "yellow", anchor= CENTER, font="tinytype 30 bold")
    s.create_text(width_main/2,350,text="WITH A FINAL SCORE OF: "+ str(newScore), fill = "yellow", anchor= CENTER, font="tinytype 30 bold")

    s.create_rectangle(width_main/2-200,500,width_main/2+200,650,fill = "cyan")
    s.create_text(width_main/2,575,text="PLAY AGAIN", fill = "blue", anchor= CENTER, font="tinytype 35 bold")
    s.create_rectangle(width_main/2-200,700,width_main/2+200,850,fill = "yellow")
    s.create_text(width_main/2,775,text="QUIT", fill = "black", anchor= CENTER, font="tinytype 35 bold")
    
####Game Run####       
def runGame():
    global timeTotal, timeStart, timeBar, dead, xfrog, yfrog,jumpingFrogUp, currentLives, jumpingFrogUp,jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight, score, beenHere
    ##Main Game Loop##
    while escapePressed == False and currentLives > 0 and timeTotal > 0 and winner != 3:
        platformCheck()
        goalReached()
        ##Only Adds Score if Frog has not been in This xPosition this Current Run##
        if yfrog not in (beenHere) and yfrog!=840:
            beenHere.append(yfrog)
            score+=100
        ##Frog in Water##
        if yfrog < 456 and onPlatform == False :
            dead = True
        ##Frog Washed off Right Edge##
        if yfrog <= 392 and xfrog-32 >= width_main:
            dead = True
        ##Frog Washed off Left Edge##
        elif yfrog <= 392 and xfrog+32 <= 0:
            dead = True
        ##Creates Ghost Images where Dead##
        if dead == True:
            s.create_image(xfrog,yfrog,image=death)
            s.delete(jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight)
            xfrog = width_main/2
            yfrog = height_main-110
            jumpingFrogUp=s.create_image(xfrog,yfrog,image=frogUp[0])
            currentLives -= 1
            score-=200
            beenHere=[]
            dead = False
        else:
            ##Moving the Frog with the Platform##
            if onPlatform == True and yfrog==328:
                s.delete(jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight)
                xfrog += log1Speed
                createPlatforms()
                ##Determine Which Image to Create##
                if keyPressed == "Up":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogUp[0])
                if keyPressed == "Down":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogDown[0])
                if keyPressed == "Left":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogLeft[0])
                if keyPressed == "Right":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogRight[0])
                    
            ##Moving the Frog with the Platform##
            elif onPlatform == True and yfrog==264:
                s.delete(jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight)
                xfrog += log2Speed
                createPlatforms()
                ##Determine Which Image to Create##
                if keyPressed == "Up":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogUp[0])
                if keyPressed == "Down":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogDown[0])
                if keyPressed == "Left":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogLeft[0])
                if keyPressed == "Right":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogRight[0])
                    
            ##Moving the Frog with the Platform##
            elif onPlatform == True and yfrog==136:
                s.delete(jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight)
                xfrog -= log3Speed
                createPlatforms()
                ##Determine Which Image to Create##
                if keyPressed == "Up":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogUp[0])
                if keyPressed == "Down":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogDown[0])
                if keyPressed == "Left":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogLeft[0])
                if keyPressed == "Right":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogRight[0])
                    
            ##Moving the Frog with the Platform##        
            elif onPlatform == True and yfrog==200:
                s.delete(jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight)
                xfrog -= turtle1Speed
                createPlatforms()
                ##Determine Which Image to Create##
                if keyPressed == "Up":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogUp[0])
                if keyPressed == "Down":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogDown[0])
                if keyPressed == "Left":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogLeft[0])
                if keyPressed == "Right":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogRight[0])
                    
            ##Moving the Frog with the Platform##     
            elif onPlatform == True and yfrog==392:
                s.delete(jumpingFrogUp, jumpingFrogDown, jumpingFrogLeft, jumpingFrogRight)
                xfrog -= turtle2Speed
                createPlatforms()
                ##Determine Which Image to Create##
                if keyPressed == "Up":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogUp[0])
                if keyPressed == "Down":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogDown[0])
                if keyPressed == "Left":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogLeft[0])
                if keyPressed == "Right":
                    jumpingFrogUp = s.create_image(xfrog,yfrog, image = frogRight[0])
            else:
                createPlatforms()
            ##Check and Create values each run Through the Loop##
            currentScoreAndLives()    
            createCars()
            collisionIndicator()
            meetsTopEdge()
            meetsBottomEdge()
            meetsLeftEdge()
            meetsRightEdge()
            timeDisplay()
            s.update()
            sleep(0.075)
            s.delete(carImage1,carImage1b,carImage1c,carImage2,carImage2b,carImage2c,carImage2d,carImage3,carImage3b,carImage4,carImage4b,carImage5,carImage5b,log1,log2,log3,log4,log5,log6,log7,turtlea,turtleb,turtlec,turtled,turtlee,barDisplay,backBar,timeTag,scoreText,scoreDisplay, lifeVisual, lifeDisplay)
            timeNow = time()
            timeChecking = timeNow - timeStart
            ####Time Countdown####
            if timeChecking >= 0.1:
                
                timeTotal -= 0.1
                timeBar -= 0.27777
                timeStart = time()
    ##If Game is lost or quit##
    if winner != 3:
        replay()
    ##If 3 Frogs Reach the Goal##
    else:
        winnerScreen()

root.after(0,startMenuValues)    

####Key Bindings####
s.bind("<Key>", keyDownHandler)
s.bind("<KeyRelease>", keyUpHandler)
s.bind("<Button-1>", mouseDownHandler)


s.pack()
s.focus_set()
root.mainloop()

