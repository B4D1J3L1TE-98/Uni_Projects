
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 9736271
#    Student name: Brandon Dahl
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#


# Draw the grass as a big green rectangle
def draw_grass():
    
    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()


# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0) 
  
        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)


# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0) 

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)


# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))
                
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.

portrait_00 = [['Pet', 4, 1, '*'],
               ['Person B', 1, 1, '*'], 
               ['Person D', 0, 1, '*'],
               ['Person C', 2, 1, '*'],
               ['Person A', 3, 1, '*']]

# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.
#

# Draw the stick figures as per the provided data set
total_king_height = 180
king_height = total_king_height * 8/9
cross_height = total_king_height/9
cross_width = 12
king_width = 100
queen_height = 160
queen_width = 100
bishop_height = 140
bishop_width = 90
rook_height = 100
rook_width = 80
knight_height = 90
knight_width = 60



def draw_portrait(portrait):
    for figure in portrait:
        draw_figure(figure)

def draw_figure(figure):
    penup()
    goto((figure[1]-2)*location_width, 0)   #move to the location the figure should be drawn at
    #set the appropriate colours
    color('black', 'white')
    if figure[0] == 'Person A':         #if the figure to be drawn is a king
        draw_king(figure)
        #pendown()
        ##circle(50*figure[2])
        ##shape('circle')
        ##shapesize(5, 4, 1)
        ##fillcolor('white')
        ##stamp()
        #circle(50*figure[2])
        #goto((figure[1]-2)*150, 50*figure[2])
        #circle(50*figure[2])
    elif figure[0] == 'Person B':       #if the figure to be drawn is a queen
        draw_queen(figure)
    elif figure[0] == 'Person C':       #if the figure to be drawn is a bishop
        draw_bishop(figure)
    elif figure[0] == 'Person D':       #if the figure to be drawn is a rook
        draw_rook(figure)
    elif figure[0] == 'Pet':            #if the figure to be drawn is a knight (could use an else as well, but then typos could cause interesting runtime errors)
        draw_knight(figure)
        

def draw_knight(figure):
        #draw the base
        pendown()
        begin_fill()
        goto(xcor()-(knight_width / 2), ycor())
        goto(xcor(), ycor() + ((knight_height*3/40) * figure[2]))
        goto(xcor() + (knight_width/8), ycor() + ((knight_height/14) * figure[2]))
        goto(xcor() + (knight_width*3/4), ycor())
        goto(xcor() + (knight_width/8), ycor() - ((knight_height/14) * figure[2]))
        goto(xcor(), ycor() - ((knight_height*3/40) * figure[2]))
        goto((figure[1]-2)*location_width, 0)
        end_fill()
        penup()
        #upper base
        goto(xcor()-knight_width*3/8, figure[2]*knight_height*41/280)
        pendown()
        begin_fill()
        goto(((figure[1]-2)*location_width) - (knight_width*2/5), figure[2]*knight_height*2/7)
        #curve
        a = 0-1
        b = figure[2]*knight_height*3/7
        start_x = xcor()
        start_y = ycor()
        y=0
        while ycor() < (figure[2]*knight_height*4/7):
            goto(start_x - ((a*y**2+b*y)/((figure[2]*knight_height)*2/3)), start_y + y)
            y = y+1
        goto(((figure[1]-2)*location_width), figure[2]*knight_height*5/7)
        goto(xcor() - (knight_width/8), ycor())
        #curve
        a = 0-1
        b = knight_width/4
        start_x = xcor()
        start_y = ycor()
        x=0
        while xcor() > (((figure[1]-2)*location_width)-(knight_width*2/5)):
            goto(start_x - x, start_y + ((a*x**2+b*x)/(1800/(figure[2]*knight_height))))
            x = x+1
        goto(xcor(), figure[2]*knight_height*6/7)
        goto(((figure[1]-2)*location_width)+(knight_width*2/5), figure[2]*knight_height*9/10)
        goto(xcor(), figure[2]*knight_height*5/7)
        #curve
        a = 0-1
        b = figure[2]*knight_height*3/7
        start_x = xcor()
        start_y = ycor()
        y=0
        while ycor() > (figure[2]*knight_height*2/7):
            goto(start_x - ((a*y**2+b*y)/((figure[2]*knight_height)*2/3)), start_y - y)
            y = y+1
        goto(((figure[1]-2)*location_width)+(knight_width*3/8), figure[2]*knight_height*39/280)
        penup()
        end_fill()
        #mane
        goto(((figure[1]-2)*location_width)+(knight_width*1/5),figure[2]*knight_height*5/7)
        pendown()
        a = 0-1
        b = figure[2]*knight_height*3/7
        start_x = xcor()
        start_y = ycor()
        y=0
        while ycor() > (figure[2]*knight_height*3/14):
            goto(start_x - ((a*y**2+b*y)/((figure[2]*knight_height)*2/3)), start_y - y)
            y = y+1
        penup()

        #part B
        if figure[3] == '*':
            goto(((figure[1]-2)*location_width)-(knight_width/2), 10+figure[2]*knight_height)
            pendown()
            goto(xcor() + knight_width, ycor())
        

