from graphics import *

#COURSEWORK MAIN FUCNTION TO CREATE THE 5X5 MATRIX 
def start():
    index = 0
    tile = 0
    colour = ""
    colourList = ["red", "green", "blue", "magenta", "orange", "pink"]
    #THIS TABLE CONTAINS A LIST OF TILE TYPES IN THEIR POSTITIONS ON A 5X5 MATRIX.
    tiletype = [
        1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1,
        2
    ]
    #THIS TABLE CONTAINS A LIST OF TILE COLOURS ON A 5X5 MATRIX.
    tilecolour = [
        1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 3, 2, 1, 2, 3, 3, 2, 2, 2, 2, 2,
        2
    ]
    #THIS IS THE WHILE LOOPS THAT WILL REJECT NON ALLOWED COULOURS TO BE INPUTED BY THE USER .
    colour1 = (input("1st colour:"))
    while colour1 not in colourList:
        colour1 = (input("invalid colour entered, please try again"))

    colour2 = (input("2nd colour:"))
    while colour2 not in colourList:
        colour2 = (input("invalid colour entered, please try again"))

    colour3 = (input("3rd colour:"))
    while colour3 not in colourList:
        colour3 = (input("invalid colour entered, please try again"))
    #THIS IS WHERE THE GRAPHIC WINDOW STARTS.
    win = GraphWin("new window", 500, 500)

    for Yaxis in range(5):

        for Xaxis in range(5):
            index = Yaxis * 5 + Xaxis
            tile = tiletype[index]
            #THIS WILL COLOUR THE TILES ACCORDING TO THE INPUT BUT ALSO THE LIST FROM TILECOULOUR.
            if tilecolour[index] == 1:
                colour = colour1
            if tilecolour[index] == 2:
                colour = colour2
            if tilecolour[index] == 3:
                colour = colour3
            #THIS CODE PLOTS EITHER TILE 1 OR 2 ON THE 5X5 MATRIX DEPENDING ON THE TITLETYPE LIST.
            if tile == 1:
                patch12(win, Xaxis * 100, Yaxis * 100, colour)
            else:
                patch7(win, Xaxis * 100, Yaxis * 100, colour)

    

#FINAL DIGIT OF STUDENT NUMBER PATCH
def patch7(win, Xval, Yval, colour):
    radius = 5
    height = 95
    #THIS RECTANGLE CREATES THE PATCH BORDER.
    rec = Rectangle(Point(Xval+0, Yval+0), Point(Xval+100, Yval+100))
    rec.setOutline('Black')
    rec.draw(win)
    #RANGE STATEMENT TO CREATE THE CIRCLES FOR THE PATCH 
    for i in range(0, 10):
        cir = Circle(Point(Xval + 50, Yval + height), radius)
        cir.setOutline(colour)
        cir.draw(win)
        radius = radius + 5
        height = height - 5
        
#PENULTIMATE DIGIT PATCH
def patch12(win, Xaxis, Yaxis, colour): 
    type = 1
    for j in range(0,5):
         
        for i in range(0,5):
            if j %2 == 0:
                if i%2 == 0:
                    type = 1
                else: 
                    type = 2
                    
            else: 
                if i%2 == 0:
                    type = 4
                else: 
                    type = 3
            patch0(win, Xaxis+(i*20), Yaxis+(j*20), type, colour)

#PENULTIMATE DIGIT PATCH BASE
def patch0(win, Xval, Yval, type, colour):
    #A BORDER AROUND EACH 20X20 SQUARE IN THE PATCH
    rec = Rectangle(
        Point(Xval + 0, Yval + 0), Point(Xval + 20, Yval + 20))
    rec.setOutline('Black')
    rec.draw(win)
    #CREATED 4 VARIATIONS OF THE SMALLER PATCHES WITHIN THE 100x100 PATCH 
    if type == 1:
        rec = Rectangle(
            Point(Xval + 0, Yval + 0), Point(Xval + 5, Yval + 20))
        rec.setFill(colour)
        rec.draw(win)

        rec1 = Rectangle(
            Point(Xval + 10, Yval + 0), Point(Xval + 15, Yval + 20))
        rec1.setFill(colour)
        rec1.draw(win)
    if type == 2:
        rec = Rectangle(
            Point(Xval + 0, Yval + 0), Point(Xval + 20, Yval + 5))
        rec.setFill(colour)
        rec.draw(win)

        rec1 = Rectangle(
            Point(Xval + 0, Yval + 10), Point(Xval + 20, Yval + 15))
        rec1.setFill(colour)
        rec1.draw(win)
    if type == 3:
        rec = Rectangle(
            Point(Xval + 5, Yval + 0), Point(Xval + 10, Yval + 20))
        rec.setFill(colour)
        rec.draw(win)

        rec1 = Rectangle(
            Point(Xval + 15, Yval + 0), Point(Xval + 20, Yval + 20))
        rec1.setFill(colour)
        rec1.draw(win)
    if type == 4:
        rec = Rectangle(
            Point(Xval + 0, Yval + 5), Point(Xval + 20, Yval + 10))
        rec.setFill(colour)
        rec.draw(win)

        rec1 = Rectangle(
            Point(Xval + 0, Yval + 15), Point(Xval + 20, Yval + 20))
        rec1.setFill(colour)
        rec1.draw(win)
    
        

    

    
    
    



    

    

