
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9736271
#    Student name: Brandon Dahl
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything 
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *

# Import the SQL functions
from sqlite3 import *

#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#
def save_pressed(top10): #Event to save top ten lists. top10 (the parameter) will be a list, containing the top 10 in rank order (from 1 to 10)
    # Create a connection to the database.
    connection = connect(database = 'top_ten.db')

    # Get a cursor on the database.  This allows you the execution of SQL queries and reading of the results.
    top10_db = connection.cursor()

    #Execute an SQL query which empties the table
    top10_db.execute("DELETE FROM Top_Ten WHERE Description IS NOT NULL")

    #Execute an SQL query that saves the list called top10 into the table, with rank
    for i in range(0, 10):
        top10_db.execute('INSERT INTO Top_Ten VALUES (' + str(i+1) + ', "' + top10[i] + '")')

    # Commit the changes to the database
    connection.commit()

    # Close the cursor.
    top10_db.close()

    # Close the database connection.
    connection.close()


#Three different commands/events, but each maps to the save Event (above) from a different window.
#This intermediate step is useful because it makes it easier to define which values are being saved into the database.
def nrl_save_pressed():
    save_pressed(nrl_top10)

def chess_save_pressed():
    save_pressed(chess_top10)

def songs_save_pressed():
    save_pressed(songs_top10)


def nrl_pressed():
    # retrieve source code from the website and store the source code as a string
    nrl_url = 'https://www.nrl.com/draw/telstrapremiership/ladder/tabid/10251/default.aspx' #NRL ladder
    nrl_page = urlopen(nrl_url).read()

    global nrl_top10 #variable was made global for PART B
    nrl_top10 = findall('</div>([A-Z][a-z]*)</td>', nrl_page)[:10] #Find names of NRL teams
    
    # Create a new 'top level' window on the screen
    nrl_window = Toplevel()

    # Give the window a title
    nrl_window.title('Top 10 NRL Teams on the Ladder')

    #Resize the nrl window
    nrl_window.geometry('700x500')

    #Change the background colour
    nrl_window.configure(bg = 'Green')

    # Add the image
    nrl_image = urlopen('http://blog.safepokies.com/wp-content/uploads/sites/2/2016/05/nrl.png').read() #save the image as a 'string'
    nrl_image = image_to_PhotoImage(nrl_image) #no need to resize image, its dimensions are already ideal
    nrl_image_label = Label(nrl_window, image = nrl_image, bg = 'Green') #create a label for the image to appear in
    nrl_image_label.place(x = 60, y = 100) #place the label (image) in the window, to the left of the text

    #loop through the list of top 10 NRL teams, printing them out alongside their rank
    for num in range(0, 10):
        new_rank_label = Label(nrl_window, text = '(' + str(num+1) + ')', font = ('Calibri', 20), fg = 'Black', bg = 'Green')
        new_team_label = Label(nrl_window, text = nrl_top10[num], font = ('Calibri', 20), fg = 'Blue', bg = 'Green')
        new_rank_label.place(x = 410 - ((1+((num+1) / 10))*12), y = 10 + 45*num)
        new_team_label.place(x = 450, y = 10 + 45*num)

    #Add line between 8th and 9th ranked teams
    finals_line = Label(nrl_window, text = '______________________________'*3, font = ('Calibri', 5), fg = 'Red', bg = 'Green')
    finals_line.place(x = 355, y = 355)

    #Display the URL
    nrl_url_label = Label(nrl_window, text = 'Data retrieved from: ' + nrl_url, font = ('Calibri', 12), fg = 'Yellow', bg = 'Green')
    nrl_url_label.place(x = 20, y = 470)

    #PART B - Create 'Save' Button
    nrl_save_button = Button(nrl_window, text = 'Save This List', command = nrl_save_pressed)
    nrl_save_button.place(x = 610, y = 10)

    # Start the new window's event loop
    nrl_window.mainloop()