def draw_bishop(figure):
        #draw the base
        pendown()
        begin_fill()
        goto(xcor()-(bishop_width / 2), ycor())
        goto(xcor(), ycor() + ((bishop_height*3/40) * figure[2]))
        goto(xcor() + (bishop_width/10), ycor() + ((bishop_height/14) * figure[2]))
        goto(xcor() + (bishop_width*4/5), ycor())
        goto(xcor() + (bishop_width/10), ycor() - ((bishop_height/14) * figure[2]))
        goto(xcor(), ycor() - ((bishop_height*3/40) * figure[2]))
        goto((figure[1]-2)*location_width, 0)
        end_fill()
        penup()
        goto(xcor()-(bishop_width / 2), ycor())                                   #start of ring
        goto(xcor(), ycor() + ((bishop_height*3/40) * figure[2]))
        goto(xcor() + (bishop_width/5), ycor() + ((bishop_height/14) * figure[2]))
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*bishop_height/20))
        goto(xcor() + 3*bishop_width/5, ycor())
        goto(xcor(), ycor() - (figure[2]*bishop_height/20))
        goto(xcor() - 3*bishop_width/5, ycor())
        end_fill()
        penup()

        #draw the body
        goto(xcor() + (bishop_width/10), ycor() + ((bishop_height/20) * figure[2]))
        pendown()
        begin_fill()
        start_y = ycor()
        goto(xcor(), (bishop_height *7/10) * figure[2])
        part_height = ycor() - start_y
        goto(xcor() + (bishop_width*2/5), ycor())
        goto(xcor(), ycor() - part_height)
        end_fill()
        penup()

        #draw the ring (on the body)/ (between the body and the top)
        goto(xcor() - (bishop_width * 3/5), (bishop_height *5/10) * figure[2])
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (bishop_height/20 * figure[2]))
        goto(xcor() + (bishop_width * 4/5), ycor())
        goto(xcor(), (bishop_height*5/10) * figure[2])
        goto(xcor() - (bishop_width*4/5), ycor())
        end_fill()
        penup()
              
        #draw the top
        goto((figure[1]-2)*location_width-(bishop_width/5), figure[2]*bishop_height*6/10)
        pendown()
        begin_fill()
        goto(xcor() + (bishop_width*2/5), ycor())
        a=bishop_width / 9      #horizontal dimension in function to draw an oval
        b=bishop_height * figure[2] /14 #vertical dimension in function to draw an oval
        start_y = ycor()#-----------------------------------------------|
        start_x = xcor()#initial values by which RHS curve loop operates|
        y = 0           #-----------------------------------------------|
        RHS_x_precurve = xcor()
        RHS_y_precurve = ycor()
        while ycor() <= (figure[2]*bishop_height*13/20):             #while loop to draw curve on RHS |
            goto(start_x+(sqrt((b**2*a**2-a**2*(b-y)**2)/b**2)), start_y + y)                       #|
            y = y+1                                                 #---------------------------------
        RHS_x_prediagonal = xcor()
        RHS_y_prediagonal = ycor()
        goto((figure[1]-2)*location_width+(bishop_width/10),(figure[2]*bishop_height*19/20)) #move in straight diagonal to top of 'mitre'
        goto(xcor() - (bishop_width/5), ycor()) #move left
        goto((2*(figure[1]-2)*location_width)-(RHS_x_prediagonal), RHS_y_prediagonal) #diagonal on left
        penup()
        goto((2*(figure[1]-2)*location_width)-(RHS_x_precurve),RHS_y_precurve)
        pendown()
        start_y = ycor()#-----------------------------------------------|
        start_x = xcor()#initial values by which LHS curve loop operates|
        y = 0           #-----------------------------------------------|
        while ycor() <= (figure[2]*bishop_height*13/20)+1:    #while loop to draw curve on LHS |
            goto(start_x-(sqrt((b**2*a**2-a**2*(b-y)**2)/b**2)), start_y + y)                     #|
            y = y+1                                                #--------------------------------
        end_fill()
        penup()
        goto(((figure[1]-2)*location_width) - (bishop_width/5), figure[2]*bishop_height*7/10) #----------------------------------------------------------------|
        pendown()                                                                                                                                       #      |
        start_x = xcor()                                                                                                                                #      |
        start_y = ycor()                                                                                                                                #      |
        x=0                                                                                                                                             #      |
        while xcor() <= (2*(figure[1]-2)*location_width)-start_x:                                           #draw inverse quadratic line for 'face' of bishop--|
            goto(start_x+x, start_y + (((((bishop_width*2/5))*x)-(x**2))/(2800/(figure[2]*bishop_height))))                                             #      |
            x=x+1                                                                                                                                       #      |
        penup()#_______________________________________________________________________________________________________________________________________________|
        goto((figure[1]-2)*location_width-(bishop_width/10),(figure[2]*bishop_height*19/20))    #start of top 'point'
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*bishop_height/20))
        goto(xcor() + (bishop_width/5), ycor())
        goto(xcor(), ycor() - (figure[2]*bishop_height/20))
        end_fill()
        penup()

        #part B
        if figure[3] == '*':
            goto(((figure[1]-2)*location_width)-(bishop_width/2), 10+figure[2]*bishop_height)
            pendown()
            goto(xcor() + bishop_width, ycor())

def draw_king(figure):
        #draw the base
        pendown()
        begin_fill()
        goto(xcor()-(king_width / 2), ycor())
        goto(xcor(), ycor() + ((king_height*3/40) * figure[2]))
        goto(xcor() + (king_width/10), ycor() + ((king_height/7) * figure[2]))
        goto(xcor() + (king_width*4/5), ycor())
        goto(xcor() + (king_width/10), ycor() - ((king_height/7) * figure[2]))
        goto(xcor(), ycor() - ((king_height*3/40) * figure[2]))
        goto((figure[1]-2)*location_width, 0)
        end_fill()
        penup()
        goto(xcor()-(king_width / 2), ycor())                                   #start of ring
        goto(xcor(), ycor() + ((king_height*3/40) * figure[2]))
        goto(xcor() + (king_width/5), ycor() + ((king_height/7) * figure[2]))
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*king_height/10))
        goto(xcor() + 3*king_width/5, ycor())
        goto(xcor(), ycor() - (figure[2]*king_height/10))
        goto(xcor() - 3*king_width/5, ycor())
        end_fill()
        penup()

        #draw the body
        goto(xcor() + (king_width/10), ycor() + ((king_height/10) * figure[2]))
        pendown()
        begin_fill()
        goto(xcor(), (king_height *7/10) * figure[2])
        goto(xcor() + (king_width*2/5), ycor())
        goto(xcor(), king_height *89/280 * figure[2])
        end_fill()
        penup()

        #draw the rings between the body and the top
        goto(xcor() - (king_width * 3/5), (king_height *7/10) * figure[2])
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (king_height/40 * figure[2]))
        goto(xcor() + (king_width * 4/5), ycor())
        goto(xcor(), (king_height*7/10) * figure[2])
        goto(xcor() - (king_width*4/5), ycor())
        end_fill()
        penup()
        goto(xcor() + (king_width/10), ycor() + (king_height/40 * figure[2]))     #start of top 'ring'
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (king_height/40 * figure[2]))
        goto(xcor() + (king_width * 3/5), ycor())
        goto(xcor(), ycor() - (king_height/40 * figure[2]))
        goto(xcor() - (king_width * 3/5), ycor())
        end_fill()
        penup()

        #draw the top of the king
        goto(xcor() + (king_width/20), ycor()+(figure[2]*king_height/40))
        pendown()
        begin_fill()
        goto(xcor() - (king_width*3/20),figure[2]*king_height)
        goto(xcor()+king_width*4/5, ycor())
        goto(xcor() - (king_width*3/20),figure[2]*king_height*15/20)
        end_fill()
        penup()

        #draw the rings for the king's cross
        goto((figure[1]-2)*location_width-(king_width/4), figure[2]*king_height)
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*king_height/40))
        goto(xcor() + (king_width/2), ycor())
        goto(xcor(), ycor() - (figure[2]*king_height/40))
        end_fill()
        penup()
        goto((figure[1]-2)*location_width-(king_width/8), figure[2]*king_height*41/40)#start of top ring
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*king_height/40))
        goto(xcor() + (king_width/4), ycor())
        goto(xcor(), ycor() - (figure[2]*king_height/40))
        end_fill()
        penup()

        #draw the cross
        goto((figure[1]-2)*location_width-(cross_width/6), figure[2]*king_height*21/20)
        pendown()
        begin_fill()
        goto(xcor(), ycor()+(figure[2]*(cross_height-(king_height/20))/3))
        goto(xcor() - (cross_width/3), ycor())
        goto(xcor(), ycor()+(figure[2]*(cross_height-(king_height/20))/3))
        goto(xcor() + (cross_width/3), ycor())
        goto(xcor(), ycor()+(figure[2]*(cross_height-(king_height/20))/3))
        goto(xcor() + (cross_width/3), ycor())
        goto(xcor(), ycor()-(figure[2]*(cross_height-(king_height/20))/3))
        goto(xcor() + (cross_width/3), ycor())
        goto(xcor(), ycor()-(figure[2]*(cross_height-(king_height/20))/3))
        goto(xcor() - (cross_width/3), ycor())
        goto(xcor(), ycor()-(figure[2]*(cross_height-(king_height/20))/3))
        end_fill()
        penup()

        #part B
        if figure[3] == '*':
            goto(((figure[1]-2)*location_width)-(king_width/2), 10+figure[2]*total_king_height)
            pendown()
            goto(xcor() + king_width, ycor())
    