def chess_pressed():
    # retrieve source code from the website and store the source code as a string
    chess_url = 'http://www.365chess.com/top-chess-players.php' #highest rated chess players worldwide
    chess_page = urlopen(chess_url).read()

    global chess_top10 #variable was made global for PART B
    #Find names of chess players
    chess_top10 = findall('<td><a href="players.*">([A-Z]*\.*[a-z]*-* *[A-Z]*\.*[a-z]* [A-Z]*\.*[a-z]*-* *[A-Z]*\.*[a-z]*)</a></td>', chess_page)[:10]
    #^^^very long-winded, but using .* resulted in the sting extending to the end of the last player (at best), and this was the simplest way to allow for all possible ways that a player's name can be written/typed

    # Create a new 'top level' window on the screen
    chess_window = Toplevel()

    # Give the window a title
    chess_window.title('Top 10 International Chess Players by FIDE Rating')

    #Resize the chess window
    chess_window.geometry('700x500')

    #Change the background colour
    chess_window.configure(bg = 'Cyan')

    # Add the image
    chess_image = urlopen('http://i.stack.imgur.com/IDssw.jpg').read() #save the image as a 'string'
    chess_image = image_to_PhotoImage(chess_image, 300, 300) #Image resizing is very unrestrictive as the image is of a square chessboard
    chess_image_label = Label(chess_window, image = chess_image, bg = 'Cyan') #create a label for the image to appear in
    chess_image_label.place(x = 350, y = 100) #place the label (image) in the window, to the right of the text

    #loop through the list of top 10 chess players, print them all out, with numbers
    for num in range(0, 10):        #the for loop allows the text colours to alternate for a checkered effect
        if num % 2 == 0:
            TextColour = 'White'
            OtherTextColour = 'Black'
        else:
            TextColour = 'Black'
            OtherTextColour = 'White'
        new_rank_label = Label(chess_window, text = str(num+1) + '.', font = ('Arial', 15), fg = TextColour, bg = 'Cyan')
        new_player_label = Label(chess_window, text = chess_top10[num], font = ('Arial', 15), fg = OtherTextColour, bg = 'Cyan')
        new_rank_label.place(x = 25 - ((1+((num+1) / 10))*12), y = 50 + 40*num)
        new_player_label.place(x = 40, y = 50 + 40*num)

    #Display the URL
    chess_url_label = Label(chess_window, text = 'Data retrieved from: ' + chess_url, font = ('Arial', 10), fg = 'Magenta', bg = 'Cyan')
    chess_url_label.place(x = 20, y = 460)

    #PART B - Create 'Save' Button
    chess_save_button = Button(chess_window, text = 'Save This List', command = chess_save_pressed)
    chess_save_button.place(x = 610, y = 10)
    
    # Start the new window's event loop
    chess_window.mainloop()

def songs_pressed():
    # retrieve source code from the website and store the source code as a string
    songs_url = 'http://www.billboard.com/charts/hot-100' #'hottest hits' songs chart
    songs_page = urlopen(songs_url).read()

    global songs_top10 #variable was made global for PART B
    songs_top10 = findall('"Song Hover-(.*)" data-songtitle=""', songs_page)[:10] #Find song titles 
    #replace HTML markup for apostrophe(') with an actual apostrophe
    for index in range(1, 10):
        songs_top10[index] = songs_top10[index].replace('&#039;', "'")
    
    # Create a new 'top level' window on the screen
    songs_window = Toplevel()

    # Give the window a title
    songs_window.title('Top 10 Songs According to billboard.com')

    #Resize the songs window
    songs_window.geometry('500x500')

    #Change the background colour
    songs_window.configure(bg = 'Black')

    # Add the image
    songs_image = urlopen('https://bennettknowsdotcom.files.wordpress.com/2013/03/billboard-hot-100-this-weeks-top-10-songs.jpeg').read() #save the image to a 'string'
    songs_image = image_to_PhotoImage(songs_image, 264, 137) #resize the image (this is half its natural height and half its natural width) to fit
    songs_image_label = Label(songs_window, image = songs_image, bg = 'Cyan') #create a label for the image to appear in
    songs_image_label.place(x = 10, y = 310) #place the label (image) in the window

    #loop through the list of top 10 songs, print them all out, with numbers
    for num in range(0, 10):
        new_rank_label = Label(songs_window, text = '[' + str(num+1) + ']', font = ('Cambria', 12), fg = 'Green', bg = 'Black')
        new_song_label = Label(songs_window, text = songs_top10[num], font = ('Cambria', 12), fg = 'Green', bg = 'Black')
        new_rank_label.place(x = (60 + (30 * num)) - ((1+((num+1) / 10))*7), y = 30 + 35*num)
        new_song_label.place(x = 80 + (30 * num), y = 30 + 35*num)

    #Display the URL
    songs_url_label = Label(songs_window, text = 'Data retrieved from: ' + songs_url, font = ('Cambria', 8), fg = 'White', bg = 'Black')
    songs_url_label.place(x = 20, y = 480)

    #PART B - Create 'Save' Button
    songs_save_button = Button(songs_window, text = 'Save This List', command = songs_save_pressed)
    songs_save_button.place(x = 410, y = 10)

    # Start the new window's event loop
    songs_window.mainloop()

intro_window = Tk() #create the 'splash' window
intro_window.title('Top 10 FIDE Chess Players, NRL Teams, and Songs') #give it a title
intro_window.geometry('600x600') #manually set the dimensions so the window is large enough to put stuff on

#Create the 3 buttons, each with the same height and width (apparently not in pixels) to keep the layout organized
nrl_button = Button(intro_window, text = 'Top 10 NRL Teams', command = nrl_pressed,
                    width = 20, height = 2)
chess_button = Button(intro_window, text = 'Top 10 Chess Players', command = chess_pressed,
                    width = 20, height = 2)
songs_button = Button(intro_window, text = 'Top 10 Songs', command = songs_pressed,
                    width = 20, height = 2)

#equally space the buttons apart at the bottom of the window
nrl_button.place(x = 20, y = 550)
chess_button.place(x = 220, y = 550)
songs_button.place(x = 420, y = 550)

# Add the 'splash' image
intro_image = urlopen('http://hamptonsrealestateshowcase.com/blog/wp-content/uploads/2013/09/TOP-10.jpg').read()
intro_image_resized = image_to_PhotoImage(intro_image, 500, 500)
intro_image_label = Label(intro_window, image = intro_image_resized)
intro_image_label.place(x = 50, y = 30)

#start the loop to ensure that user interactions trigger events/commands
intro_window.mainloop()