def draw_queen(figure):
        #draw the base
        pendown()
        begin_fill()
        goto(xcor()-(queen_width / 2), ycor())
        goto(xcor(), ycor() + ((queen_height/10) * figure[2]))
        goto(xcor() + (queen_width/10), ycor() + ((queen_height/7) * figure[2]))
        goto(xcor() + (queen_width*4/5), ycor())
        goto(xcor() + (queen_width/10), ycor() - ((queen_height/7) * figure[2]))
        goto(xcor(), ycor() - ((queen_height/10) * figure[2]))
        goto((figure[1]-2)*location_width, 0)
        end_fill()
        penup()
        goto(xcor()-(queen_width / 2), ycor())                  #start of ring
        goto(xcor(), ycor() + ((queen_height/10) * figure[2]))
        goto(xcor() + (queen_width/5), ycor() + ((queen_height/7) * figure[2]))
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*queen_height/20))
        goto(xcor() + 3*queen_width/5, ycor())
        goto(xcor(), ycor() - (figure[2]*queen_height/20))
        goto(xcor() - 3*queen_width/5, ycor())
        end_fill()
        penup()

        #draw the body
        goto(xcor() + (queen_width/10), ycor() + ((queen_height/20) * figure[2]))
        pendown()
        begin_fill()
        goto(xcor(), (queen_height *7/10) * figure[2])
        goto(xcor() + (queen_width*2/5), ycor())
        goto(xcor(), queen_height *41/140 * figure[2])
        end_fill()
        penup()

        #draw the rings between the body and the top
        goto(xcor() - (queen_width * 3/5), (queen_height *7/10) * figure[2])
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (queen_height/40 * figure[2]))
        goto(xcor() + (queen_width * 4/5), ycor())
        goto(xcor(), (queen_height*7/10) * figure[2])
        goto(xcor() - (queen_width*4/5), ycor())
        end_fill()
        penup()
        goto(xcor() + (queen_width/10), ycor() + (queen_height/40 * figure[2]))     #start of top 'ring'
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (queen_height/40 * figure[2]))
        goto(xcor() + (queen_width * 3/5), ycor())
        goto(xcor(), ycor() - (queen_height/40 * figure[2]))
        goto(xcor() - (queen_width * 3/5), ycor())
        end_fill()
        penup()

        #draw the top of the queen
        goto(xcor() + (queen_width/20), ycor()+(figure[2]*queen_height/40))
        pendown()
        begin_fill()
        goto(xcor(), ycor() + (figure[2]*queen_height/20))
        goto(xcor() - (queen_width*3/20),figure[2]*queen_height*19/20)
        goto(xcor()+queen_width*4/5, ycor())
        goto(xcor() - (queen_width*3/20),figure[2]*queen_height*16/20)
        goto(xcor(), ycor() - (figure[2]*queen_height/20))
        end_fill()
        penup()

        #draw the (semi)circle on the queen's 'head'
        goto((figure[1]-2)*location_width + (queen_height/20)+1, figure[2]*queen_height*19/20)
        pendown()
        begin_fill()
        setheading(90)   #necessary to draw the semicircle in the correct spot
        circle(queen_height/20, 180)
        end_fill()
        penup()

        #part B
        if figure[3] == '*':
            goto(((figure[1]-2)*location_width)-(queen_width/2), 10+figure[2]*queen_height)
            pendown()
            goto(xcor() + queen_width, ycor())
        

def draw_rook(figure):       
        #draw the base
        pendown()
        begin_fill()
        goto(xcor()-(rook_width / 2), ycor())
        goto(xcor(), ycor() + ((rook_height/10) * figure[2]))
        goto(xcor() + (rook_width/5), ycor() + ((rook_height/7) * figure[2]))
        goto(xcor() + (rook_width*3/5), ycor())
        goto(xcor() + (rook_width/5), ycor() - ((rook_height/7) * figure[2]))
        goto(xcor(), ycor() - ((rook_height/10) * figure[2]))
        goto((figure[1]-2)*location_width, 0)
        end_fill()
        penup()

        #draw the body
        goto(xcor() - (rook_width * 3/10), ycor() + ((rook_height*17/70)*figure[2]))
        pendown()
        begin_fill()
        goto(xcor(), (rook_height *7/10) * figure[2])
        goto(xcor() + (rook_width*3/5), ycor())
        goto(xcor(), rook_height *17/70 * figure[2])
        end_fill()
        penup()

        #draw the ring between the body and the top
        goto(xcor() - (rook_width * 3/5), (rook_height *7/10) * figure[2])
        pendown()
        begin_fill()
        goto(xcor() - (rook_width/20), ycor())
        goto(xcor(), ycor() + (rook_height/20 * figure[2]))
        goto(xcor() + (rook_width * 7/10), ycor())
        goto(xcor(), (rook_height*7/10) * figure[2])
        goto(xcor() - (rook_width/20), ycor())
        end_fill()
        penup()
        
        #draw the top of the rook
        goto((figure[1]-2)*location_width - (rook_width * 4/10), figure[2] * rook_height * 15/20)
        pendown()
        begin_fill()
        ridge_width = rook_width/5
        goto(xcor(), rook_height * figure[2])
        goto(xcor() + ridge_width, ycor())            
        goto(xcor(), ycor() - (figure[2] * rook_height /15))            #
        goto(xcor() + ((rook_width*4/5) - (3*(ridge_width)))/2, ycor())# dip 1
        goto(xcor(), ycor() + (figure[2] * rook_height /15))            #
        goto(xcor() + ridge_width, ycor())
        goto(xcor(), ycor() - (figure[2] * rook_height /15))            #
        goto(xcor() + ((rook_width*4/5) - (3*(ridge_width)))/2, ycor())# dip 2
        goto(xcor(), ycor() + (figure[2] * rook_height /15))            #
        goto(xcor() + ridge_width, ycor())
        goto(xcor(), figure[2] * rook_height * 15/20)
        goto((figure[1]-2)*location_width - (rook_width*4/10), ycor())
        end_fill()
        penup()
        
        #part B
        if figure[3] == '*':
            goto(((figure[1]-2)*location_width)-(rook_width/2), 10+figure[2]*rook_height)
            pendown()
            goto(xcor() + rook_width, ycor())
        
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
draw_grass()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Chess Pieces')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the lestocations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False
draw_locations(True)
draw_labels(True)
mark_coords(True)

# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False
tracer(True)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_00) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------------------------

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

